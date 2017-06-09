cmake_minimum_required(VERSION 2.6)
 
Project(ConstructGraph)
 
set(Boost_USE_MULTITHREADED ON)
FIND_PACKAGE(Boost 1.38 COMPONENTS required)
 
INCLUDE_DIRECTORIES(${INCLUDE_DIRECTORIES} ${Boost_INCLUDE_DIRS})
LINK_DIRECTORIES(${LINK_DIRECTORIES} ${Boost_LIBRARY_DIRS})

SET(HEADERS FindCenter.h)

ADD_EXECUTABLE(ConstructGraph CreateGraph.cpp)
target_link_libraries(ConstructGraph)

MESSAGE( STATUS "Include -> : " ${INCLUDE_DIRECTORIES} )

ADD_EXECUTABLE(Closeness 
	Closeness.cpp )
target_link_libraries(Closeness /usr/lib/x86_64-linux-gnu/libboost_graph.so)

ADD_EXECUTABLE(Closeness2
	Closeness2.cpp )
target_link_libraries(Closeness2 /usr/lib/x86_64-linux-gnu/libboost_graph.so)

ADD_EXECUTABLE(Dijkstra Dijkstra.cpp )
target_link_libraries(Dijkstra /usr/lib/x86_64-linux-gnu/libboost_graph.so)

# build SO 
ADD_LIBRARY(graph_ops SHARED FindCenter.cpp ${HEADERS})
target_link_libraries(graph_ops /usr/lib/x86_64-linux-gnu/libboost_graph.so)

ADD_EXECUTABLE(graph_test graph_test ${HEADERS})
target_link_libraries(graph_test graph_ops /usr/lib/x86_64-linux-gnu/libboost_graph.so)

