cmake_minimum_required(VERSION 3.10)
project(GFlagParser)

# Set C++ Standard
set(CMAKE_CXX_STANDARD 17)

# Find gflags installed by Homebrew
find_package(gflags REQUIRED)
find_package(glog REQUIRED)

# Include your headers
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)

# Add executable
add_executable(gflag_parser
    src/main.cpp 
    src/foo.cpp 
    src/bar.cpp 
    src/main_flags.cpp
    src/foo_flags.cpp 
    src/bar_flags.cpp)

# Link gflags
target_link_libraries(gflag_parser
    gflags
    glog::glog)
