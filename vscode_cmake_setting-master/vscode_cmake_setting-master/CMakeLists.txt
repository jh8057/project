cmake_minimum_required(VERSION 3.0.0)
project(hello2 VERSION 0.1.0)

include(CTest)
enable_testing()

INCLUDE_DIRECTORIES("${CMAKE_SOURCE_DIR}/a" "${CMAKE_SOURCE_DIR}/d")

file(GLOB_RECURSE C_FILES "${CMAKE_SOURCE_DIR}/a/*.c*" "${CMAKE_SOURCE_DIR}/d/*.c*")

ADD_DEFINITIONS(-std=c++17)

add_executable(hello2 main.cpp ${C_FILES})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
