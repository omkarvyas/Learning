function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%

h = X * theta;

err = h - y;

err_sq = err.^2;

err_sum = sum(err_sq);

J = 1/(2*m)*err_sum;

grad = (1/m)*(X'*err);

theta(1) = 0;

theta_sum = sum(theta.^2);

scale = lambda/(2*m);

theta_sum = scale * theta_sum;

J = J + theta_sum;

reg_grad = theta*(lambda/m);

%;

grad = grad + reg_grad;
























% =========================================================================

grad = grad(:);

end
