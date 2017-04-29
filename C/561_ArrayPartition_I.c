#include <stdio.h>
#include <stdlib.h>
#include "sorting_algos.h"

int arrayPairSum(int *nums, int numsSize){

int i = 0;
int Sum = 0;


    for(i = 0; i<numsSize; ++i){
        printf("\n input = %d \n",nums[i]);
        Sum = Sum + nums[i];
    }
return Sum;

}

#define Number_Of_Elements 10

int main(void){

int arr[Number_Of_Elements] = {1,6,4,3,2,7,8,12,44,3};
int Sum = 0;
int i = 0;

for(i = 0; i<Number_Of_Elements; ++i){

    printf("\ninput = %d",arr[i]);

}

BubbleSort(arr,Number_Of_Elements);

printf("\n After Bubble Sort \n");

for(i = 0; i<Number_Of_Elements; ++i){

    printf("\n output = %d",arr[i]);

}

Sum = arrayPairSum(arr,Number_Of_Elements);
printf("\n Sum = %d \n", Sum);

return 0;

}
