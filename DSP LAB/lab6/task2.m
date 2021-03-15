time = [0:29];
x = 2*cos((pi*time)/10);
N = 2048;
X = abs(fft(x,N));

hold on;
plot (X,'color', [42  137  199]./255);

h = hamming(30)';
X = x .* h;
X = abs(fft(X,N));

plot (X,'color', [227  132  90]./255);
legend('Before Hamming window','After Hamming window');