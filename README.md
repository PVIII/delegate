# The Impossibly Fast C++ Delegates

[![Build Status](https://travis-ci.com/PVIII/delegate.svg?branch=master)](https://travis-ci.com/PVIII/delegate)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPVIII%2Fdelegate.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FPVIII%2Fdelegate?ref=badge_shield)

This repository packages "The Impossibly Fast C++ Delegates, Fixed" by 
[Sergey Alexandrovich Kryukov](https://www.codeproject.com/script/Membership/View.aspx?mid=2291164) as described on [Code Project](https://www.codeproject.com/Articles/1170503/The-Impossibly-Fast-Cplusplus-Delegates-Fixed).

It is the C++11 version of ["The Impossibly Fast C++ Delegates"](https://www.codeproject.com/articles/11015/the-impossibly-fast-c-delegates) by [Sergey Ryazanov](https://www.codeproject.com/script/Membership/View.aspx?mid=2013375).

This in turn is based on ["Member Function Pointers and the Fastest Possible C++ Delegates by Don Clugston"](https://www.codeproject.com/Articles/7150/Member-Function-Pointers-and-the-Fastest-Possible) by [Don Clugston](https://www.codeproject.com/Members/Don-Clugston).

## Getting Started

This is a header only library. It should compile with any C++14-capable compiler.

### Installing

You can just download or clone the library and set your include directory to `include`.

If you use [Conan](https://conan.io/) you can add the Conan remote
```
conan remote add <REMOTE> https://api.bintray.com/conan/pviii/conan
```
and reference the package `delegate/x.x.x@pviii/stable` as a dependency.

## Built With

* [CMake](https://cmake.org/) - Build System (Generator)
* [Conan](https://conan.io/) - Dependency Management
* [Bintray](https://bintray.com) - Package Hosting

## Versioning

This package is versioned using [SemVer](http://semver.org/).

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.


[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPVIII%2Fdelegate.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FPVIII%2Fdelegate?ref=badge_large)

## Acknowledgements

* Don Clugston
* Sergey Ryazanov
* Sergey Alexandrovich Kryukov