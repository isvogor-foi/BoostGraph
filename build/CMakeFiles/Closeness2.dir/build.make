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
include CMakeFiles/Closeness2.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Closeness2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Closeness2.dir/flags.make

CMakeFiles/Closeness2.dir/Closeness2.cpp.o: CMakeFiles/Closeness2.dir/flags.make
CMakeFiles/Closeness2.dir/Closeness2.cpp.o: ../Closeness2.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ivan/dev/eclipse/workspace/BoostGraph/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Closeness2.dir/Closeness2.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Closeness2.dir/Closeness2.cpp.o -c /home/ivan/dev/eclipse/workspace/BoostGraph/Closeness2.cpp

CMakeFiles/Closeness2.dir/Closeness2.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Closeness2.dir/Closeness2.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ivan/dev/eclipse/workspace/BoostGraph/Closeness2.cpp > CMakeFiles/Closeness2.dir/Closeness2.cpp.i

CMakeFiles/Closeness2.dir/Closeness2.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Closeness2.dir/Closeness2.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ivan/dev/eclipse/workspace/BoostGraph/Closeness2.cpp -o CMakeFiles/Closeness2.dir/Closeness2.cpp.s

CMakeFiles/Closeness2.dir/Closeness2.cpp.o.requires:

.PHONY : CMakeFiles/Closeness2.dir/Closeness2.cpp.o.requires

CMakeFiles/Closeness2.dir/Closeness2.cpp.o.provides: CMakeFiles/Closeness2.dir/Closeness2.cpp.o.requires
	$(MAKE) -f CMakeFiles/Closeness2.dir/build.make CMakeFiles/Closeness2.dir/Closeness2.cpp.o.provides.build
.PHONY : CMakeFiles/Closeness2.dir/Closeness2.cpp.o.provides

CMakeFiles/Closeness2.dir/Closeness2.cpp.o.provides.build: CMakeFiles/Closeness2.dir/Closeness2.cpp.o


# Object files for target Closeness2
Closeness2_OBJECTS = \
"CMakeFiles/Closeness2.dir/Closeness2.cpp.o"

# External object files for target Closeness2
Closeness2_EXTERNAL_OBJECTS =

Closeness2: CMakeFiles/Closeness2.dir/Closeness2.cpp.o
Closeness2: CMakeFiles/Closeness2.dir/build.make
Closeness2: /usr/lib/x86_64-linux-gnu/libboost_graph.so
Closeness2: CMakeFiles/Closeness2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ivan/dev/eclipse/workspace/BoostGraph/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Closeness2"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Closeness2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Closeness2.dir/build: Closeness2

.PHONY : CMakeFiles/Closeness2.dir/build

CMakeFiles/Closeness2.dir/requires: CMakeFiles/Closeness2.dir/Closeness2.cpp.o.requires

.PHONY : CMakeFiles/Closeness2.dir/requires

CMakeFiles/Closeness2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Closeness2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Closeness2.dir/clean

CMakeFiles/Closeness2.dir/depend:
	cd /home/ivan/dev/eclipse/workspace/BoostGraph/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ivan/dev/eclipse/workspace/BoostGraph /home/ivan/dev/eclipse/workspace/BoostGraph /home/ivan/dev/eclipse/workspace/BoostGraph/build /home/ivan/dev/eclipse/workspace/BoostGraph/build /home/ivan/dev/eclipse/workspace/BoostGraph/build/CMakeFiles/Closeness2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Closeness2.dir/depend

