function [X] = my_inverse_conv2(Y,H)
  O = size(Y)(1,2);
  M = size(H)(1,2);
  N = O-M+1;
  
  H = [zeros(1,N-1),H,zeros(1,N-1)];
  Stack_H = zeros(N, N);
  for i = 1:(N)
    Stack_H(i,:) = H(1,i:i+N-1);
  endfor
  
  Stack_H = [Stack_H,Y(1:N)'];
  
  Stack_H = rref(Stack_H); #solving the first N equations
  
  X = flip(Stack_H(:,N+1))';
  
endfunction