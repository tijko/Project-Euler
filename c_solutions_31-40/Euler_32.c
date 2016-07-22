#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int pandigits[9];
int digits[5000];

int length;
int found;

void peel(int *set)
{
    for (int i=0; i < 3; i++) {
        int num = set[i];
        while (num > 0) {
            int current_digit = num % 10;
            num /= 10;
            length++;
            pandigits[current_digit - 1] = 1;
        }            
    }
}

bool is_pandigital(void)
{
    int nine = 0;

    for (int i=0; i < 9; i++)
        nine += pandigits[i];

    if (nine == 9) 
        return true;

    return false;
}

bool unique(int can)
{
    for (int i=0; i < found; i++)
        if (digits[i] == can) return false;
    return true;
}

int main(int argc, char *argv[])
{
    int total = 0;
    found = 0;

    memset(digits, 0, sizeof(int) * 5000);

    for (int i=2; i < 100; i++) {
        for (int j=100; j < 5000; j++) {
            memset(pandigits, 0, sizeof(int) * 9);
            length = 0;
            int set[3] = {i * j, i, j};
            peel(set);
            if (length > 9) continue;
            if (is_pandigital()) 
                if (unique(i*j))
                    digits[found++] = i * j;
        }
    }
    
    for (int i=0; i < found; i++)
        total += digits[i];

    printf("%d\n", total);

    return 0;
}

