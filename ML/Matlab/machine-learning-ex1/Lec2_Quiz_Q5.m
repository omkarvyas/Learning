

X = magic(7);


for i = 1:7
    for j = 1:7
        A(i, j) = log(X(i,j));
        B(i, j) = X(i, j) ^ 2;
        C(i, j) = X(i, j) + 1;
        D(i, j) = X(i, j) /4;
    end
end 