# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

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
CMAKE_SOURCE_DIR = /root/Cracking/ch12/ch12-1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /root/Cracking/ch12/ch12-1

# Include any dependencies generated for this target.
include CMakeFiles/12-1.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/12-1.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/12-1.dir/flags.make

CMakeFiles/12-1.dir/12-1.cpp.o: CMakeFiles/12-1.dir/flags.make
CMakeFiles/12-1.dir/12-1.cpp.o: 12-1.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/Cracking/ch12/ch12-1/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/12-1.dir/12-1.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/12-1.dir/12-1.cpp.o -c /root/Cracking/ch12/ch12-1/12-1.cpp

CMakeFiles/12-1.dir/12-1.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/12-1.dir/12-1.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/Cracking/ch12/ch12-1/12-1.cpp > CMakeFiles/12-1.dir/12-1.cpp.i

CMakeFiles/12-1.dir/12-1.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/12-1.dir/12-1.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/Cracking/ch12/ch12-1/12-1.cpp -o CMakeFiles/12-1.dir/12-1.cpp.s

CMakeFiles/12-1.dir/12-1.cpp.o.requires:

.PHONY : CMakeFiles/12-1.dir/12-1.cpp.o.requires

CMakeFiles/12-1.dir/12-1.cpp.o.provides: CMakeFiles/12-1.dir/12-1.cpp.o.requires
	$(MAKE) -f CMakeFiles/12-1.dir/build.make CMakeFiles/12-1.dir/12-1.cpp.o.provides.build
.PHONY : CMakeFiles/12-1.dir/12-1.cpp.o.provides

CMakeFiles/12-1.dir/12-1.cpp.o.provides.build: CMakeFiles/12-1.dir/12-1.cpp.o


# Object files for target 12-1
12__1_OBJECTS = \
"CMakeFiles/12-1.dir/12-1.cpp.o"

# External object files for target 12-1
12__1_EXTERNAL_OBJECTS =

12-1: CMakeFiles/12-1.dir/12-1.cpp.o
12-1: CMakeFiles/12-1.dir/build.make
12-1: CMakeFiles/12-1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/root/Cracking/ch12/ch12-1/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable 12-1"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/12-1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/12-1.dir/build: 12-1

.PHONY : CMakeFiles/12-1.dir/build

CMakeFiles/12-1.dir/requires: CMakeFiles/12-1.dir/12-1.cpp.o.requires

.PHONY : CMakeFiles/12-1.dir/requires

CMakeFiles/12-1.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/12-1.dir/cmake_clean.cmake
.PHONY : CMakeFiles/12-1.dir/clean

CMakeFiles/12-1.dir/depend:
	cd /root/Cracking/ch12/ch12-1 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/Cracking/ch12/ch12-1 /root/Cracking/ch12/ch12-1 /root/Cracking/ch12/ch12-1 /root/Cracking/ch12/ch12-1 /root/Cracking/ch12/ch12-1/CMakeFiles/12-1.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/12-1.dir/depend

