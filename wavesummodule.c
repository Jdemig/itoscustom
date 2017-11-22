#include <Python.h>

static PyObject * example(PyObject *self)
{
  // do something
  return Py_BuildValue("i", result);
}

static PyMethodDef ExampleMethods[] = {
  { "hello", hello_wrapper, METH_VARARGS, "Say hello" },
  { NULL, NULL, 0, NULL }
};

DL_EXPORT(void) initexample(void)
{
  Py_InitModule("hello", ExampleMethods);
}

