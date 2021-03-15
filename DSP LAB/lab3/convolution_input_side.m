function [Y] = convolution_input_side(X,H)
  N = size(X)(1,2);
  M = size(H)(1,2);
  
  X = flip(X)';
  H = [zeros(1,N-1),H,zeros(1,N-1)];
  
  Y = zeros(1,(M+N-1));
  for i = 1:(M+N-1)
    Y(1,i) = H(1,i:i+N-1)*X;
  endfor
  
endfunction
