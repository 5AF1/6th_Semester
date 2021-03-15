x = [17, 4, 13, 24, 35, 43, 31, 29, 53];
h = [2, 3, 5, 7, 11];
x=[11,8,3,7,5,100,13,74,19] 
h=[1,0,2,1]

x=[-1 2 3 4]
x = [1 0 1 0 1 2 3 1 0 4 5 6]
h = [1 2 3]





iy = convolution_input_side(x,h)
oy = convolution_output_side(flip(x),(h))

subplot (2, 1 , 1);
plot (iy,'r');
title ("Convolution input side");
subplot (2, 1, 2);
plot (oy);
title ("Convolution output side");

conv(x,h)


x = [61 13 17 255 173 81 59 100]
h = [181 255 173 112]
conv(x,h)(8)


x = [3 7 2 8 1 0 2 6 9 17 13]
h = [2 8 1]
conv(x,h)(9)

x = [11 8 3 7 5 100 13 74 19]
h = [8 3 7]

conv(flip(x),h)

x = [39 17 32 8 11 0 22 16 9 17 13 14 9 7]
h = [1 0 1]
conv(x,h)