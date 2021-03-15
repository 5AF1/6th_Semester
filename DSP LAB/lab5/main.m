#Task 1
s = [1,2,3,4]'
[r,i] = forward_dft(s)
x = inverse_dft(r,i)

#Task 2
LIMIT = 450; #Gives error if above 45K

[A Fs] = audioread('underwater.wav');
A = A(1:LIMIT,1);
sound(A,Fs);

[R,I] = forward_dft(A);

subplot (3, 1 , 1);
plot (A,'r');
title ("Time domain vector");
subplot (3, 1, 2);
plot (R,'g');
title ("Real part");
subplot (3, 1, 3);
plot (I,'b');
title ("imaginary part");

#Task 3
R(1:2000,1) = 0;
I(1:2000,1) = 0;

X = inverse_dft(R,I);
sound(X,Fs);


