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
    char *number_words[5][10] = {{"", "one", "two", "three", "four", 
                                  "five", "six", "seven", "eight", "nine"},
                                 {"ten", "eleven", "twelve", "thirteen", 
                                  "fourteen", "fifteen", "sixteen", 
                                  "seventeen", "eighteen", "nineteen"},
                                 {"twenty", "thirty", "forty", "fifty", 
                                  "sixty", "seventy", "eighty", "ninety"},
                                 {"", "hundred", "hundredand"}, {"", "thousand"}};
 

    int i, current;
    for (i=1, current=i; i <= count_to;  i++, current=i) {

        letter_count += strlen(number_words[0][current / 1000]);
        letter_count += strlen(number_words[4][current / 1000]);

        current %= 1000;
        
        letter_count += current / 100 > 0 ? current % 100 > 0 ? strlen(number_words[0][current / 100]) + 
                                                                strlen(number_words[3][2]) : 
                                                                strlen(number_words[0][current / 100]) +
                                                                strlen(number_words[3][1]) :
                                                                strlen(number_words[3][0]);
        
        current %= 100;

        letter_count += current / 10 > 0 ? current / 10 == 1 ? strlen(number_words[1][current % 10]) :
                                           strlen(number_words[2][(current / 10) - tens_offset]) + 
                                           strlen(number_words[0][current % 10]) :
                                           strlen(number_words[0][current % 10]);
    }
   
    stop = clock();
    printf("Answer: %d\n", letter_count);
    printf("Time: %f\n", ((float) stop - (float) start) / CLOCKS_PER_SEC);
 
    return 0;
}
