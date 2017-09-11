ex4data1.mat = 5000 training examples = put it in X

each training example is 20x20 pixel grayscale 

X is 5000x400 matrix 5000 rows and 400 coloumns each row is one training set and each training set is 20x20 matrix which is flatend or "unrolled" into a 400 dimentional vector. 

y contains lables for the trining set 

digit zero is mapped to value 10

images are 20 x 20 that gives 400 input layer units not contianing the extra bias unit which always output 1. 

Training data is loaded in X and y

y first 500 = 10
second 500 = 1
3rd 500 = 2
4th 500 = 3 and so on..

already trained THETA-s Theta1 and Theta 2 are already provided to you and are already trained by examiner ex4weights.mat and will be loaded to Theta1 and Theta2 
Theta1 is 25x401 matrix representing hidden layer 
Theta1 is 10x401 matrix representing output layer 

Now you will implement the cose function and gradient of the neural network, first complete the code in nnConstFunction.m to reurn the cost

cost function for the neural network without regularization is 1/m * (sum i=1 to m) sum(k =1 to K)[-yki log((htheta(xi))k) - (1-yki)log(1-(htheta(xi))k)]


where htheta(xi) is coputed as K=10 total numbe of possible labels 
htheta(xi)k = ak(3) is activation output value of kth output unit

for the purpose of traiing a neural network we need to record the labels as vectors contianing only values 0 or 1 so that 

y = [1 0 0 0 0 0 0 0 0 0]'
y = [0 1 0 0 0 0 0 0 0 0]'
y = [0 0 1 0 0 0 0 0 0 0]'
y = [0 0 0 1 0 0 0 0 0 0]' and so on 


you should implement the feedforward computation that computes htheta(xi) for every example i and sum the cost over all examples. 









