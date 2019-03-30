cmake_minimum_required(VERSION 3.8)
project(delegate)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(delegate INTERFACE)
target_sources(delegate INTERFACE
            ${CMAKE_CURRENT_SOURCE_DIR}/include/delegate/Delegate.h
            ${CMAKE_CURRENT_SOURCE_DIR}/include/delegate/DelegateBase.h
            ${CMAKE_CURRENT_SOURCE_DIR}/include/delegate/MultiCastDelegate.h)
target_include_directories(delegate INTERFACE include/)
target_compile_features(delegate INTERFACE cxx_std_14)

