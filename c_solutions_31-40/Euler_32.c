#include "euler_util.h"

#include <string.h>

#define MAX 13 
#define TABLE_SIZE 7000

char pandigital[10];
char *pandigital_string = "123456789";

struct pandigital_entry {
    char *pandigital_str;
    int product;
    struct pandigital_entry *next;
};

unsigned long create_pandigital_hash(char *prime_str)
{
    unsigned long hash = 5381;

    for (char c=*prime_str++; *prime_str; prime_str++)
        hash = ((hash << 5) + hash) + c;

    hash %= TABLE_SIZE;

    return hash;
}

void add_pandigital_entry(struct pandigital_entry **table, char *prime_str,
                          int product, unsigned long hash)
{
    struct pandigital_entry *add_in = table[hash];

    if (!add_in) {
        table[hash] = malloc(sizeof *(table[hash]));
        table[hash]->next = NULL;
        table[hash]->product = product;
        table[hash]->pandigital_str = strdup(prime_str);
        return;
    }

    while (add_in->next && add_in->product != product) 
        add_in = add_in->next; 

    if (add_in->product == product)
        return;

    add_in->next = malloc(sizeof *(add_in->next));
    add_in->next->product = product;
    add_in->next->pandigital_str = strdup(prime_str);
    add_in->next->next = NULL;
}

long total_pandigital_products(struct pandigital_entry **table)
{
    long total = 0;

    for (int i=0; i < TABLE_SIZE; i++) {
        if (table[i]) {
            total += table[i]->product;
            if (table[i]->next) {
                struct pandigital_entry *ent = table[i]->next;
                free(table[i]->pandigital_str);
                free(table[i]);
                while (ent) {
                    total += ent->product;
                    free(ent->pandigital_str);
                    struct pandigital_entry *lst_ent = ent;
                    ent = ent->next;
                    free(lst_ent);
                }
            } else {
                free(table[i]->pandigital_str);
                free(table[i]);
            }
        }
    }

    return total;
}

int is_pandigital(char *prime_string)
{
    memset(pandigital, '0', 9);

    for (int i=0; i < strlen(prime_string); i++)
        pandigital[(prime_string[i] - '0') - 1] = prime_string[i];
    pandigital[9] = '\0';

    return strcmp(pandigital, pandigital_string) == 0 ? 1 : 0;
}

int main(int argc, char *argv[])
{
    float start = timeit();

    struct pandigital_entry **table = calloc(sizeof *table * 7000, sizeof *table);

    char *prime_str = malloc(sizeof(char) * MAX + 1);

    for (int i=2; i < 100; i++) {
        for (int j=100; j < 5000; j++) {
            int product = i * j;
            snprintf(prime_str, MAX, "%d%d%d", product, i, j);
            if (strlen(prime_str) != 9 || strchr(prime_str, '0')) continue;
            if (is_pandigital(prime_str)) {
                unsigned long pandigital_hash = create_pandigital_hash(prime_str);
                add_pandigital_entry(table, prime_str, product, pandigital_hash);
            }
        }
    }

    float stop = timeit();
    printf("Answer: %ld\n", total_pandigital_products(table));
    printf("Time: %f\n", stop - start);
    free(table);
    free(prime_str);

    return 0;
}

