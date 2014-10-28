// Name Scores -> order the words listed in the word file alphabetically
// then tally the score based on order rank word total.

#include <time.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_NAMES 6000
#define MAX_NAME 15
#define BASE_PATH(name) ((getenv(name)))
#define NAME_PATH "/Project_Euler/euler_txt/names1.txt"

#define MIN_NAME_LEN(name1, name2) (strlen(name1) >= strlen(name2)) ? \
                                        strlen(name2) : strlen(name1)


struct Name_Info {
    char *name;
    int score;
    int position;
};

int load_names(struct Name_Info *name_list[])
{
    FILE *name_file;
    char *path, *home, *ln, *name;
    size_t path_length, ln_length, n;
    int i, name_count, name_letter, j;
 
    home = BASE_PATH("HOME");
    path_length = strlen(home) + 1 + strlen(NAME_PATH) + 1;
    path = malloc(sizeof(char) * path_length + 1);
    snprintf(path, path_length, "%s%s", home, NAME_PATH);

    name_file = fopen(path, "r");
    if (name_file == NULL)
        perror("<fopen>");

    n = 0;
    name = malloc(sizeof(char) * MAX_NAME);

    while ((ln_length = getline(&ln, &n, name_file) > 0)) {
        for (i=0, name_count=0, name_letter=0; i < strlen(ln); i++) {
            if (isalpha(*(ln + i))) {
                *(name + name_letter) = *(ln + i);
                name_letter++;
            } else if (*(ln + i) == ',') {
                *(name + name_letter) = '\0'; 
                name_letter = 0;
                name_list[name_count] = malloc(sizeof(struct Name_Info));
                for (j=0; j < strlen(name); j++)
                    name_list[name_count]->score += ((*(name + j) - '0') - 16);
                name_list[name_count]->name = malloc(sizeof(char) * strlen(name) + 1);
                memcpy(name_list[name_count]->name, name, strlen(name) + 1);
                name_count++;
            }
        }
    }

    free(path);
    free(name);
    fclose(name_file);
    
    return name_count;
}

int min_alpha(char *name1, char *name2)
{
    int i;
    for (i=0; i < MIN_NAME_LEN(name1, name2); i++) {
        if ((*(name1 + i) - '0') < (*(name2 + i) - '0')) 
            return 1;
        else if ((*(name1 + i) - '0') > (*(name2 + i) - '0')) 
            return 2;
    }

    i = MIN_NAME_LEN(name1, name2) == strlen(name1) ? 1 : 2;
    return i;
}

void sort_name_list(struct Name_Info *name_list[], int length)
{
    struct Name_Info *curr;

    int i, j;
    for (i=0; i < length; i++) {
        curr = name_list[i];
        j = i - 1;
        while (j >= 0 && min_alpha(curr->name, name_list[j]->name) == 1) {
            name_list[j + 1] = name_list[j];
            j--;
        }
        name_list[j + 1] = curr;
    }
}

void free_list(struct Name_Info *name_list[], int length)
{
    int i;
    for (i=0; i < length; i++) {
        free(name_list[i]->name);
        free(name_list[i]);
    }
}

int main(int argc, char *argv[])
{

    clock_t start, stop;
    int total, i;
    long answer;
    struct Name_Info *name_list[MAX_NAMES];

    start = clock();

    total = load_names(name_list);
    sort_name_list(name_list, total);

    i = 0;
    answer = 0;
    while (i < total) {
        answer += (name_list[i]->score * (i + 1));
        i++;
    }

    stop = clock();

    printf("Answer: %ld\n", answer);
    printf("Time: %f\n", ((float) stop - (float) start) / CLOCKS_PER_SEC);

    return 0;
}
