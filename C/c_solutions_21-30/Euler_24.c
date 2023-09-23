/* 
 * What is the millionth lexicographic permutation of the digits
 * 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9?
 *
 */

#include "euler_util.h"

#define PERMUTATION_SIZE 10 
#define PERMUTATION_LIMIT 1000000


void sort(int permutation[], int idx)
{
    int i, j, curr;
    for (i=idx; i < PERMUTATION_SIZE - 1; i++) {
        curr = permutation[i + 1];
        j = i;
        while (j > idx && curr < permutation[j]) {
            permutation[j + 1] = permutation[j];
            permutation[j] = curr;
            j--;
        }
        permutation[j + 1] = curr;
    }
}

void swap(int permutation[], int idx1, int idx2)
{
    int tmp;
    tmp = permutation[idx1];
    permutation[idx1] = permutation[idx2];
    permutation[idx2] = tmp;    
}

int next_largest_idx(int permutation[])
{
    int i;
    for (i=PERMUTATION_SIZE - 1; i > 0; i--)
        if (permutation[i] > permutation[i - 1])
            return i - 1;
    return i;
}

int last_largest_idx(int permutation[], int idx)
{
    int i;
    for (i=PERMUTATION_SIZE - 1; i >= idx; i--)
        if (permutation[i] > permutation[idx])
            return i;
    return i;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    int one_to_ten[PERMUTATION_SIZE] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int first_idx, second_idx, count;

    int i;

    for (count=0; count < PERMUTATION_LIMIT - 1; count++) {
        first_idx = next_largest_idx(one_to_ten);
        second_idx = last_largest_idx(one_to_ten, first_idx);
        swap(one_to_ten, first_idx, second_idx);
        sort(one_to_ten, first_idx);
    }

    float stop = timeit();
    
    printf("Answer: ");

    for (i=0; i < PERMUTATION_SIZE; i++)
        printf("%d", one_to_ten[i]);

    printf("\nTime: %f\n", stop - start);

    return 0;
}
