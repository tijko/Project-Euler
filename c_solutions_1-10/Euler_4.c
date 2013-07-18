#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


int main(void) {

    clock_t start;
    clock_t stop;

    start = clock();

    unsigned long high = 0;    
    unsigned long canidate;

    int x,y;
    for (x=100; x < 1000; x++) {
        for (y=100; y < 1000; y++) {

            canidate = x * y;
            char int_str[BUFSIZ];
            sprintf (int_str, "%d", canidate);

            size_t int_len = strlen (int_str);
            int str_len = int_len - 1;
            char *palindrome = malloc (sizeof(int_str));

            int i;
            for (i=0; i < int_len; i++, str_len--) {
                palindrome[i] = int_str[str_len];
            }        
            if (strcmp (int_str, palindrome) == 0 && atoi (palindrome) > high) {
                high = atoi (palindrome);
            }
            free (palindrome);
        }
    }

    stop = clock();
    printf ("Answer: %ld\n", high);
    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);
    return 0;
}


