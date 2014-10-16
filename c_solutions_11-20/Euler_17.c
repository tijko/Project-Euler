// 
//    Count all the letters that are needed to write out the words from one to 
//    one thousand.
//

#include <time.h>
#include <stdio.h>
#include <string.h>


int main(int argc, char *argv[])
{
    clock_t start, stop;

    start = clock();

    int count_to = 1000;
    int letter_count = 0;
    int tens_offset = 2;
    char *number_words[4][9] = {{"one", "two", "three", "four", 
                                  "five", "six", "seven", "eight", "nine"},
                                 {"twenty", "thirty", "forty", "fifty", 
                                  "sixty", "seventy", "eighty", "ninety"},
                                 {"hundred", "hundredand"}, {"thousand"}};
 
    char *tens[10] = {"ten", "eleven", "twelve", "thirteen", "fourteen", 
                      "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};

    int i, tmp;
    for (i=1; i <= count_to; i++) {
        if (i / 1000) {
            letter_count += strlen(number_words[0][(i / 1000) - 1]);
            letter_count += strlen(number_words[3][0]);
        } else if (i / 100) {
            letter_count += strlen(number_words[0][(i / 100) - 1]);
            if (i % 10) {
                letter_count += strlen(number_words[2][1]);
                tmp = i % 100;
                if (tmp / 10 == 1) {
                    letter_count += strlen(tens[(tmp % 10) - 1]);
                } else {
                    letter_count += strlen(number_words[1][(tmp / 10) - tens_offset]);
                }
                if (tmp % 10)
                    letter_count += strlen(number_words[0][(tmp % 10) - 1]);
            } else {
                letter_count += strlen(number_words[2][0]);
            }
        } else if (i / 10) {
            if (i / 10 == 1) {
                letter_count += strlen(tens[i % 10]);
            } else {
                letter_count += strlen(number_words[1][(i / 10) - tens_offset]);
                if (i % 10)
                    letter_count += strlen(number_words[0][(i % 10) - 1]);
            }
        } else {
            letter_count += strlen(number_words[0][(i % 10) - 1]);
        }
    }
   
    stop = clock();
    printf("Answer: %d\n", letter_count);
    printf("Time: %f\n", ((float) stop - (float) start) / CLOCKS_PER_SEC);
 
    return 0;
}
