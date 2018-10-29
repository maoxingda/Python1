// pyebd1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <boost/python.hpp>

using namespace boost::python;

int _tmain(int argc, _TCHAR* argv[])
{
	Py_Initialize();
	//object main = import("__main__");

	//object global(main.attr("__dict__"));

	//object result = exec(
	//	"def greet():\n"
	//	"	return 'Hello from Python!\n",
	//	global, global);

	//object greet = global["greet"];

	//std::string msg = extract<std::string>(greet());
	//std::cout << msg << std::endl;

	object sys = import("sys");

	std::string ver = extract<std::string>(sys.attr("executable"));
	std::cout << ver << std::endl;

	getchar();
	return 0;
}

