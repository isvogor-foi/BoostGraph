#include <iostream>
#include <iomanip>

#include <boost/graph/undirected_graph.hpp>
#include <boost/graph/exterior_property.hpp>
#include <boost/graph/floyd_warshall_shortest.hpp>
#include <boost/graph/dijkstra_shortest_paths.hpp>
#include <boost/graph/closeness_centrality.hpp>
#include <boost/graph/property_maps/constant_property_map.hpp>
#include <boost/graph/graphml.hpp>
#include <boost/graph/graphviz.hpp>


using namespace std;
using namespace boost;


typedef float Weight;
typedef boost::property<boost::edge_weight_t, Weight> WeightProperty;
typedef boost::property<boost::vertex_name_t, std::string> NameProperty;

typedef boost::adjacency_list < boost::listS, boost::vecS, boost::undirectedS, NameProperty, WeightProperty > Graph;

typedef boost::graph_traits < Graph >::vertex_descriptor Vertex;
typedef boost::graph_traits < Graph >::edge_descriptor Edge;

typedef constant_property_map<Edge, int> WeightMap;
typedef boost::property_map < Graph, boost::vertex_index_t >::type IndexMap;
typedef boost::property_map < Graph, boost::vertex_name_t >::type NameMap;

typedef boost::iterator_property_map < Vertex*, IndexMap, Vertex, Vertex& > PredecessorMap;
typedef boost::iterator_property_map < Weight*, IndexMap, Weight, Weight& > DistanceMap;;

void WriteGraph(const Graph& g, const std::string& filename);

int main(int argc, char *argv[])
{
    Graph g;
    dynamic_properties dp;

    std::ifstream inFile;
    inFile.open("../graph/graph.xml", std::ifstream::in);
    read_graphml(inFile, g, dp);
    cout<<"Vertices/edges: " << num_vertices(g) << " / " << num_edges(g) << endl;


    // Create things for Dijkstra
    std::vector<Vertex> predecessors(boost::num_vertices(g)); // To store parents
    std::vector<Weight> distances(boost::num_vertices(g)); // To store distances

    IndexMap indexMap = boost::get(boost::vertex_index, g);
    PredecessorMap predecessorMap(&predecessors[0], indexMap);
    DistanceMap distanceMap(&distances[0], indexMap);


    NameMap nameMap = boost::get(boost::vertex_name, g);
    for(int i = 0; i <= num_vertices(g); i++){
    	stringstream ss;
    	ss << i;
    	nameMap[i] = "n" + ss.str();
    }

    graph_traits<Graph>::vertex_iterator i, end;
    for(tie(i, end) = vertices(g); i != end; ++i) {
    	cout << "Name: " << get(nameMap, *i) << endl;
    }

    for(int i = 0; i < num_vertices(g); i++){
    	cout << "Distance: " << distanceMap[i] << endl;
    	distances[i] = 1;
    	distanceMap[i] = 1;
    }


    // sets the weight
    graph_traits<Graph>::edge_iterator ei, ee;
    for(tie(ei, ee) = edges(g); ei != ee; ++ei){
    	put(edge_weight, g, *ei, 1);
    	cout << "Distance: " << get(edge_weight, g, *ei) << endl;
    }




    Vertex v0 = vertex(11, g);
    boost::dijkstra_shortest_paths(g, v0, boost::distance_map(distanceMap).predecessor_map(predecessorMap));

    BGL_FORALL_VERTICES(v, g, Graph)
    {
      std::cout << "distance(" << nameMap[v0] << ", " << nameMap[v] << ") = " << distanceMap[v] << ", ";
      std::cout << "predecessor(" << nameMap[v] << ") = " << nameMap[predecessorMap[v]] << std::endl;
    }

    /////////////////////////

    typedef std::vector<Graph::edge_descriptor> PathType;

     PathType path;

     Vertex v3= vertex(25, g);
     Vertex v = v3; // We want to start at the destination and work our way back to the source
     for(Vertex u = predecessorMap[v]; // Start by setting 'u' to the destintaion node's predecessor
         u != v; // Keep tracking the path until we get to the source
         v = u, u = predecessorMap[v]) // Set the current vertex to the current predecessor, and the predecessor to one level up
     {
       std::pair<Graph::edge_descriptor, bool> edgePair = boost::edge(u, v, g);
       Graph::edge_descriptor edge = edgePair.first;

       path.push_back( edge );
     }

     // Write shortest path
     std::cout << "Shortest path from v0 to v3:" << std::endl;
     float totalDistance = 0;
     for(PathType::reverse_iterator pathIterator = path.rbegin(); pathIterator != path.rend(); ++pathIterator)
     {
       std::cout << nameMap[boost::source(*pathIterator, g)] << " -> " << nameMap[boost::target(*pathIterator, g)]
                 << " = " << boost::get( boost::edge_weight, g, *pathIterator ) << std::endl;

     }

     std::cout << std::endl;

     std::cout << "Distance: " << distanceMap[v3] << std::endl;

    WriteGraph(g, "after.dot");
    return 0;
}

void WriteGraph(const Graph& g, const std::string& filename)
{
  std::ofstream graphStream;
  graphStream.open(filename.c_str());
  boost::write_graphviz(graphStream, g );
  graphStream.close();
}

