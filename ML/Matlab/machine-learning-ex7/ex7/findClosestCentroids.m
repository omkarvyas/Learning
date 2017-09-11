function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])
%

% Set K
K = size(centroids, 1);

% You need to return the following variables correctly.
idx = zeros(size(X,1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Go over every example, find its closest centroid, and store
%               the index inside idx at the appropriate location.
%               Concretely, idx(i) should contain the index of the centroid
%               closest to example i. Hence, it should be a value in the 
%               range 1..K
%
% Note: You can use a for-loop over the examples to compute this.
%

%for c = 1:idx
%    for x = 1:K

[m, n] = size(X);

distance = zeros(m,K);


% Use a for-loop over the 1:K centroids
for c = 1:K
    % Inside this loop, 
    % create a column vector of the distance 
    % from each training example to that centroid, 
    % and store it as a column of the distance matrix. 
    % One method is to use the bsxfun) function 
    % and the sum() function to calculate 
    % the sum of the squares of the differences between 
    % each row in the X matrix and a centroid.
    
    D = bsxfun(@minus,X,centroids(c,:));
    cv = sum(D.^2,2);
    cv = cv';
    distance(:,c) = cv;
end

[val idx] = min(distance,[],2);

% =============================================================

end

