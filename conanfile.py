from conans import ConanFile, CMake, tools

class Delegate(ConanFile):
    name = "delegate"
    version = "1.0.0"
    url = "https://www.codeproject.com/Articles/1170503/The-Impossibly-Fast-Cplusplus-Delegates-Fixed"
    license = "MIT"
    description = "The Impossibly Fast C++ Delegates"
    generators = "cmake"
    exports_sources = "include/**", "CMakeLists.txt"

    def package(self):
        self.copy("*.h")
        self.copy("CMakeLists.txt")
        self.copy("LICENSE.txt")

