cmake_minimum_required(VERSION 3.8)
project(CustomContextItemExample)

find_package(VTK REQUIRED COMPONENTS
    CommonCore
    RenderingCore
    RenderingContext2D
    RenderingContextOpenGL2
    RenderingOpenGL2
    InteractionStyle
)

include(${VTK_USE_FILE})

add_executable(CustomContextItemExample main.cpp)
target_link_libraries(CustomContextItemExample ${VTK_LIBRARIES})
