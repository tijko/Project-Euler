#define _GNU_SOURCE

#include <math.h>
#include <time.h>
#include <stdio.h>
#include <errno.h>
#include <sched.h>
#include <unistd.h>
#include <stdlib.h>

#define NANO pow(10, 9)


int is_prime(int value)
{
    if (value == 2)
        return 1;
    else if (value < 2 || value % 2 == 0)
        return 0;

    int limit = (int) sqrt(value) + 1;

    for (int i=3; i < limit; i+=2)
        if (value % i == 0) return 0;
    return 1;
} 
    
static inline void iso_proc_cpu(void)
{
    pid_t pid = getpid();

    cpu_set_t cpu;
    CPU_ZERO(&cpu);
    CPU_SET(0, &cpu);

    if (sched_setaffinity(pid, sizeof(cpu), &cpu) < 0)
        perror("sched_setaffinity");
}

float timeit(void)
{
    struct timespec tm_spec;
    if (clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &tm_spec) < 0)
        perror("clock_gettime");

    float time = (float) tm_spec.tv_sec + (float) tm_spec.tv_nsec / NANO;
    return time;
}
