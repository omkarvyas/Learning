function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m

eye_matrix = eye(num_labels)
y_matrix = eye_matrix(y,:)

% a1 equals the X input matrix with a column of 1's added 
% (bias units) as the first column

temp = size(X,1);
a1 = [ones(temp,1) X];

% z2 equals the product of a1 and ?1(Theta1)

z2 = a1*Theta1';

% a2 is the result of passing z2 through g()and g() is the sigmoid function.

a2 = sigmoid(z2);

% Then add a column of bias units to a2 (as the first column).
% NOTE: Be sure you DON'T add the bias units as a new row of Theta

temp = size(a2,1);

a2 = [ones(temp,1) a2];

% z3 equals the product of a2 and ?2

z3 = a2 * Theta2';


a3 = sigmoid(z3);

%elementwise multiplication

% first half of equestion true clasification
sum_1 = -(y_matrix .* log(a3));

% second part of equeation false clasification 
sum_2 = (1-y_matrix) .* log(1-a3);

% subtract second term from first term 
inner_calc = sum_1 - sum_2;

% Sclae the double sum by m; double sum is actually sum over coloumns and
% rows, matrix is already m x K size so this double sum automatically
% calculates double sum for respective lenght 
% i.e. number of training examples m varies from i = 1 to m in our that is
% 1 to 5000 
% Other sum of classes or possiblities varies from k = % 1 to K that is 10 

J = 1/m * sum(sum(inner_calc));


% Regularized J

J = 0;

scaling = lambda/(2*m);

% remove the bias term that is remove first coloumn of both theta

Theta1(:,1) = [];
Theta2(:,1) = [];

% element wise multiplication of Thetas to get the square of each term

Theta1_sqr = Theta1 .* Theta1;

Theta2_sqr = Theta2 .* Theta2;

% double sum of matrix Theta1 square and Theta2 square 

Theta1_Double_sum = sum(sum(Theta1_sqr));

Theta2_Double_sum = sum(sum(Theta2_sqr));

%regularization calculation

regularization = scaling*(Theta1_Double_sum + Theta2_Double_sum)

%adding cost term to regularization 

J = 1/m * sum(sum(inner_calc)) + regularization;

%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.


% m = the number of training examples

% n = the number of training features, including the initial bias unit.

% h = the number of units in the hidden layer - NOT including the bias unit

% r = the number of output classifications

d3 = a3 - y_matrix;

% z2 came from the forward propagation process - 
% it's the product of a1 and Theta1, 
% prior to applying the sigmoid() function. 
% Dimensions are (m x n) ? (n x h) --> (m x h)

sig_grad_z2 = sigmoidGradient(z2);

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

Theta2 = Theta2(:,2:end);

d3_Theta2_product = d3 * Theta2;

d2 = sig_grad_z2 .* d3_Theta2_product;
 
Delta1 = d2' * a1;

Delta2 = d3' * a2;

Theta1_grad = Delta1/m;

Theta2_grad = Delta2/m;
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

             
Theta1(:,1) = 0;
Theta2(:,1) = 0;

Theta1 = Theta1 *(lambda/m);
Theta2 = Theta2 *(lambda/m);

Theta1_grad = Theta1_grad + Theta1;
Theta2_grad = Theta2_grad + Theta2;


% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
