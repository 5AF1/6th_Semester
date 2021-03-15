x = [2:0.1:3]
#y = 20 * x -36

y = [4:2:4+2*(length(x)-1)]

A = [x;ones(1,11);y]

z = mean(A,1)

zz = sum(A,2)