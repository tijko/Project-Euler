// Find the number of sundays that fell on the first day of the month in 
// between 1901 - 2000

#include "euler_util.h"


int Months[12] = {31, 00, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31};

int main(int argc, char *argv[])
{
    float start = timeit();

    int answer;
    int year, mos, day, day_num, duration;

    for (answer=0, day_num=0, year=1901; year < 2000; year++) {
        for (mos=0; mos < 12; mos++) {
            if (mos == 1)
                duration = year % 4 == 0 ? 29 : 28;
            else
                duration = Months[mos];

            for (day=0; day <= duration; day++, day_num++)
                if (day == 0 && day_num % 7 == 0)
                    answer++;
        }
    }

    printf("Answer: %d\n", answer);
    float stop = timeit();
    printf("Time: %f\n", stop - start);

    return 0;
}
