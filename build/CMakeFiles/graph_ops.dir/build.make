# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ivan/dev/eclipse/workspace/BoostGraph

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ivan/dev/eclipse/workspace/BoostGraph/build

# Include any dependencies generated for this target.
include CMakeFiles/graph_ops.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/graph_ops.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/graph_ops.dir/flags.make

CMakeFiles/graph_ops.dir/FindCenter.cpp.o: CMakeFiles/graph_ops.dir/flags.make
CMakeFiles/graph_ops.dir/FindCenter.cpp.o: ../FindCenter.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ivan/dev/eclipse/workspace/BoostGraph/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/graph_ops.dir/FindCenter.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/graph_ops.dir/FindCenter.cpp.o -c /home/ivan/dev/eclipse/workspace/BoostGraph/FindCenter.cpp

CMakeFiles/graph_ops.dir/FindCenter.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/graph_ops.dir/FindCenter.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ivan/dev/eclipse/workspace/BoostGraph/FindCenter.cpp > CMakeFiles/graph_ops.dir/FindCenter.cpp.i

CMakeFiles/graph_ops.dir/FindCenter.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/graph_ops.dir/FindCenter.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ivan/dev/eclipse/workspace/BoostGraph/FindCenter.cpp -o CMakeFiles/graph_ops.dir/FindCenter.cpp.s

CMakeFiles/graph_ops.dir/FindCenter.cpp.o.requires:

.PHONY : CMakeFiles/graph_ops.dir/FindCenter.cpp.o.requires

CMakeFiles/graph_ops.dir/FindCenter.cpp.o.provides: CMakeFiles/graph_ops.dir/FindCenter.cpp.o.requires
	$(MAKE) -f CMakeFiles/graph_ops.dir/build.make CMakeFiles/graph_ops.dir/FindCenter.cpp.o.provides.build
.PHONY : CMakeFiles/graph_ops.dir/FindCenter.cpp.o.provides

CMakeFiles/graph_ops.dir/FindCenter.cpp.o.provides.build: CMakeFiles/graph_ops.dir/FindCenter.cpp.o


# Object files for target graph_ops
graph_ops_OBJECTS = \
"CMakeFiles/graph_ops.dir/FindCenter.cpp.o"

# External object files for target graph_ops
graph_ops_EXTERNAL_OBJECTS =

libgraph_ops.so: CMakeFiles/graph_ops.dir/FindCenter.cpp.o
libgraph_ops.so: CMakeFiles/graph_ops.dir/build.make
libgraph_ops.so: /usr/lib/x86_64-linux-gnu/libboost_graph.so
libgraph_ops.so: CMakeFiles/graph_ops.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ivan/dev/eclipse/workspace/BoostGraph/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libgraph_ops.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/graph_ops.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/graph_ops.dir/build: libgraph_ops.so

.PHONY : CMakeFiles/graph_ops.dir/build

CMakeFiles/graph_ops.dir/requires: CMakeFiles/graph_ops.dir/FindCenter.cpp.o.requires

.PHONY : CMakeFiles/graph_ops.dir/requires

CMakeFiles/graph_ops.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/graph_ops.dir/cmake_clean.cmake
.PHONY : CMakeFiles/graph_ops.dir/clean

CMakeFiles/graph_ops.dir/depend:
	cd /home/ivan/dev/eclipse/workspace/BoostGraph/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ivan/dev/eclipse/workspace/BoostGraph /home/ivan/dev/eclipse/workspace/BoostGraph /home/ivan/dev/eclipse/workspace/BoostGraph/build /home/ivan/dev/eclipse/workspace/BoostGraph/build /home/ivan/dev/eclipse/workspace/BoostGraph/build/CMakeFiles/graph_ops.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/graph_ops.dir/depend

