function [Z] = forward_dft(X)
  N = size(X)(1,1);
  
  k = [0:(N/2)];
  ii = [0:N-1];
  
  ki = k'*ii;
  ki = (2*pi/N) .* ki;
  
  cs = cos(ki);
  sn = -sin(ki);
  
  R = cs*X;
  I = sn*X;
  
  Z = R+i*I;

endfunction