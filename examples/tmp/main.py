import time
from sympy.parsing.latex import parse_latex
from sympy import *


def main():
    l = r"\cos(\tan^{-1}(x^2))"
    l = r"\frac{\sec^{2} (x) - 1}{\sec(x) - 10}"
    l = r"\frac{(x^2++2x +1)}{(x+1)}"
    e = parse_latex(l)
    e = simplify(e)
    print(latex(e))


if __name__ == '__main__':
    st = time.time()
    main()
    print("cost:",time.time()-st)
