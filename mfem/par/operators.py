# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_operators')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_operators')
    _operators = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_operators', [dirname(__file__)])
        except ImportError:
            import _operators
            return _operators
        try:
            _mod = imp.load_module('_operators', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _operators = swig_import_helper()
    del swig_import_helper
else:
    import _operators
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


import vector
import array
import ostream_typemap
class Operator(_object):
    """Proxy of C++ mfem::Operator class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Operator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Operator, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::Operator self, int s=0) -> Operator
        __init__(mfem::Operator self) -> Operator
        __init__(mfem::Operator self, int h, int w) -> Operator
        """
        if self.__class__ == Operator:
            _self = None
        else:
            _self = self
        this = _operators.new_Operator(_self, *args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Height(self):
        """Height(Operator self) -> int"""
        return _operators.Operator_Height(self)


    def NumRows(self):
        """NumRows(Operator self) -> int"""
        return _operators.Operator_NumRows(self)


    def Width(self):
        """Width(Operator self) -> int"""
        return _operators.Operator_Width(self)


    def NumCols(self):
        """NumCols(Operator self) -> int"""
        return _operators.Operator_NumCols(self)


    def Mult(self, x, y):
        """Mult(Operator self, Vector x, Vector y)"""
        return _operators.Operator_Mult(self, x, y)


    def MultTranspose(self, x, y):
        """MultTranspose(Operator self, Vector x, Vector y)"""
        return _operators.Operator_MultTranspose(self, x, y)


    def GetGradient(self, x):
        """GetGradient(Operator self, Vector x) -> Operator"""
        return _operators.Operator_GetGradient(self, x)


    def GetProlongation(self):
        """GetProlongation(Operator self) -> Operator"""
        return _operators.Operator_GetProlongation(self)


    def GetRestriction(self):
        """GetRestriction(Operator self) -> Operator"""
        return _operators.Operator_GetRestriction(self)


    def FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior=0):
        """
        FormLinearSystem(Operator self, intArray ess_tdof_list, Vector x, Vector b, mfem::Operator *& A, Vector X, Vector B, int copy_interior=0)
        FormLinearSystem(Operator self, intArray ess_tdof_list, Vector x, Vector b, mfem::Operator *& A, Vector X, Vector B)
        """
        return _operators.Operator_FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior)


    def RecoverFEMSolution(self, X, b, x):
        """RecoverFEMSolution(Operator self, Vector X, Vector b, Vector x)"""
        return _operators.Operator_RecoverFEMSolution(self, X, b, x)


    def PrintMatlab(self, out, n=0, m=0):
        """
        PrintMatlab(Operator self, std::ostream & out, int n=0, int m=0)
        PrintMatlab(Operator self, std::ostream & out, int n=0)
        PrintMatlab(Operator self, std::ostream & out)
        """
        return _operators.Operator_PrintMatlab(self, out, n, m)

    __swig_destroy__ = _operators.delete_Operator
    __del__ = lambda self: None
    ANY_TYPE = _operators.Operator_ANY_TYPE
    MFEM_SPARSEMAT = _operators.Operator_MFEM_SPARSEMAT
    Hypre_ParCSR = _operators.Operator_Hypre_ParCSR
    PETSC_MATAIJ = _operators.Operator_PETSC_MATAIJ
    PETSC_MATIS = _operators.Operator_PETSC_MATIS
    PETSC_MATSHELL = _operators.Operator_PETSC_MATSHELL
    PETSC_MATNEST = _operators.Operator_PETSC_MATNEST
    PETSC_MATHYPRE = _operators.Operator_PETSC_MATHYPRE
    PETSC_MATGENERIC = _operators.Operator_PETSC_MATGENERIC

    def GetType(self):
        """GetType(Operator self) -> mfem::Operator::Type"""
        return _operators.Operator_GetType(self)

    def __disown__(self):
        self.this.disown()
        _operators.disown_Operator(self)
        return weakref_proxy(self)
Operator_swigregister = _operators.Operator_swigregister
Operator_swigregister(Operator)

class TimeDependentOperator(Operator):
    """Proxy of C++ mfem::TimeDependentOperator class."""

    __swig_setmethods__ = {}
    for _s in [Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TimeDependentOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TimeDependentOperator, name)
    __repr__ = _swig_repr
    EXPLICIT = _operators.TimeDependentOperator_EXPLICIT
    IMPLICIT = _operators.TimeDependentOperator_IMPLICIT
    HOMOGENEOUS = _operators.TimeDependentOperator_HOMOGENEOUS

    def __init__(self, *args):
        """
        __init__(mfem::TimeDependentOperator self, int n=0, double t_=0.0, mfem::TimeDependentOperator::Type type_) -> TimeDependentOperator
        __init__(mfem::TimeDependentOperator self, int n=0, double t_=0.0) -> TimeDependentOperator
        __init__(mfem::TimeDependentOperator self, int n=0) -> TimeDependentOperator
        __init__(mfem::TimeDependentOperator self) -> TimeDependentOperator
        __init__(mfem::TimeDependentOperator self, int h, int w, double t_=0.0, mfem::TimeDependentOperator::Type type_) -> TimeDependentOperator
        __init__(mfem::TimeDependentOperator self, int h, int w, double t_=0.0) -> TimeDependentOperator
        __init__(mfem::TimeDependentOperator self, int h, int w) -> TimeDependentOperator
        """
        if self.__class__ == TimeDependentOperator:
            _self = None
        else:
            _self = self
        this = _operators.new_TimeDependentOperator(_self, *args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetTime(self):
        """GetTime(TimeDependentOperator self) -> double"""
        return _operators.TimeDependentOperator_GetTime(self)


    def SetTime(self, _t):
        """SetTime(TimeDependentOperator self, double const _t)"""
        return _operators.TimeDependentOperator_SetTime(self, _t)


    def isExplicit(self):
        """isExplicit(TimeDependentOperator self) -> bool"""
        return _operators.TimeDependentOperator_isExplicit(self)


    def isImplicit(self):
        """isImplicit(TimeDependentOperator self) -> bool"""
        return _operators.TimeDependentOperator_isImplicit(self)


    def isHomogeneous(self):
        """isHomogeneous(TimeDependentOperator self) -> bool"""
        return _operators.TimeDependentOperator_isHomogeneous(self)


    def ExplicitMult(self, x, y):
        """ExplicitMult(TimeDependentOperator self, Vector x, Vector y)"""
        return _operators.TimeDependentOperator_ExplicitMult(self, x, y)


    def ImplicitMult(self, x, k, y):
        """ImplicitMult(TimeDependentOperator self, Vector x, Vector k, Vector y)"""
        return _operators.TimeDependentOperator_ImplicitMult(self, x, k, y)


    def Mult(self, x, y):
        """Mult(TimeDependentOperator self, Vector x, Vector y)"""
        return _operators.TimeDependentOperator_Mult(self, x, y)


    def ImplicitSolve(self, dt, x, k):
        """ImplicitSolve(TimeDependentOperator self, double const dt, Vector x, Vector k)"""
        return _operators.TimeDependentOperator_ImplicitSolve(self, dt, x, k)


    def GetImplicitGradient(self, x, k, shift):
        """GetImplicitGradient(TimeDependentOperator self, Vector x, Vector k, double shift) -> Operator"""
        return _operators.TimeDependentOperator_GetImplicitGradient(self, x, k, shift)


    def GetExplicitGradient(self, x):
        """GetExplicitGradient(TimeDependentOperator self, Vector x) -> Operator"""
        return _operators.TimeDependentOperator_GetExplicitGradient(self, x)

    __swig_destroy__ = _operators.delete_TimeDependentOperator
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _operators.disown_TimeDependentOperator(self)
        return weakref_proxy(self)
TimeDependentOperator_swigregister = _operators.TimeDependentOperator_swigregister
TimeDependentOperator_swigregister(TimeDependentOperator)

class Solver(Operator):
    """Proxy of C++ mfem::Solver class."""

    __swig_setmethods__ = {}
    for _s in [Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Solver, name)
    __repr__ = _swig_repr
    __swig_setmethods__["iterative_mode"] = _operators.Solver_iterative_mode_set
    __swig_getmethods__["iterative_mode"] = _operators.Solver_iterative_mode_get
    if _newclass:
        iterative_mode = _swig_property(_operators.Solver_iterative_mode_get, _operators.Solver_iterative_mode_set)

    def __init__(self, *args):
        """
        __init__(mfem::Solver self, int s=0, bool iter_mode=False) -> Solver
        __init__(mfem::Solver self, int s=0) -> Solver
        __init__(mfem::Solver self) -> Solver
        __init__(mfem::Solver self, int h, int w, bool iter_mode=False) -> Solver
        __init__(mfem::Solver self, int h, int w) -> Solver
        """
        if self.__class__ == Solver:
            _self = None
        else:
            _self = self
        this = _operators.new_Solver(_self, *args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetOperator(self, op):
        """SetOperator(Solver self, Operator op)"""
        return _operators.Solver_SetOperator(self, op)

    __swig_destroy__ = _operators.delete_Solver
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _operators.disown_Solver(self)
        return weakref_proxy(self)
Solver_swigregister = _operators.Solver_swigregister
Solver_swigregister(Solver)

class IdentityOperator(Operator):
    """Proxy of C++ mfem::IdentityOperator class."""

    __swig_setmethods__ = {}
    for _s in [Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IdentityOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IdentityOperator, name)
    __repr__ = _swig_repr

    def __init__(self, n):
        """__init__(mfem::IdentityOperator self, int n) -> IdentityOperator"""
        this = _operators.new_IdentityOperator(n)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(IdentityOperator self, Vector x, Vector y)"""
        return _operators.IdentityOperator_Mult(self, x, y)

    __swig_destroy__ = _operators.delete_IdentityOperator
    __del__ = lambda self: None
IdentityOperator_swigregister = _operators.IdentityOperator_swigregister
IdentityOperator_swigregister(IdentityOperator)

class TransposeOperator(Operator):
    """Proxy of C++ mfem::TransposeOperator class."""

    __swig_setmethods__ = {}
    for _s in [Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TransposeOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TransposeOperator, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::TransposeOperator self, Operator a) -> TransposeOperator
        __init__(mfem::TransposeOperator self, Operator a) -> TransposeOperator
        """
        this = _operators.new_TransposeOperator(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(TransposeOperator self, Vector x, Vector y)"""
        return _operators.TransposeOperator_Mult(self, x, y)


    def MultTranspose(self, x, y):
        """MultTranspose(TransposeOperator self, Vector x, Vector y)"""
        return _operators.TransposeOperator_MultTranspose(self, x, y)

    __swig_destroy__ = _operators.delete_TransposeOperator
    __del__ = lambda self: None
TransposeOperator_swigregister = _operators.TransposeOperator_swigregister
TransposeOperator_swigregister(TransposeOperator)

class ProductOperator(Operator):
    """Proxy of C++ mfem::ProductOperator class."""

    __swig_setmethods__ = {}
    for _s in [Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ProductOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ProductOperator, name)
    __repr__ = _swig_repr

    def __init__(self, A, B, ownA, ownB):
        """__init__(mfem::ProductOperator self, Operator A, Operator B, bool ownA, bool ownB) -> ProductOperator"""
        this = _operators.new_ProductOperator(A, B, ownA, ownB)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(ProductOperator self, Vector x, Vector y)"""
        return _operators.ProductOperator_Mult(self, x, y)


    def MultTranspose(self, x, y):
        """MultTranspose(ProductOperator self, Vector x, Vector y)"""
        return _operators.ProductOperator_MultTranspose(self, x, y)

    __swig_destroy__ = _operators.delete_ProductOperator
    __del__ = lambda self: None
ProductOperator_swigregister = _operators.ProductOperator_swigregister
ProductOperator_swigregister(ProductOperator)

class RAPOperator(Operator):
    """Proxy of C++ mfem::RAPOperator class."""

    __swig_setmethods__ = {}
    for _s in [Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RAPOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RAPOperator, name)
    __repr__ = _swig_repr

    def __init__(self, Rt_, A_, P_):
        """__init__(mfem::RAPOperator self, Operator Rt_, Operator A_, Operator P_) -> RAPOperator"""
        this = _operators.new_RAPOperator(Rt_, A_, P_)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(RAPOperator self, Vector x, Vector y)"""
        return _operators.RAPOperator_Mult(self, x, y)


    def MultTranspose(self, x, y):
        """MultTranspose(RAPOperator self, Vector x, Vector y)"""
        return _operators.RAPOperator_MultTranspose(self, x, y)

    __swig_destroy__ = _operators.delete_RAPOperator
    __del__ = lambda self: None
RAPOperator_swigregister = _operators.RAPOperator_swigregister
RAPOperator_swigregister(RAPOperator)

class TripleProductOperator(Operator):
    """Proxy of C++ mfem::TripleProductOperator class."""

    __swig_setmethods__ = {}
    for _s in [Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TripleProductOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TripleProductOperator, name)
    __repr__ = _swig_repr

    def __init__(self, A, B, C, ownA, ownB, ownC):
        """__init__(mfem::TripleProductOperator self, Operator A, Operator B, Operator C, bool ownA, bool ownB, bool ownC) -> TripleProductOperator"""
        this = _operators.new_TripleProductOperator(A, B, C, ownA, ownB, ownC)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(TripleProductOperator self, Vector x, Vector y)"""
        return _operators.TripleProductOperator_Mult(self, x, y)


    def MultTranspose(self, x, y):
        """MultTranspose(TripleProductOperator self, Vector x, Vector y)"""
        return _operators.TripleProductOperator_MultTranspose(self, x, y)

    __swig_destroy__ = _operators.delete_TripleProductOperator
    __del__ = lambda self: None
TripleProductOperator_swigregister = _operators.TripleProductOperator_swigregister
TripleProductOperator_swigregister(TripleProductOperator)

class ConstrainedOperator(Operator):
    """Proxy of C++ mfem::ConstrainedOperator class."""

    __swig_setmethods__ = {}
    for _s in [Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ConstrainedOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ConstrainedOperator, name)
    __repr__ = _swig_repr

    def __init__(self, A, list, own_A=False):
        """
        __init__(mfem::ConstrainedOperator self, Operator A, intArray list, bool own_A=False) -> ConstrainedOperator
        __init__(mfem::ConstrainedOperator self, Operator A, intArray list) -> ConstrainedOperator
        """
        this = _operators.new_ConstrainedOperator(A, list, own_A)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def EliminateRHS(self, x, b):
        """EliminateRHS(ConstrainedOperator self, Vector x, Vector b)"""
        return _operators.ConstrainedOperator_EliminateRHS(self, x, b)


    def Mult(self, x, y):
        """Mult(ConstrainedOperator self, Vector x, Vector y)"""
        return _operators.ConstrainedOperator_Mult(self, x, y)

    __swig_destroy__ = _operators.delete_ConstrainedOperator
    __del__ = lambda self: None
ConstrainedOperator_swigregister = _operators.ConstrainedOperator_swigregister
ConstrainedOperator_swigregister(ConstrainedOperator)

class PyOperatorBase(Operator):
    """Proxy of C++ mfem::PyOperatorBase class."""

    __swig_setmethods__ = {}
    for _s in [Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyOperatorBase, name, value)
    __swig_getmethods__ = {}
    for _s in [Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PyOperatorBase, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::PyOperatorBase self, int s=0) -> PyOperatorBase
        __init__(mfem::PyOperatorBase self) -> PyOperatorBase
        __init__(mfem::PyOperatorBase self, int h, int w) -> PyOperatorBase
        """
        if self.__class__ == PyOperatorBase:
            _self = None
        else:
            _self = self
        this = _operators.new_PyOperatorBase(_self, *args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(PyOperatorBase self, Vector x, Vector y)"""
        return _operators.PyOperatorBase_Mult(self, x, y)


    def _EvalMult(self, arg0):
        """_EvalMult(PyOperatorBase self, Vector arg0) -> Vector"""
        return _operators.PyOperatorBase__EvalMult(self, arg0)

    __swig_destroy__ = _operators.delete_PyOperatorBase
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _operators.disown_PyOperatorBase(self)
        return weakref_proxy(self)
PyOperatorBase_swigregister = _operators.PyOperatorBase_swigregister
PyOperatorBase_swigregister(PyOperatorBase)

class PyTimeDependentOperatorBase(TimeDependentOperator):
    """Proxy of C++ mfem::PyTimeDependentOperatorBase class."""

    __swig_setmethods__ = {}
    for _s in [TimeDependentOperator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyTimeDependentOperatorBase, name, value)
    __swig_getmethods__ = {}
    for _s in [TimeDependentOperator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PyTimeDependentOperatorBase, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::PyTimeDependentOperatorBase self, int n=0, double _t=0.0) -> PyTimeDependentOperatorBase
        __init__(mfem::PyTimeDependentOperatorBase self, int n=0) -> PyTimeDependentOperatorBase
        __init__(mfem::PyTimeDependentOperatorBase self) -> PyTimeDependentOperatorBase
        __init__(mfem::PyTimeDependentOperatorBase self, int h, int w, double _t=0.0) -> PyTimeDependentOperatorBase
        __init__(mfem::PyTimeDependentOperatorBase self, int h, int w) -> PyTimeDependentOperatorBase
        """
        if self.__class__ == PyTimeDependentOperatorBase:
            _self = None
        else:
            _self = self
        this = _operators.new_PyTimeDependentOperatorBase(_self, *args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(PyTimeDependentOperatorBase self, Vector x, Vector y)"""
        return _operators.PyTimeDependentOperatorBase_Mult(self, x, y)


    def _EvalMult(self, arg0):
        """_EvalMult(PyTimeDependentOperatorBase self, Vector arg0) -> Vector"""
        return _operators.PyTimeDependentOperatorBase__EvalMult(self, arg0)

    __swig_destroy__ = _operators.delete_PyTimeDependentOperatorBase
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _operators.disown_PyTimeDependentOperatorBase(self)
        return weakref_proxy(self)
PyTimeDependentOperatorBase_swigregister = _operators.PyTimeDependentOperatorBase_swigregister
PyTimeDependentOperatorBase_swigregister(PyTimeDependentOperatorBase)


class PyOperator(PyOperatorBase):
   def __init__(self, *args):
       PyOperatorBase.__init__(self, *args)
   def _EvalMult(self, x):
       return self.EvalMult(x.GetDataArray())
   def EvalMult(self, x):
       raise NotImplementedError('you must specify this method')

class PyTimeDependentOperator(PyTimeDependentOperatorBase):
   def __init__(self, *args):  
       PyTimeDependentOperatorBase.__init__(self, *args)
   def _EvalMult(self, x):
       return self.EvalMult(x.GetDataArray())
   def EvalMult(self, x):
       raise NotImplementedError('you must specify this method')


# This file is compatible with both classic and new-style classes.


