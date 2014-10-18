// Find the maximum total from the top to bottom of the triangle

#include <time.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 3


FILE *tri_file(void)
{
    char *fullpath, *home_path, *triangle_path;
    size_t home_path_len, triangle_path_len, fullpath_len;
    
    home_path = getenv("HOME");
    home_path_len = strlen(home_path);

    triangle_path = "/Project_Euler/euler_txt/triangle1.txt";
    triangle_path_len = strlen(triangle_path);

    fullpath_len = triangle_path_len + home_path_len + 1;
    fullpath = malloc(sizeof(char) * fullpath_len);

    snprintf(fullpath, fullpath_len, "%s%s", home_path, triangle_path);

    return fopen(fullpath, "r"); 
}

int main(int argc, char *argv[])
{
    clock_t start, stop;
    start = clock();

    size_t n;
    int tri_pos;
    int answer, i;
    int digit, pos, high;
    ssize_t line_size;
    char *number, *ln;

    FILE *triangle = tri_file();
    number = malloc(sizeof(char) * MAX);
    memset(number, '0', MAX);

    n = 0;
    digit = 0;    
    answer = 0;
    tri_pos = 1;

    while ((line_size = getline(&ln, &n, triangle)) > 0) {

        for (i=0, pos=0, high=0; i < line_size; i++) {

            if (isspace(*(ln + i))) {
                digit = 0;
                continue;
            }

            *(number + digit++) = *(ln + i);

            if (digit == 2) {
                *(number + digit) = '\0';
                pos++;
            } else {
                continue;
            }

            if (pos == tri_pos) { 
                high = atoi(number);
            } else if (pos == (tri_pos + 1) && high < atoi(number)) {
                high = atoi(number);
                tri_pos++;
                break;
            }    
        }

        answer += high;
    }

    stop = clock();
    printf("Answer: %d\n", answer);
    printf("Time: %f\n", ((float) stop - (float) start) / CLOCKS_PER_SEC);
    return 0;
}
