from sympy import Symbol, solve, cbrt, N, re

a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
ysq = x**3+a*x+b
ymax = Symbol('ymax')
xmin = solve(ysq,x)
bvalue = 1
ymaxvalue = 3.5
xmax_eq = (ysq - ymax**2).subs(b,bvalue).subs(ymax,ymaxvalue)

print("\nGeneral solution for x^3 + ax + b = 0\n")
for i in range(len(xmin)):
    print("x_" + str(i+1) + " = " + str(xmin[i]))

print("\nelliptic-fibres-neg.tex\n")
avalue = 0
xmax = solve(xmax_eq.subs(a,avalue),x)
print("\\newcommand{\\xmax}{" + str(N(xmax[0])) + "}")
xmin_N = float(N(xmin[0].subs(a,avalue).subs(b,bvalue)))
print("\\newcommand{\\xmin}{" + str(xmin_N) + "}")

print("\nelliptic-fibres-zero.tex\n")
avalue = -3*cbrt(2)/2
xmax = solve(xmax_eq.subs(a,avalue),x)
print("\\newcommand{\\xmax}{" + str(N(xmax[0])) + "}")
xmin_N = N(xmin[0].subs(a,avalue).subs(b,bvalue))
print("\\newcommand{\\xmin}{" + str(xmin_N) + "}")
xnode_N = re(N(xmin[1].subs(a,avalue).subs(b,bvalue)))
print("\\newcommand{\\xnode}{" + str(xnode_N) + "}")

print("\nelliptic-fibres-pos.tex")
avalue = -3
xmax = solve(xmax_eq.subs(a,avalue),x)
print("\\newcommand{\\xmax}{" + str(N(xmax[0])) + "}")
xmin_N = re(N(xmin[0].subs(a,avalue).subs(b,bvalue)))
print("\\newcommand{\\xmin}{" + str(xmin_N) + "}")
xii_N = re(N(xmin[1].subs(a,avalue).subs(b,bvalue)))
print("\\newcommand{\\xii}{" + str(xii_N) + "}")
xiii_N = re(N(xmin[2].subs(a,avalue).subs(b,bvalue)))
print("\\newcommand{\\xiii}{" + str(xiii_N) + "}")
