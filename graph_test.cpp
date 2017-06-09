/*
 * FindCenter.cpp
 *
 *  Created on: 2017-05-26
 *      Author: ivan
 */

#include <iostream>
#include "FindCenter.h"

using namespace std;
using namespace graph_buzz;

int main(int argc, char *argv[])
{
	std::string s = "<?xml version='1.0' encoding='UTF-8'?><graphml xmlns='http://graphml.graphdrawing.org/xmlns' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd'><graph id='G' edgedefault='undirected'><node id='n0'></node><node id='n1'></node><node id='n2'></node><node id='n3'></node><node id='n100'></node><edge id='e0' source='n0' target='n1'></edge><edge id='e1' source='n0' target='n2'></edge><edge id='e2' source='n0' target='n100'></edge><edge id='e3' source='n1' target='n0'></edge><edge id='e4' source='n1' target='n2'></edge><edge id='e5' source='n1' target='n3'></edge><edge id='e6' source='n1' target='n100'></edge><edge id='e7' source='n2' target='n0'></edge><edge id='e8' source='n2' target='n1'></edge><edge id='e9' source='n2' target='n3'></edge><edge id='e10' source='n2' target='n100'></edge><edge id='e11' source='n3' target='n1'></edge><edge id='e12' source='n3' target='n2'></edge><edge id='e13' source='n100' target='n0'></edge><edge id='e14' source='n100' target='n1'></edge><edge id='e15' source='n100' target='n2'></edge></graph></graphml>";
	GraphOperations go;

	std::cout << go.SayHello() << std::endl;

	char *a = new char[s.size()+1];
	a[s.size()]=0;
	memcpy(a,s.c_str(),s.size());

	std::string result = go.CreateTree(a);

	std::cout << "Result (T): " << result << std::endl;
	//std::cout << "Second: " << go.counterix() << std::endl;
	return 0;
}
