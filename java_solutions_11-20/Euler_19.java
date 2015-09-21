/*
/   Project Euler #19 Counting Sundays
/
/   How many Sundays fell on the first of the month during the twentieth
/   century (Jan 1, 1901 to Dec 31, 2000)?
/
*/


public class Euler_19
{
    public static void main(String[] args)
    {
        int sundayCount = 0;
        int[] mosLengths = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29};

        int curDay = 1;
        int weekLength = 7;
        int yearLength = 12;
        int mosLength = 0;

        for (int yr = 1901; yr < 2001; yr++) 
        {
            for (int mos = 0; mos < yearLength; mos++)
            { 
                int mosDay = 0;

                if (mos == 1 && yr % 4 == 0) 
                    mosLength = mosLengths[12];
                else 
                    mosLength = mosLengths[mos];
                if (curDay == 0)
                    sundayCount++;
 
                while (mosDay < mosLength)
                {
                    for (; curDay < weekLength && mosDay < mosLength; curDay++, mosDay++);
                    if (curDay == weekLength)
                        curDay = 0;
                }
            }
        }

        System.out.printf("Answer: %d\n", sundayCount);
    }
}   
