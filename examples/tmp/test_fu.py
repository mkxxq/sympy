from sympy import latex
from sympy.parsing.latex import parse_latex
from sympy.simplify.fu import TR14


def test_tr14():
    print()
    cases =[
        r"(\cos x + 1)(\sin x + 1)(\cos x - 1)",
    ]

    for case in cases:
        cal = parse_latex(case)
        scal = TR14(cal)
        print("origin:",case,"after simple:",latex(scal))
