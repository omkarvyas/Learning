function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%

% Add a column of 1's to X (the first column), and it becomes 'a1'.
v = ones(1,m);

% a1 is (m x n), where 'n' is the number of features including the bias unit
a1 = [v' X]; 


% Multiply by Theta1 and you have 'z2'.
% Note: When you multiply by the Theta matrices, 
% you'll have to use transposition to get a result that is the correct size.

% Theta1 is (h x n) where 'h' is the number of hidden units

z2 = a1 * Theta1';
% Compute the sigmoid() of 'z2', then add a column of 1's, and it becomes 'a2'
% Note: Not getting the correct results? In the hidden layer, 
% be sure you use sigmoid() first, then add the bias unit.

sig = sigmoid(z2);

% a2 is (m x (h + 1))

a2 = [v' sig];

% Multiply by Theta2, compute the sigmoid() and it becomes 'a3'.
% Note: The predictions must be returned as a column vector - size (m x 1). 
% If you return a row vector, the script will not compute the accuracy correctly.

% Theta2 is (c x (h + 1)), where 'c' is the number of labels.

% a3 is (m x c)

a3 = a2 * Theta2';

% p is a vector of size (m x 1)

[max_val p] = max(a3,[],2);
















% =========================================================================


end
