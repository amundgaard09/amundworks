cmake_minimum_required(VERSION 3.20)
project(OpenGLProject)

set(CMAKE_CXX_STANDARD 20)

find_package(OpenGL REQUIRED)
find_package(glfw3 CONFIG REQUIRED)
find_package(glad CONFIG REQUIRED)
find_package(glm CONFIG REQUIRED)

add_executable(app src/main.cpp)

target_link_libraries(app
    PRIVATE
    OpenGL::GL
    glfw
    glad::glad
    glm::glm
)