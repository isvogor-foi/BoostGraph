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
include CMakeFiles/Closeness.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Closeness.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Closeness.dir/flags.make

CMakeFiles/Closeness.dir/Closeness.cpp.o: CMakeFiles/Closeness.dir/flags.make
CMakeFiles/Closeness.dir/Closeness.cpp.o: ../Closeness.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ivan/dev/eclipse/workspace/BoostGraph/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Closeness.dir/Closeness.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Closeness.dir/Closeness.cpp.o -c /home/ivan/dev/eclipse/workspace/BoostGraph/Closeness.cpp

CMakeFiles/Closeness.dir/Closeness.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Closeness.dir/Closeness.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ivan/dev/eclipse/workspace/BoostGraph/Closeness.cpp > CMakeFiles/Closeness.dir/Closeness.cpp.i

CMakeFiles/Closeness.dir/Closeness.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Closeness.dir/Closeness.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ivan/dev/eclipse/workspace/BoostGraph/Closeness.cpp -o CMakeFiles/Closeness.dir/Closeness.cpp.s

CMakeFiles/Closeness.dir/Closeness.cpp.o.requires:

.PHONY : CMakeFiles/Closeness.dir/Closeness.cpp.o.requires

CMakeFiles/Closeness.dir/Closeness.cpp.o.provides: CMakeFiles/Closeness.dir/Closeness.cpp.o.requires
	$(MAKE) -f CMakeFiles/Closeness.dir/build.make CMakeFiles/Closeness.dir/Closeness.cpp.o.provides.build
.PHONY : CMakeFiles/Closeness.dir/Closeness.cpp.o.provides

CMakeFiles/Closeness.dir/Closeness.cpp.o.provides.build: CMakeFiles/Closeness.dir/Closeness.cpp.o


# Object files for target Closeness
Closeness_OBJECTS = \
"CMakeFiles/Closeness.dir/Closeness.cpp.o"

# External object files for target Closeness
Closeness_EXTERNAL_OBJECTS =

Closeness: CMakeFiles/Closeness.dir/Closeness.cpp.o
Closeness: CMakeFiles/Closeness.dir/build.make
Closeness: /usr/lib/x86_64-linux-gnu/libboost_graph.so
Closeness: CMakeFiles/Closeness.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ivan/dev/eclipse/workspace/BoostGraph/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Closeness"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Closeness.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Closeness.dir/build: Closeness

.PHONY : CMakeFiles/Closeness.dir/build

CMakeFiles/Closeness.dir/requires: CMakeFiles/Closeness.dir/Closeness.cpp.o.requires

.PHONY : CMakeFiles/Closeness.dir/requires

CMakeFiles/Closeness.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Closeness.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Closeness.dir/clean

CMakeFiles/Closeness.dir/depend:
	cd /home/ivan/dev/eclipse/workspace/BoostGraph/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ivan/dev/eclipse/workspace/BoostGraph /home/ivan/dev/eclipse/workspace/BoostGraph /home/ivan/dev/eclipse/workspace/BoostGraph/build /home/ivan/dev/eclipse/workspace/BoostGraph/build /home/ivan/dev/eclipse/workspace/BoostGraph/build/CMakeFiles/Closeness.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Closeness.dir/depend
