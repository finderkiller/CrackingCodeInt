cmake_minimum_required(VERSION 3.1 FATAL_ERROR)

project(Test)

find_package(PkgConfig)
include(GNUInstallDirs)

# global settings
add_compile_options(-Wall)
include_directories(${PROJECT_SOURCE_DIR}/include)

SET (HELLO_SRCS 12-8.cpp)
ADD_EXECUTABLE (12-8 ${HELLO_SRCS})
