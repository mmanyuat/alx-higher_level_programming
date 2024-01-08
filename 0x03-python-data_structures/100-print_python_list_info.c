#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_size(p);
	int j;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] size of the python list = %li\n", size);
	printf("[*] Allocated = %li", obj->allocated);
	for (j = 0; j < size; j++)
		printf("Element %i: %s\n", i, py_TYPE(obj->ob_item[j])->tp_name);

}
