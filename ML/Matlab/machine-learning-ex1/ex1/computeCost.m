function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

%   The hypothesis (also called the prediction) 
%   is simply the product of X and theta. 

%   h = {multiply X and theta, 
%   in the proper order that the inner dimensions match}

h = X*theta;


%   Since X is size (m x n) and theta is size (n x 1), 
%   you arrange the order of operators so the result is size (m x 1).
%   The second line of code will compute the difference between 
%   the hypothesis and y -  that's the error for each training example. 
%   Difference means subtract. error = {the difference between h and y}

error = h - y;

%   The third line of code will compute the square of each of those error 
%   terms (using element-wise exponentiation),

error_sqr = error.^2;

%   Next, here's an example of how the sum function works 

% Cost function equation. 

J = (1/(2*m))* sum (error_sqr);



% =========================================================================

end
