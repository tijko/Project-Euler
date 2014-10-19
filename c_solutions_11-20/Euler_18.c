// Find the maximum total from the top to bottom of the triangle

#include <time.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_NUM 3
#define MAX_ROW 15
#define MAX_COL 16

#define MAX(x, y) ((x) > (y) ? (x) : (y))


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

void load_array(FILE *triangle_file, int triangle[MAX_ROW][MAX_COL])
{
    size_t n;
    ssize_t line_size;
    char *number, *ln;

    number = malloc(sizeof(char) * MAX_NUM);
    memset(number, '0', MAX_NUM);

    int i, row, col, digit;
    row = 0;

    for (i=0; i < MAX_ROW; i++)
        memset(triangle[i], -1, sizeof(int) * MAX_COL);

    digit = 0;
    while ((line_size = getline(&ln, &n, triangle_file)) > 0) {
        for (i=0, col=0; i < line_size; i++) {
            if (isspace(*(ln + i))) {
                digit = 0;
                continue;
            }

            *(number + digit++) = *(ln + i);

            if (digit == 2) {
                *(number + digit) = '\0';
                triangle[row][col++] = atoi(number);
            } else {
                continue;
            }
        }
        ++row;
    }
}

int main(int argc, char *argv[])
{
    clock_t start, stop;
    start = clock();

    int answer, row, col;
    int triangle[MAX_ROW][MAX_COL];

    FILE *triangle_file = tri_file();
    load_array(triangle_file, triangle);

    answer = 0; 
    row = 0;
    col = 0;
    while (row < MAX_ROW - 2) {
        answer += triangle[row][col];

        col += triangle[row + 1][col] + MAX(triangle[row + 2][col], 
                                            triangle[row + 2][col + 1]) > 
               triangle[row + 1][col + 1] + MAX(triangle[row + 2][col + 1], 
                                                triangle[row + 2][col + 2]) ? 
                                                                       0 : 1;

        ++row;

    }
    answer += triangle[row][col];
    answer += MAX(triangle[row + 1][col], triangle[row + 1][col + 1]);

    stop = clock();
    printf("Answer: %d\n", answer);
    printf("Time: %f\n", ((float) stop - (float) start) / CLOCKS_PER_SEC);
    return 0;
}
