// Find the sum of the digits in !100.

#include <time.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

#define FACTORIAL_BUFFER 200
#define FACTORIAL_TO 100
#define DIGIT_MAX 4


void overflow(int flood[], int pos)
{
    flood[pos + 1] += flood[pos] / 10;
    flood[pos] %= 10;   
}

void mul(char *factorial, int pos, int digit, int total[], int head)
{
    int i;
    
    for (i=0; i < head + 1; i++) 
        total[i + pos] += ((*(factorial + i) - '0') * digit);
}

void add(int total[], int head)
{
    int j;
    for (j=0; j <= head; j++)
        if (total[j] > 9)
            overflow(total, j);
}

int find_head(int total[])
{
    int j;
    for (j=FACTORIAL_BUFFER - 1; total[j] == 0; j--)
        ;
    return j + 1;
}

int main(int argc, char *argv[])
{
    clock_t start, stop;
    start = clock();

    char *factorial, *current;
    int total[FACTORIAL_BUFFER];
    int answer, head, pos;
    int i, j;

    factorial = malloc(sizeof(char) * FACTORIAL_BUFFER); 
    memset(factorial, '0', FACTORIAL_BUFFER);

    current = malloc(sizeof(char) * DIGIT_MAX);

    for (i=1, head=1, *factorial='1'; i <= FACTORIAL_TO; i++) {

        memset(current, '0', DIGIT_MAX);
        snprintf(current, DIGIT_MAX, "%d", i);
        memset(total, 0, sizeof(int) * FACTORIAL_BUFFER);

        for (j=strlen(current)-1, pos=0; j >= 0; j--, pos++) 
            mul(factorial, pos, *(current + j) - '0', total, head);

        head = find_head(total);
        add(total, head);

        for (j=head; j >= 0; j--) 
            *(factorial + j) = total[j] + '0';

        *(factorial + j) = '\0';
    }

    for (i=0, answer=0; i < FACTORIAL_BUFFER; i++) {
        j = *(factorial + i) - '0';      
        answer += j;
    }

    free(factorial);
    free(current);

    stop = clock();    
    printf("Answer: %d\n", answer);
    printf("Time: %f\n", ((float) stop - (float) start) / CLOCKS_PER_SEC);

    return 0;
}
