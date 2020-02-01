pkg load symbolic

syms y(t)
ode = diff(y, t) == t*y
ySol(t) = dsolve(ode)
cond = y(0) == 2;
Note that the semicolon can not be omitted

% Solve with condition
ySol(t) = dsolve(ode, cond)

clear
syms y(x)
DE = (diff(y,x) + y)^2 == 0
dsolve (DE, y(0) == 1)

clear
syms y(x)
Dy = diff(y)
ode = diff(y,x,2) == cos(2*x)-y
cond1 = y(0) == 1
cond2 = Dy(0) == 0
ySol(x) = dsolve(ode,cond1,cond2)
vpa(ySol(0))


clear
syms y(x)
ode = 2*x^2*diff(y,x,2)+3*x*diff(y,x)-y == 0
dsolve(ode)

clear
syms y(x)
ode = diff(y,x,2) == x*y
dsolve(ode)

