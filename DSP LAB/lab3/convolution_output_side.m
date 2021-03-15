function [Y] = convolution_output_side(X,H)
  N = size(X)(1,2);
  M = size(H)(1,2);
  
  H = flip(H)';
  X = [zeros(1,M-1),X,zeros(1,M-1)];
  
  Y = zeros(1,(M+N-1));
  for i = 1:(M+N-1)
    Y(1,i) = X(1,i:i+M-1)*H;
  endfor
  
endfunction
