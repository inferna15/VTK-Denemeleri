cmake_minimum_required(VERSION 3.10)
project(VTKPickerExample)

# VTK'yi bul
find_package(VTK REQUIRED)

# VTK başlık dosyalarını dahil et
include_directories(${VTK_INCLUDE_DIRS})

# Kaynak dosyasını belirt
add_executable(VTKPickerExample main.cpp)

# VTK kütüphanelerini bağla
target_link_libraries(VTKPickerExample ${VTK_LIBRARIES})

# C++17 kullan
set(CMAKE_CXX_STANDARD 17)

