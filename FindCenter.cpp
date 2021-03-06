/*
 * FindCenter.cpp
 *
 *  Created on: 2017-05-26
 *      Author: ivan
 */

#include <iostream>
#include <iomanip>
#include <algorithm>

#include "FindCenter.h"

using namespace std;
using namespace graph_buzz;

void GraphOperations::WriteGraphToFile(const Graph& g, const std::string& filename)
{
  std::ofstream graphStream;
  graphStream.open(filename.c_str());
  boost::write_graphviz(graphStream, g );
  graphStream.close();
}
std::string GraphOperations::WriteGraphToString(const Graph& g)
{
  std::stringstream stream;
  boost::write_graphviz(stream, g);
  return stream.str();
}

void GraphOperations::OpenFromXML(Graph& g, dynamic_properties& dp, const std::string& filename){
	std::ifstream inFile;

	inFile.open(filename.c_str(), std::ifstream::in);
	read_graphml(inFile, g, dp);

    //cout << "File opened successfully!" << endl;
	//cout << "Vertices/edges: " << num_vertices(g) << " / " << num_edges(g) << endl;
}

void GraphOperations::OpenFromString(Graph& g, dynamic_properties& dp, char buffer []){
	membuf sbuf(buffer, buffer + strlen(buffer));
	std::istream in(&sbuf);
	read_graphml(in, g, dp);

    //cout << "File opened successfully!" << endl;
	//cout << "Vertices/edges: " << num_vertices(g) << " / " << num_edges(g) << endl;
}

void GraphOperations::SetNames(Graph& g, NameMap& nameMap){
	std::cout<< "Ready: " << num_vertices(g) << std::endl;
    for(int i = 0; i < num_vertices(g); i++){
    	std::stringstream ss;
    	ss << i;
    	nameMap[i] = i;
    }

}

void GraphOperations::SetWeights(Graph& g, float weight){
    // sets the weight
    graph_traits<Graph>::edge_iterator ei, ee;
    for(tie(ei, ee) = edges(g); ei != ee; ++ei){
    	put(edge_weight, g, *ei, weight);
    	//cout << "Distance: " << get(edge_weight, g, *ei) << endl;
    }
}

void GraphOperations::RemoveEdges(Graph &g){
    graph_traits<Graph>::vertex_iterator i, end;
    for(tie(i, end) = vertices(g); i != end; ++i) {
    	//cout << "Name: " << get(nameMap, *i) << endl;
    	clear_vertex(*i, g);
    }
}

void GraphOperations::PrintGraphProperties(Graph& g, NameMap& nameMap, DistanceMap& distanceMap){
    graph_traits<Graph>::vertex_iterator i, end;
    for(tie(i, end) = vertices(g); i != end; ++i) {
    	cout << "Name: " << get(nameMap, *i) << endl;
    }

    for(int i = 0; i < num_vertices(g); i++){
    	cout << "Distance: " << distanceMap[i] << endl;
    }
}

std::vector< std::pair<int, float> > GraphOperations::GetCentralities(Graph& g, NameMap& nameMap, IndexMap& indexMap){
	DistanceMatrix dsts(num_vertices(g));
	DistanceMatrixMap dm(dsts, g);
	WeightMap wm(1);
    floyd_warshall_all_pairs_shortest_paths(g, dm, weight_map(wm));

    // centrality
    ClosenessContainer cents(num_vertices(g));
    ClosenessMap cm(cents, g);
    all_closeness_centralities(g, dm, cm);

    std::vector< std::pair<int, float> > centralities;
    graph_traits<Graph>::vertex_iterator i, end;
    for(boost::tie(i, end) = vertices(g); i != end; ++i) {
        //cout << "Centrality of " <<  get(nameMap, *i) << " :" << get(cm, *i) << endl;
        centralities.push_back(std::make_pair((int)get(indexMap, *i),(float)get(cm, *i)));
    }

    std::sort(centralities.begin(), centralities.end(), boost::bind(&std::pair<int, float>::second, _1) > boost::bind(&std::pair<int, float>::second, _2));
    /*
    for(std::vector< std::pair<int, float> >::iterator i = centralities.begin(); i != centralities.end(); ++i){
    	std::cout<<"Vec: " << i->first << ": " << i->second << endl;
    }
    */

    return centralities;
}

std::string GraphOperations::CreateTree(std::string text){

		//std::cout << "Text: " << text << std::endl;
		Graph g;
		dynamic_properties dp;
		//char text1 [] = "<?xml version='1.0' encoding='UTF-8'?><graphml xmlns='http://graphml.graphdrawing.org/xmlns' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd'><graph id='G' edgedefault='undirected'><node id='n0'></node><node id='n1'></node><node id='n2'></node><node id='n3'></node><node id='n100'></node><edge id='e0' source='n0' target='n1'></edge><edge id='e1' source='n0' target='n2'></edge><edge id='e2' source='n0' target='n100'></edge><edge id='e3' source='n1' target='n0'></edge><edge id='e4' source='n1' target='n2'></edge><edge id='e5' source='n1' target='n3'></edge><edge id='e6' source='n1' target='n100'></edge><edge id='e7' source='n2' target='n0'></edge><edge id='e8' source='n2' target='n1'></edge><edge id='e9' source='n2' target='n3'></edge><edge id='e10' source='n2' target='n100'></edge><edge id='e11' source='n3' target='n1'></edge><edge id='e12' source='n3' target='n2'></edge><edge id='e13' source='n100' target='n0'></edge><edge id='e14' source='n100' target='n1'></edge><edge id='e15' source='n100' target='n2'></edge></graph></graphml>";
		char *a = new char[text.size()+1];
		a[text.size()]=0;
		memcpy(a,text.c_str(),text.size());

		OpenFromString(g, dp, a);

		// Create data for Dijkstra
		std::vector<Vertex> predecessors(boost::num_vertices(g)); 	// To store parents
		std::vector<Weight> distances(boost::num_vertices(g)); 		// To store distances


		IndexMap indexMap = boost::get(boost::vertex_index, g);
		NameMap nameMap = boost::get(boost::vertex_name, g);

		PredecessorMap predecessorMap(&predecessors[0], indexMap);
		DistanceMap distanceMap(&distances[0], indexMap);


		// set names and weights
		SetNames(g, nameMap);
		SetWeights(g, 1);
		//PrintGraphProperties(g, nameMap, distanceMap);

		// floyd warshall
		std::vector< std::pair<int, float> > centralities = GetCentralities(g, nameMap, indexMap);
		// dijkstra

		Vertex v0 = vertex(centralities[0].first, g); // < change
		boost::dijkstra_shortest_paths(g, v0, boost::distance_map(distanceMap).predecessor_map(predecessorMap));

		/*
		BGL_FORALL_VERTICES(v, g, Graph)
		{
			std::cout << "distance(" << nameMap[v0] << ", " << nameMap[v] << ") = " << distanceMap[v] << ", ";
			std::cout << "predecessor(" << nameMap[v] << ") = " << nameMap[predecessorMap[v]] << std::endl;
		}
		 */
		/////////////////////////

		Graph tree;
		boost::copy_graph(g, tree);

		RemoveEdges(tree);
		typedef std::vector<Graph::edge_descriptor> PathType;

		 for(int i = 0; i < num_vertices(g); i++){
			 PathType path;
			 Vertex v3= vertex(i, g);
			 Vertex v = v3; // We want to start at the destination and work our way back to the source
			 for(Vertex u = predecessorMap[v];  u != v; v = u, u = predecessorMap[v])
			 {
				std::pair<Graph::edge_descriptor, bool> edgePair = boost::edge(u, v, g);
				Graph::edge_descriptor edge = edgePair.first;
				path.push_back( edge );
				if(boost::edge(u,v, tree).second == false)
					add_edge(u, v, 1, tree);	// source, destination, weight, tree
			 }

			 // Write shortest path
			 /*
			 std::cout << "Shortest to " << i  << std::endl;
			 float totalDistance = 0;
			 for(PathType::reverse_iterator pathIterator = path.rbegin(); pathIterator != path.rend(); ++pathIterator)
			 {
			   std::cout << nameMap[boost::source(*pathIterator, g)] << " -> " << nameMap[boost::target(*pathIterator, g)]
						 << " = " << boost::get( boost::edge_weight, g, *pathIterator ) << std::endl;

			 }

			 std::cout << std::endl;
			 std::cout << "Distance: " << distanceMap[v3] << std::endl;
			 */
		 }
		 return WriteGraphToString(tree);

		//return text;
}

std::string GraphOperations::SayHello(){
	return "Hello";
}
