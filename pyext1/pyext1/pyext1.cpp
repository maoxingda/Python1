// pyext1.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include <boost/python.hpp>


#define DEF(identifier) boost::python::def(#identifier, identifier)


char const* hello_world()
{
	return "hello world";
}

BOOST_PYTHON_MODULE(hw)
{
	DEF(hello_world);
}