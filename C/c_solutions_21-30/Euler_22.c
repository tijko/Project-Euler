// Name Scores -> order the words listed in the word file alphabetically
// then tally the score based on order rank word total.

#include "euler_util.h"

#include <ctype.h>
#include <string.h>

#define SIZE 0x10000
#define MAX_NAMES 6000
#define MAX_NAME 15
#define BASE_PATH(name) ((getenv(name)))
#define NAME_PATH "/Project-Euler/euler_txt/names1.txt"
#define LETTER_SCORE(c) (c - '0') - 16
#define MIN_NAME_LEN(name1, name2) (strlen(name1) >= strlen(name2)) ? \
                                        strlen(name2) : strlen(name1)


FILE *get_file_handle(void)
{
    char *home = BASE_PATH("HOME");
    size_t path_length = strlen(home) + strlen(NAME_PATH) + 1;
    char *path = malloc(sizeof(char) * path_length);
    snprintf(path, path_length, "%s%s", home, NAME_PATH);

    FILE *name_file = fopen(path, "r");
    if (name_file == NULL)
        perror("<fopen>");

    free(path);

    return name_file;
}

int load_names(FILE *fh, char **name_list)
{
    int name_count = 0;
    char *delimiter = "\"";

    char name_entry_buffer[SIZE];
    fread(name_entry_buffer, 1, SIZE, fh);

    char *entry = strtok(name_entry_buffer, delimiter);

    while (entry) {
        if (!strchr(entry, ','))
            name_list[name_count++] = strdup(entry);
        entry = strtok(NULL, delimiter);
    }

    fclose(fh);
    
    return name_count;
}

int min_alpha(char *name1, char *name2)
{
    for (int i=0; i < MIN_NAME_LEN(name1, name2); i++) {
        if ((name1[i] - '0') < (name2[i] - '0'))
            return 1;
        else if ((name1[i] - '0') > (name2[i] - '0'))
            return 2;
    }

    return 0;
}

void sort_name_list(char **name_list, int length)
{
    for (int i=0; i < length; i++) {
        char *curr = name_list[i];
        int j = i - 1;

        while (j >= 0 && min_alpha(curr, name_list[j]) == 1) { 
            name_list[j + 1] = name_list[j];
            j--;
        }

        name_list[j + 1] = curr;
    }
}

static inline void free_list(char **name_list, int length)
{
    for (int i=0; i < length; i++) 
        free(name_list[i]);
    free(name_list);
}

int name_score(char *name)
{
    int score = 0;

    for (int i=0; i < strlen(name); i++)
        score += LETTER_SCORE(name[i]);

    return score;
}

long name_scores_total(char **name_list, int length)
{
    long total = 0;

    for (int idx=0; idx < length; idx++) {
        int score = name_score(name_list[idx]); 
        total += (score * (idx + 1));
    }

    return total;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    char **name_list = calloc(MAX_NAMES, sizeof(char *));

    FILE *fh = get_file_handle();

    int total = load_names(fh, name_list);
    sort_name_list(name_list, total);
    long answer = name_scores_total(name_list, total);

    free_list(name_list, total);

    float stop = timeit();

    printf("Answer: %ld\n", answer);
    printf("Time: %f\n", stop - start);

    return 0;
}
