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
13. function J = computeCost(X, y, theta) 
	: J = COMPUTECOST(X, y, theta) computes the cost of using theta as the parameter for linear regression to fit the data points in X and y
	m = length(y); % number of training examples
	J = 0

	% Instructions: Compute the cost of a particular choice of theta
	% You should set J to the cost. The hypothesis (also called the prediction) is simply the product of X and theta. 

%   h = {multiply X and theta, in the proper order that the inner dimensions match}

h = X*theta;

% Since X is size (m x n) and theta is size (n x 1) you arrange the order of operators so the result is size (m x 1).

% The second line of code will compute the difference between the hypothesis and y -  that's the error for each training example.

error = h - y;

% The third line of code will compute the square of each of those error  terms (using element-wise exponentiation),


error_sqr = error.^2;

%   Next, here's an example of how the sum function works  Cost function equation. equation 2.2.1 in ex1.pdf 

J = (1/(2*m))* sum (error_sqr);


