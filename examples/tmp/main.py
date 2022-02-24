import math
from sympy.parsing.latex import parse_latex
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


def simple_compute(s):
    origin = parse_latex(s)
    simpl = simplify(origin)
    return origin,simpl


def solve_compute(s):
    origin = parse_latex(s)
    res = solve(origin)
    return origin,res


def factor_compute(s):
    origin = parse_latex(s)
    res = factor(origin)
    return origin,res


def trigsimp_compute(s):
    origin = parse_latex(s)
    res = trigsimp(origin)
    return origin,res


def main():
    cal = parse_latex(r"( 1 + \cot ^ { 2 } x ) ( 1 - \cos ^ { 2 } x )")
    scal = _futrig(cal)
    print("final result", scal)


if __name__ == '__main__':
    main()
