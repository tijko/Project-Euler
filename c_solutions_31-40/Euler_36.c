#include <math.h>
#include <stdio.h>


int base10[7];
int base2[22];

int to_base_ten(int value)
{
    int digits = 0;

    for (; value > 0; digits++) {
        base10[digits] = value % 10;
        value /= 10;
    }

    return digits;        
}

int to_base_two(int value)
{
    int places = 0;

    for (; value > 0; places++) {
        base2[places] = value % 2;
        value >>= 1;
    }

    return places;
}

int palindrome(int *narray, int length)
{
    for (int i=0, j=length-1; i < j; i++, j--)
        if (narray[i] != narray[j]) return 0;
    return 1;
}

int main(int argc, char *argv[])
{
    int double_palindromes = 0;

    for (int i=1; i < pow(10, 6); i++) { 
        if (palindrome(base10, to_base_ten(i)) &&
            palindrome(base2, to_base_two(i))) {
            double_palindromes += i;
        }
    }

    printf("Answer: %d\n", double_palindromes);

    return 0;
}
