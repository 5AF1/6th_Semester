function [X] = my_inverse_conv(Y,H)
  O = size(Y)(1,2);
  M = size(H)(1,2);
  N = O-M+1;
  
  H = [zeros(1,N-1),H,zeros(1,N-1)];
  Stack_H = zeros(O, N);
  for i = 1:(O)
    Stack_H(i,:) = H(1,i:i+N-1);
  endfor
  
  #Explanation
  #Y = conv(X,H)
  #Y' = Stack_H * flip(X)'
  #Stack_H' * Y' = Stack_H' * Stack_H * flip(X)'
  
  A = Stack_H'*Stack_H;
  #Stack_H' * Y' = A * flip(X)'
  #inverse(A) * Stack_H' * Y' = flip(X)'
  #X = flip(inverse(A) * Stack_H' * Y')'
  
  X = flip(inverse(A) * Stack_H' * Y')';
  
endfunction