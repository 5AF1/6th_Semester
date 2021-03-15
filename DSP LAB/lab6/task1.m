n = 512;
x = rand(1,n);
dft_len = [];
dft_tim = [];
fft_len = [];
fft_tim = [];

for i = 1:n/2
  dft_len = [dft_len 2*i];
  t = tic();
  a = forward_dft(x(1:2*i)');
  t = toc(t);
  dft_tim = [dft_tim t];
  
  fft_len = [fft_len 2*i];
  t = tic();
  a = fft(x(1:2*i)');
  t = toc(t);
  fft_tim = [fft_tim t];
endfor

hold on;
xlabel('Length'); 
ylabel('Time'); 

plot (dft_len,dft_tim,'r');
plot (fft_len,fft_tim,'g');

legend('DFT','FFT');
title ("Convolution input side");