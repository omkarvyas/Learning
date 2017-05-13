.mat file format means data is in saved in native matlab matrix format, instead of text ASCII format like .csv file. 
ex3data1.mat 5000 training examples 
each training example is a 20x20 pixel gray-scale image of the digit 
each pixel is represented by floating point number indicating the gray scale intensity at that location
20x20 grid of pixels is unrolled into a 400 dimensional vector 
each of these training examples becomes a single row in our data matrix X
This gives us 5000 by 400 matrix X where every row is a training example for a handwritten digit image. 

X = [ ---x(1) T---]

second part of training set is a 5000 dimensional vector y that contains labels for the training set. 
To make things more compatible with Matlab indexing where there is no zero index we mapped digit 0 to 10 and 1 to 9 are 1 to 9





