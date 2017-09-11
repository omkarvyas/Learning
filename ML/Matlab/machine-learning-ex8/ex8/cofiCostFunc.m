function [J, grad] = cofiCostFunc(params, Y, R, num_users, num_movies, ...
                                  num_features, lambda)
%COFICOSTFUNC Collaborative filtering cost function
%   [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, ...
%   num_features, lambda) returns the cost and gradient for the
%   collaborative filtering problem.
%

% Unfold the U and W matrices from params
X = reshape(params(1:num_movies*num_features), num_movies, num_features);
Theta = reshape(params(num_movies*num_features+1:end), ...
                num_users, num_features);

% You need to return the following values correctly
J = 0;
X_grad = zeros(size(X));
Theta_grad = zeros(size(Theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost function and gradient for collaborative
%               filtering. Concretely, you should first implement the cost
%               function (without regularization) and make sure it is
%               matches our costs. After that, you should implement the 
%               gradient and use the checkCostFunction routine to check
%               that the gradient is correct. Finally, you should implement
%               regularization.
%
% Notes: X - num_movies  x num_features matrix of movie features
%        Theta - num_users  x num_features matrix of user features
%        Y - num_movies x num_users matrix of user ratings of movies
%        R - num_movies x num_users matrix, where R(i, j) = 1 if the 
%            i-th movie was rated by the j-th user
%
% You should set the following variables correctly:
%
%        X_grad - num_movies x num_features matrix, containing the 
%                 partial derivatives w.r.t. to each element of X
%        Theta_grad - num_users x num_features matrix, containing the 
%                     partial derivatives w.r.t. to each element of Theta
%



% R: a matrix of observations (binary values). Dimensions are (movies x users)
% 
% Y: a matrix of movie ratings: Dimensions are (movies x users)
% 
% X: a matrix of movie features (0 to 5): Dimensions are (movies x features)
% 
% Theta: a matrix of feature weights: Dimensions are (users x features)            

% 
% - Compute the predicted movie ratings for all users using 
% the product of X and Theta. A transposition may be needed.

predicted_movie_rating = X * Theta';

% Compute the movie rating error by subtracting Y from the predicted ratings.

movie_rating_error = predicted_movie_rating - Y;

% Compute the "error_factor" my multiplying the movie rating error by the R matrix. 
% The error factor will be 0 for movies that a user has not rated. 
% Use the type of multiplication by R (vector or element-wise) so the size 
% of the error factor matrix remains unchanged (movies x users).


error_factor = movie_rating_error .* R;
error_factor_sq = error_factor(:) .^ 2; % Crucial step (:) makes vector of matrix
J = (1/2)*sum(error_factor_sq);




X_grad = error_factor * Theta;

Theta_grad = error_factor' * X;


regularization_theta_term = (lambda\2)*sum(sum(Theta(:) .^2 ));
regularization_x_term = (lambda\2)*sum(sum(X(:) .^2));

Reg_J = J + regularization_theta_term + regularization_x_term;

% =============================================================

grad = [X_grad(:); Theta_grad(:)];

end
