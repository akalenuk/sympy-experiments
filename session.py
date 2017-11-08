a, b, c = symbols('a b c')
aa, bb, cc = symbols('aa bb cc')
dd, ee, ff = symbols('dd ee ff')
x0, x1, x2, x3 = symbols('x0 x1 x2 x3')
y0, y1, y2, y3 = symbols('y0 y1 y2 y3')

x_0, y_0 = (0, 0)
x_1, y_1 = (0, 1)
x_2, y_2 = (1, 0)
x_3, y_3 = (1, 1)

# 1 
linsolve([aa*x_0 + bb*y_0 + cc - x0*a*x_0 - x0*b*y_0 - x0*c,
          dd*x_0 + ee*y_0 + ff - y0*a*x_0 - y0*b*y_0 - y0*c,          
          aa*x_1 + bb*y_1 + cc - x1*a*x_1 - x1*b*y_1 - x1*c,
          dd*x_1 + ee*y_1 + ff - y1*a*x_1 - y1*b*y_1 - y1*c,
          aa*x_2 + bb*y_2 + cc - x2*a*x_2 - x2*b*y_2 - x2*c,
          dd*x_2 + ee*y_2 + ff - y2*a*x_2 - y2*b*y_2 - y2*c,
          aa*x_3 + bb*y_3 + cc - x3*a*x_3 - x3*b*y_3 - x3*c,
          dd*x_3 + ee*y_3 + ff - y3*a*x_3 - y3*b*y_3 - y3*c,
	  c - 1], (aa, bb, cc, dd, ee, ff, a, b, c))

# 2 
linsolve([cc - x0*c,
          ff - y0*c,          
          bb + cc - x1*b - x1*c,
          ee + ff - y1*b - y1*c,
          aa + cc - x2*a - x2*c,
          dd + ff - y2*a - y2*c,
          aa + bb + cc - x3*a - x3*b - x3*c,
          dd + ee + ff - y3*a - y3*b - y3*c,
	  c - 1], (aa, bb, cc, dd, ee, ff, a, b, c))

# 3
linsolve([cc - x0*c,
          ff - y0*c,          
	  c - 1], (cc, ff, c))

# cc, ff, c =  x0, y0, 1

linsolve([bb + x0 - x1*b - x1,
          ee + y0 - y1*b - y1,
          aa + x0 - x2*a - x2,
          dd + y0 - y2*a - y2], (aa, bb, dd, ee))

# aa, bb, dd, ee = a*x2 - x0 + x2, b*x1 - x0 + x1, a*y2 - y0 + y2, b*y1 - y0 + y1

linsolve([a*x2 - x0 + x2 + b*x1 - x0 + x1 + 1 - x3*a - x3*b - x3,
          a*y2 - y0 + y2 + b*y1 - y0 + y1 + y0 - y3*a - y3*b - y3], (a, b))

# a = (-2*x0*y1 + 2*x0*y3 + x1*y0 - x1*y2 + x2*y1 - x2*y3 - x3*y0 + x3*y2 + y1 - y3)/(x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2)
# b = ((x2 - x3)*(-y0 + y1 + y2 - y3) - (y2 - y3)*(-2*x0 + x1 + x2 - x3 + 1))/((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))

expand(((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3)))

# x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2

factor(-2*x0*y1 + 2*x0*y3 + x1*y0 - x1*y2 + x2*y1 - x2*y3 - x3*y0 + x3*y2 + y1 - y3)
collect(-2*x0*y1 + 2*x0*y3 + x1*y0 - x1*y2 + x2*y1 - x2*y3 - x3*y0 + x3*y2 + y1 - y3, (x0, x1, x2, x3))
# x0*(-2*y1 + 2*y3) + x1*(y0 - y2) + x2*(y1 - y3) + x3*(-y0 + y2) + y1 - y3
# -2*x0*(y1 - y3) + x1*(y0 - y2) + x2*(y1 - y3) - x3*(y0 - y2) + y1 - y3
# (y1 - y3)*(x2 - 2*x0) + (y0 - y2)*(x1 - x3) + y1 - y3
# (y1 - y3)*(x2 - 2*x0 + 1) + (y0 - y2)*(x1 - x3)


# d = 1 / ((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))
#
# a = ((y1 - y3)*(x2 - 2*x0 + 1) + (y0 - y2)*(x1 - x3)) * d
# b = ((x2 - x3)*(-y0 + y1 + y2 - y3) - (y2 - y3)*(-2*x0 + x1 + x2 - x3 + 1)) * d
# c = 1
# aa = a*x2 - x0 + x2
# bb = b*x1 - x0 + x1
# cc = x0
# dd = a*y2 - y0 + y2
# ee = b*y1 - y0 + y1
# ff = y0
