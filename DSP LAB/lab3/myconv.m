function [Y] = myconv(X,H)
  N = size(X)(1,2);
  M = size(H)(1,2);
  
  X = flip(X)';
  H = [zeros(1,N-1),H,zeros(1,N-1)];
  Stack_H = zeros(M+N-1, N);
  
  Y = zeros(1,(M+N-1));
  for i = 1:(M+N-1)
    Stack_H(i,:) = H(1,i:i+N-1);
  endfor
  Y = (Stack_H*X)';
  
endfunction
