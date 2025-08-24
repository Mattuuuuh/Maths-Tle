from gekko import GEKKO
m = GEKKO(remote=False)
x,y = m.Array(m.Var,2,lb=0)
m.Equations([6*x+4*y<=24,x+2*y<=6,-x+y<=1,y<=2])
m.Maximize(x+y)
m.solve(disp=False)
