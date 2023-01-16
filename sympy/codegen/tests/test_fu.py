import sys

from sympy import *
from sympy.plotting import plot
from sympy.simplify.trigsimp import _is_Expr,_eapply,_futrig
from sympy.simplify.fu import (
    TR1, TR2, TR3, TR2i, TR10, L, TR10i,
    TR8, TR6, TR15, TR16, TR111, TR5, TRmorrie, TR11, _TR11, TR14, TR22,
    TR12,as_f_sign_1)
from sympy.core.compatibility import _nodes
from sympy.functions.elementary.trigonometric import TrigonometricFunction
from sympy.core.function import count_ops, _mexpand
from sympy import Integral, Sum, Symbol

def test_tr8():
    case = [
        r'(\cos x) * 2  * (\sin x)',
    ]
    for item in case:
        exp = parse_latex(item)
        print("\ninput",item)
        res = TR8(exp)
        print("res",latex(res))

def test_syspath():
    print("\n",sys.path)





