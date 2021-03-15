function [R,I] = forward_dft(X)
  N = size(X)(1,1);
  
  k = [0:(N/2)];
  i = [0:N-1];
  
  ki = k'*i;
  ki = (2*pi/N) .* ki;
  
  cs = cos(ki);
  sn = -sin(ki);
  
  R = cs*X;
  I = sn*X;

endfunction