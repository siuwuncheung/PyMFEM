# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _auxiliary
else:
    import _auxiliary

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _auxiliary.SWIG_PyInstanceMethod_New
_swig_new_static_method = _auxiliary.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.vector
import mfem._ser.coefficient
import mfem._ser.globals
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.symmat
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.fe_base
import mfem._ser.fe_fixed_order
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.fe_h1
import mfem._ser.fe_nd
import mfem._ser.fe_rt
import mfem._ser.fe_l2
import mfem._ser.fe_nurbs
import mfem._ser.fe_pos
import mfem._ser.fe_ser
import mfem._ser.mesh
import mfem._ser.sort_pairs
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.doftrans
import mfem._ser.handle
import mfem._ser.restriction
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.std_vectors
class EulerSystem(mfem._ser.operators.TimeDependentOperator):
    r"""Proxy of C++ EulerSystem class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, vfes_, A_, Aflux_, specific_heat_ratio_, num_equation_):
        r"""__init__(EulerSystem self, FiniteElementSpace vfes_, Operator A_, SparseMatrix Aflux_, double specific_heat_ratio_, int num_equation_) -> EulerSystem"""
        _auxiliary.EulerSystem_swiginit(self, _auxiliary.new_EulerSystem(vfes_, A_, Aflux_, specific_heat_ratio_, num_equation_))

    def GetMaxWavespeed(self, x):
        r"""GetMaxWavespeed(EulerSystem self, Vector x) -> float"""
        return _auxiliary.EulerSystem_GetMaxWavespeed(self, x)
    GetMaxWavespeed = _swig_new_instance_method(_auxiliary.EulerSystem_GetMaxWavespeed)

    def Mult(self, x, y):
        r"""Mult(EulerSystem self, Vector x, Vector y)"""
        return _auxiliary.EulerSystem_Mult(self, x, y)
    Mult = _swig_new_instance_method(_auxiliary.EulerSystem_Mult)
    __swig_destroy__ = _auxiliary.delete_EulerSystem

# Register EulerSystem in _auxiliary:
_auxiliary.EulerSystem_swigregister(EulerSystem)

class RiemannSolver(object):
    r"""Proxy of C++ RiemannSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    flux1 = property(_auxiliary.RiemannSolver_flux1_get, _auxiliary.RiemannSolver_flux1_set, doc=r"""flux1 : mfem::Vector""")
    flux2 = property(_auxiliary.RiemannSolver_flux2_get, _auxiliary.RiemannSolver_flux2_set, doc=r"""flux2 : mfem::Vector""")
    num_equation = property(_auxiliary.RiemannSolver_num_equation_get, _auxiliary.RiemannSolver_num_equation_set, doc=r"""num_equation : int""")
    specific_heat_ratio = property(_auxiliary.RiemannSolver_specific_heat_ratio_get, _auxiliary.RiemannSolver_specific_heat_ratio_set, doc=r"""specific_heat_ratio : double""")

    def __init__(self, specific_heat_ratio_, num_equation_):
        r"""__init__(RiemannSolver self, double specific_heat_ratio_, int num_equation_) -> RiemannSolver"""
        _auxiliary.RiemannSolver_swiginit(self, _auxiliary.new_RiemannSolver(specific_heat_ratio_, num_equation_))

    def Eval(self, state1, state2, nor, flux):
        r"""Eval(RiemannSolver self, Vector state1, Vector state2, Vector nor, Vector flux) -> double"""
        return _auxiliary.RiemannSolver_Eval(self, state1, state2, nor, flux)
    Eval = _swig_new_instance_method(_auxiliary.RiemannSolver_Eval)
    __swig_destroy__ = _auxiliary.delete_RiemannSolver

# Register RiemannSolver in _auxiliary:
_auxiliary.RiemannSolver_swigregister(RiemannSolver)

class FaceIntegrator(mfem._ser.nonlininteg.NonlinearFormIntegrator):
    r"""Proxy of C++ FaceIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    rsolver = property(_auxiliary.FaceIntegrator_rsolver_get, _auxiliary.FaceIntegrator_rsolver_set, doc=r"""rsolver : RiemannSolver""")
    num_equation = property(_auxiliary.FaceIntegrator_num_equation_get, _auxiliary.FaceIntegrator_num_equation_set, doc=r"""num_equation : int""")
    shape1 = property(_auxiliary.FaceIntegrator_shape1_get, _auxiliary.FaceIntegrator_shape1_set, doc=r"""shape1 : mfem::Vector""")
    shape2 = property(_auxiliary.FaceIntegrator_shape2_get, _auxiliary.FaceIntegrator_shape2_set, doc=r"""shape2 : mfem::Vector""")
    funval1 = property(_auxiliary.FaceIntegrator_funval1_get, _auxiliary.FaceIntegrator_funval1_set, doc=r"""funval1 : mfem::Vector""")
    funval2 = property(_auxiliary.FaceIntegrator_funval2_get, _auxiliary.FaceIntegrator_funval2_set, doc=r"""funval2 : mfem::Vector""")
    nor = property(_auxiliary.FaceIntegrator_nor_get, _auxiliary.FaceIntegrator_nor_set, doc=r"""nor : mfem::Vector""")
    fluxN = property(_auxiliary.FaceIntegrator_fluxN_get, _auxiliary.FaceIntegrator_fluxN_set, doc=r"""fluxN : mfem::Vector""")

    def __init__(self, rsolver_, dim, num_equation_):
        r"""__init__(FaceIntegrator self, RiemannSolver rsolver_, int const dim, double num_equation_) -> FaceIntegrator"""
        _auxiliary.FaceIntegrator_swiginit(self, _auxiliary.new_FaceIntegrator(rsolver_, dim, num_equation_))

    def AssembleFaceVector(self, el1, el2, Tr, elfun, elvect):
        r"""AssembleFaceVector(FaceIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elfun, Vector elvect)"""
        return _auxiliary.FaceIntegrator_AssembleFaceVector(self, el1, el2, Tr, elfun, elvect)
    AssembleFaceVector = _swig_new_instance_method(_auxiliary.FaceIntegrator_AssembleFaceVector)
    __swig_destroy__ = _auxiliary.delete_FaceIntegrator

# Register FaceIntegrator in _auxiliary:
_auxiliary.FaceIntegrator_swigregister(FaceIntegrator)

class NeumannBCFaceIntegrator(mfem._ser.nonlininteg.NonlinearFormIntegrator):
    r"""Proxy of C++ NeumannBCFaceIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    rsolver = property(_auxiliary.NeumannBCFaceIntegrator_rsolver_get, _auxiliary.NeumannBCFaceIntegrator_rsolver_set, doc=r"""rsolver : RiemannSolver""")
    num_equation = property(_auxiliary.NeumannBCFaceIntegrator_num_equation_get, _auxiliary.NeumannBCFaceIntegrator_num_equation_set, doc=r"""num_equation : int""")
    shape = property(_auxiliary.NeumannBCFaceIntegrator_shape_get, _auxiliary.NeumannBCFaceIntegrator_shape_set, doc=r"""shape : mfem::Vector""")
    funval = property(_auxiliary.NeumannBCFaceIntegrator_funval_get, _auxiliary.NeumannBCFaceIntegrator_funval_set, doc=r"""funval : mfem::Vector""")
    nor = property(_auxiliary.NeumannBCFaceIntegrator_nor_get, _auxiliary.NeumannBCFaceIntegrator_nor_set, doc=r"""nor : mfem::Vector""")
    fluxN = property(_auxiliary.NeumannBCFaceIntegrator_fluxN_get, _auxiliary.NeumannBCFaceIntegrator_fluxN_set, doc=r"""fluxN : mfem::Vector""")

    def __init__(self, rsolver_, dim, num_equation_):
        r"""__init__(NeumannBCFaceIntegrator self, RiemannSolver rsolver_, int const dim, double num_equation_) -> NeumannBCFaceIntegrator"""
        _auxiliary.NeumannBCFaceIntegrator_swiginit(self, _auxiliary.new_NeumannBCFaceIntegrator(rsolver_, dim, num_equation_))

    def AssembleFaceVector(self, el1, el2, Tr, elfun, elvect):
        r"""AssembleFaceVector(NeumannBCFaceIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elfun, Vector elvect)"""
        return _auxiliary.NeumannBCFaceIntegrator_AssembleFaceVector(self, el1, el2, Tr, elfun, elvect)
    AssembleFaceVector = _swig_new_instance_method(_auxiliary.NeumannBCFaceIntegrator_AssembleFaceVector)
    __swig_destroy__ = _auxiliary.delete_NeumannBCFaceIntegrator

# Register NeumannBCFaceIntegrator in _auxiliary:
_auxiliary.NeumannBCFaceIntegrator_swigregister(NeumannBCFaceIntegrator)


def StateIsPhysical(state, dim):
    r"""StateIsPhysical(Vector state, int const dim) -> bool"""
    return _auxiliary.StateIsPhysical(state, dim)
StateIsPhysical = _auxiliary.StateIsPhysical

def ComputePressure(state, num_equation, specific_heat_ratio):
    r"""ComputePressure(Vector state, int num_equation, double specific_heat_ratio) -> double"""
    return _auxiliary.ComputePressure(state, num_equation, specific_heat_ratio)
ComputePressure = _auxiliary.ComputePressure

def ComputeFlux(state, dim, flux, specific_heat_ratio, num_equation):
    r"""ComputeFlux(Vector state, int dim, DenseMatrix flux, double specific_heat_ratio, int num_equation)"""
    return _auxiliary.ComputeFlux(state, dim, flux, specific_heat_ratio, num_equation)
ComputeFlux = _auxiliary.ComputeFlux

def ComputeFluxDotN(state, nor, fluxN, specific_heat_ratio, num_equation):
    r"""ComputeFluxDotN(Vector state, Vector nor, Vector fluxN, double specific_heat_ratio, int num_equation)"""
    return _auxiliary.ComputeFluxDotN(state, nor, fluxN, specific_heat_ratio, num_equation)
ComputeFluxDotN = _auxiliary.ComputeFluxDotN

def ComputeMaxCharSpeed(state, dim, specific_heat_ratio, num_equation):
    r"""ComputeMaxCharSpeed(Vector state, int const dim, double specific_heat_ratio, int num_equation) -> double"""
    return _auxiliary.ComputeMaxCharSpeed(state, dim, specific_heat_ratio, num_equation)
ComputeMaxCharSpeed = _auxiliary.ComputeMaxCharSpeed


