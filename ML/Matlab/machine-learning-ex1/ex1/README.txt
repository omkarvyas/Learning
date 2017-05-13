Problem
1. In this part of this exercise, you will implement linear regression with one variable to predict profits for a food truck.
2. Suppose you are the CEO of a restaurant franchise and are considering dierent cities for opening a new outlet. The chain already has trucks in various cities and you have data for prots and populations from the cities.
3. You would like to use this data to help you select which city to expand to next.
4. ex1data1.txt population vs profit 
Solution
1. understand the data by visualizing 
2. PLOT the data. 
3. The objective of linear regression is to minimize the cost function cost function equation J(theta)
4. Hypothesis h theata (x) is linear model theta zero + theta1*x1 (thetas actually are slope consants)
5. Cost function is actually difference in prediction and actual output value
6. alpha is learning rate 
7. m is number of samples 
8. x(i) input y(i) output 
9. parameters of model are theta_j these are values we will adjest to minimize cost function J(theta)
10. use batch gradiant decent algo
11. add another dimention of 1's to your data to accomodate theta_0
12. alpha is 0.01


%%%%%%%%%%%%%%%%%%%%%%

computeCost.m

%%%%%%%%%%%% Cost function only not yet gradient decent it is just a cost of our hypothesis predection and error we get with respect to actual output %%%%%%%%%%%

13. function J = computeCost(X, y, theta) 
	: J = COMPUTECOST(X, y, theta) computes the cost of using theta as the parameter for linear regression to fit the data points in X and y
	m = length(y); % number of training examples
	J = 0

	% Instructions: Compute the cost of a particular choice of theta
	% You should set J to the cost. The hypothesis (also called the prediction) is simply the product of X and theta. 

%   h = {multiply X and theta, in the proper order that the inner dimensions match}

Vector multiplication!


h = X*theta;

% Since X is size (m x n) and theta is size (n x 1) you arrange the order of operators so the result is size (m x 1).

% The second line of code will compute the difference between the hypothesis and y -  that's the error for each training example.

error = h - y;

% The third line of code will compute the square of each of those error  terms (using element-wise exponentiation),


error_sqr = error.^2;

%   Next, here's an example of how the sum function works  Cost function equation. equation 2.2.1 in ex1.pdf 

J = (1/(2*m))* sum (error_sqr);




Problem:
1. Next, you will implement gradient descent in the le gradientDescent.m. The loop structure has been written for you, and you only need to supply the updates to theta within each iteration.
2. We should just change the theta not X or y
3. Each step should reduce the cost function J which was computed previously. 


%%%%%%%%%%%%%%%%%%%%%%

gradientDescent.m

%%%%%%%%%%% Gradient Decent %%%%%%%%%%%%

function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)

% Some gradient descent settings
iterations = 1500;
alpha = 0.01;

%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);





for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %

    %   1 - The hypothesis is a vector, 
    %   formed by multiplying the X matrix and the theta vector. 
    %   X has size (m x n), and theta is (n x 1), 
    %   so the product is (m x 1). 
    %   That's good, because it's the same size as 'y'. 
    %   Call this hypothesis vector 'h'.
    
    h = X * theta;

    %     2 - The "errors vector" is the 
    %     difference between the 'h' vector and the 'y' vector.
    
    error = h - y;
    
    %   3 - The change in theta (the "gradient") 
    %   is the sum of the product of X    and the "errors vector", scaled by alpha and 1/m. Since X is (m x n), and the error vector is (m x 1), and the result you want is the same size as theta (which is (n x 1), 
    %   you need to transpose X before you can multiply it by the error vector. 
    %   The vector multiplication automatically includes calculating the sum of the products.

    theta_change = alpha *(1/m)*(X' * error);


    %   Subtract this "change in theta" from the original value of theta. 
    %   A line of code like this will do it:

    theta = theta - theta_change;
    
    % ============================================================
    %   Save the cost J in every iteration    


    J_history(iter) = computeCost(X, y, theta);

end

end





















