#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* printErr(PyObject* err, const char* msg)
{
    PyErr_SetString(err, msg);
    return NULL;
}

typedef struct
{
    Py_ssize_t rows;
    Py_ssize_t columns;
} MatrixSizes;

static MatrixSizes getMatrixSizes(PyObject* matrix)
{
    MatrixSizes result = { PyList_Size(matrix), PyList_Size(PyList_GetItem(matrix, 0)) };
    return result;
}

static PyObject* ematrix(PyObject* matrix, Py_ssize_t l)
{
    PyObject* result = PyList_New(l);
    for (Py_ssize_t i = 0; i < l; i++) {
        PyObject* row = PyList_New(l);
        for (Py_ssize_t j = 0; j < l; j++) {
            if (i == j) {
                PyList_SetItem(row, j, PyFloat_FromDouble(1.0));
            } else {
                PyList_SetItem(row, j, PyFloat_FromDouble(0.0));
            }
        }
        PyList_SetItem(result, i, row);
    }
    return result;
}

static PyObject* matrix_multiply(PyObject* matrix1, PyObject* matrix2, Py_ssize_t l) 
{
    PyObject* result = PyList_New(l);
    for (Py_ssize_t i = 0; i < l; i++) {
        PyObject* row = PyList_New(l);
        for (Py_ssize_t j = 0; j < l; j++) {
            double sum = 0.0;
            for (Py_ssize_t k = 0; k < l; k++) {
                double a = PyFloat_AsDouble(PyList_GetItem(PyList_GetItem(matrix1, i), k));
                double b = PyFloat_AsDouble(PyList_GetItem(PyList_GetItem(matrix2, k), j));
                sum += a * b;
            }
            PyList_SetItem(row, j, PyFloat_FromDouble(sum));
        }
        PyList_SetItem(result, i, row);
    }

    return result;
}

static PyObject* foreign_matrix_power(PyObject* self, PyObject* args) 
{
    PyObject* matrix;
    long power;

    if (!PyArg_ParseTuple(args, "Ol", &matrix, &power)) {
        return NULL;
    }

    if (!PyList_Check(matrix)) return printErr(PyExc_TypeError, "Wrong arguments");

    if (power < 0) return printErr(PyExc_ValueError, "Wrong value");

    MatrixSizes m = getMatrixSizes(matrix);
    if(m.rows != m.columns) return printErr(PyExc_TypeError, "Wrong arguments");

    if (!power) return ematrix(matrix, m.rows);

    PyObject* result = matrix;
    for (long i = 1; i < power; i++) {
        result = matrix_multiply(result, matrix, m.rows);
        if(!result) return NULL;
    }
    return result;
}

static PyMethodDef MatrixMethods[] = 
{
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS, "Matrix operations"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef matrixmodule = 
{
    PyModuleDef_HEAD_INIT,
    "matrixpower",
    NULL,
    -1,
    MatrixMethods
};

PyMODINIT_FUNC PyInit_matrixpower(void) { return PyModule_Create(&matrixmodule); }