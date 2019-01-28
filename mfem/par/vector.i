
/*

   vector.i

*/
%module vector
%feature("autodoc", "1");
%{
#include "linalg/vector.hpp"
#include <sstream>
#include <fstream>
#include <limits>
#include <cmath>
#include <cstring>
#include <ctime>
#include "numpy/arrayobject.h"
#include "iostream_typemap.hpp"           
%}

// initialization required to return numpy array from SWIG
%init %{
import_array();
%}

%include "exception.i"
%import "array.i"
%import "ostream_typemap.i"
%import "../common/ignore_common_functions.i"
%import "../common/numpy_int_typemap.i"
%import "../common/typemap_macros.i"
%import "../common/exception.i"

ARRAY_TO_DOUBLEARRAY_IN(double *_data)

%pythonprepend mfem::Vector::Vector %{
from numpy import ndarray, ascontiguousarray
keep_link = False
own_data = False  
if len(args) == 1:
    if isinstance(args[0], list): 
        args = (args[0], len(args[0]))
        own_data = True	  
    elif isinstance(args[0], ndarray):
        if args[0].dtype != 'float64':
            raise ValueError('Must be float64 array ' + args[0].dtype + ' is given')  
        else:
  	    args = (ascontiguousarray(args[0]), args[0].shape[0])
             # in this case, args[0] need to be maintained
	     # in this object.
	    keep_link = True
%}

%pythonappend mfem::Vector::Vector %{
if keep_link:
   self._link_to_data = args[0]
if own_data:
   self.MakeDataOwner()
%}

%feature("shadow") mfem::Vector::operator+= %{
def __iadd__(self, v):
    ret = _vector.Vector___iadd__(self, v)
    #ret.thisown = self.thisown
    ret.thisown = 0                  
    return self
%}
%feature("shadow") mfem::Vector::operator-= %{
def __isub__(self, v):
    ret = _vector.Vector___isub__(self, v)
    #ret.thisown = self.thisown
    ret.thisown = 0            
    return self
%} 
%feature("shadow") mfem::Vector::operator*= %{
def __imul__(self, v):
    ret = _vector.Vector___imul__(self, v)
    #ret.thisown = self.thisown
    ret.thisown = 0            
    return self
%} 
%feature("shadow") mfem::Vector::operator/= %{
def __itruediv__(self, v):
    ret = _vector.Vector___itruediv__(self, v)
    #ret.thisown = self.thisown
    ret.thisown = 0      
    return self
%}
//rename(Assign) mfem::Vector::operator=;
%pythonprepend mfem::Vector::Assign %{
from numpy import ndarray, ascontiguousarray
if len(args) == 1 and isinstance(args[0], ndarray):
        if args[0].dtype != 'float64':
            raise ValueError('Must be float64 array ' + args[0].dtype + ' is given')    
        elif args[0].ndim != 1:
            raise ValueError('Ndim must be one') 
        elif args[0].shape[0] != _vector.Vector_Size(self):
            raise ValueError('Length does not match')
        else:
  	    args = (ascontiguousarray(args[0]),)
%}
%pythonappend mfem::Vector::Assign %{
    return self
%}

%ignore mfem::add;
%ignore mfem::subtract;
%ignore mfem::Vector::operator =;
%ignore mfem::Vector::operator double *;
%ignore mfem::Vector::operator const double *;

%inline %{
void add_vector(const mfem::Vector &v1, const mfem::Vector &v2, mfem::Vector &v){
   add(v1, v2, v);
}
   /// Do v = v1 + alpha * v2.
void add_vector(const mfem::Vector &v1, double alpha, const mfem::Vector &v2, mfem::Vector &v){
   add(v1, alpha, v2, v);
}
   /// z = a * (x + y)
void add_vector(const double a, const mfem::Vector &x, const mfem::Vector &y, mfem::Vector &z){
   add(a, x, y, z);
}
  /// z = a * x + b * y
void add_vector (const double a, const mfem::Vector &x,
		   const double b, const mfem::Vector &y, mfem::Vector &z){
   add(a, x, b, y, z);
}
   /// Do v = v1 - v2.
void subtract_vector(const mfem::Vector &v1, const mfem::Vector &v2, mfem::Vector &v){
   subtract(v1, v2, v);
}
   /// z = a * (x - y)
void subtract_vector(const double a, const mfem::Vector &x,
		       const mfem::Vector &y, mfem::Vector &z){
   subtract(a, x, y, z);
}
%}


%include "linalg/vector.hpp"

%extend mfem::Vector {
  /* define Assine as a replacement of = operator */
  Vector(const mfem::Vector &v, int offset, int size){
      mfem::Vector *vec;
      vec = new mfem::Vector(v.GetData() +  offset, size);     
      return vec;
  }
  void Assign(const double v) {
    (* self) = v;
  }
  void Assign(PyObject* param) {
    /* note that these error does not raise error in python
       type check is actually done in wrapper layer */
    if (!PyArray_Check(param)){
       PyErr_SetString(PyExc_ValueError, "Input data must be ndarray");
       return;
    }
    int typ = PyArray_TYPE(param);
    if (typ != NPY_DOUBLE){
        PyErr_SetString(PyExc_ValueError, "Input data must be float64");
	return;
    }
    int ndim = PyArray_NDIM(param);
    if (ndim != 1){
      PyErr_SetString(PyExc_ValueError, "Input data NDIM must be one");
      return ;
    }
    npy_intp *shape = PyArray_DIMS(param);    
    int len = self->Size();
    if (shape[0] != len){    
      PyErr_SetString(PyExc_ValueError, "input data length does not match");
      return ;
    }    
    (* self) = (double *) PyArray_DATA(param);
  }
  
  void Print(const char *file){
        std::ofstream ofile(file);
        if (!ofile)
        {
	  std::cerr << "\nCan not produce output file: " << file << '\n' << std::endl;
   	  return;
        }
	self -> Print(ofile);
        ofile.close();
  }

  void __setitem__(int i, const double v) {
    int len = self->Size();        
    if (i >= 0){    
       (* self)(i) = v;
    } else {
      (* self)(len+i) = v;
    }
  }
  PyObject* __getitem__(PyObject* param) {
    int len = self->Size();    
    if (PySlice_Check(param)) {
        long start = 0, stop = 0, step = 0, slicelength = 0;
        int check;
	check = PySlice_GetIndicesEx((PySliceObject*)param, len, &start, &stop, &step,
				     &slicelength);
	if (check == -1) {
            PyErr_SetString(PyExc_ValueError, "Slicing mfem::Vector failed.");
            return NULL; 
	}
	if (step == 1) {
            mfem::Vector *vec;
            vec = new mfem::Vector(self->GetData() +  start, slicelength);
            return SWIG_NewPointerObj(SWIG_as_voidptr(vec), $descriptor(mfem::Vector *), 1);  
	} else {
            mfem::Vector *vec;
            vec = new mfem::Vector(slicelength);
            double* data = vec -> GetData();
	    int idx = start;
            for (int i = 0; i < slicelength; i++)
            {
	      data[i] = (* self)(idx);
	      idx += step;
            }
            return SWIG_NewPointerObj(SWIG_as_voidptr(vec), $descriptor(mfem::Vector *), 1);
	}
    } else {
        PyErr_Clear();
        long idx = PyInt_AsLong(param);
        if (PyErr_Occurred()) {
           PyErr_SetString(PyExc_ValueError, "Argument must be either int or slice");
            return NULL; 	
        }
        if (idx >= 0){
           return PyFloat_FromDouble((* self)(idx));
        } else {
          return PyFloat_FromDouble((* self)(len+idx));
	}
    }
  }
  PyObject* GetDataArray(void) const{
     double * A = self->GetData();    
     int L = self->Size();
     npy_intp dims[] = {L};
     return  PyArray_SimpleNewFromData(1, dims, NPY_DOUBLE, A);
  }
};

%pythoncode %{
   Vector.__idiv__ = Vector.__itruediv__
%}


