#include "sorting_algos.h"

/*
One of the most simple forms of sorting is that of comparing each item with
every other item in some list, however as the description may imply this form
of sorting is not particularly e®ecient O(n2). In it's most simple form bubble
sort can be implemented as two loops.
*/

/*

1) algorithm BubbleSort(list)
2) Pre: list 6= ;
3) Post: list has been sorted into values of ascending order
4) for i Ã 0 to list:Count ¡ 1
5) for j Ã 0 to list:Count ¡ 1
6) if list[i] < list[j]
7) Swap(list[i]; list[j])
8) end if
9) end for
10) end for
11) return list
12) end BubbleSort

*/

/*
Takes Array as input and sorts it in place.

*/

void BubbleSort(int *nums, int numSize){

int i = 0;
int j = 0;
int temp = 0;

    for(i = 0; i < numSize; ++i){

        for(j = 0; j < numSize; ++j){

            if(nums[i] < nums[j]){

                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;

            }

        }
    }

}


/*

Merge sort is an algorithm that has a fairly effcient space time complexity - O(n log n) and is fairly trivial to implement. The algorithm is based on splitting
a list, into two similar sized lists (left, and right) and sorting each list and then merging the sorted lists back together.
Note: the function MergeOrdered simply takes two ordered lists and makes
them one.

*/


/*

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = (l+r)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)

*/











