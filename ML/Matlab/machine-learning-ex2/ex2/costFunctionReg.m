function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta


h = sigmoid(X*theta);

%J =(1/m) * (((-y * log(h)) - (1 - y*)*(log(1-h))))

sum_1 = -y' * log(h);
sum_2 = (1-y)' * (log(1-h));

total_sum = sum_1 - sum_2;
non_reg_J = total_sum/m;

error = h-y;
non_reg_grad = (1/m)*(X' * error);


theta(1) = 0;

sum_sq_theta = theta' * theta;

reg_for_J = (lambda/(2*m))* sum_sq_theta;

J = non_reg_J + reg_for_J;

reg_for_grad = (lambda/(m))*(theta);

grad = non_reg_grad + reg_for_grad;


% =============================================================

end
