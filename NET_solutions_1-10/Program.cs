using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NET_solutions_1_10
{
    class Program
    {
        static void Main(string[] args)
        {
            UInt64 total = 0;
            for (UInt64 i=0; i < 1000; i++)
            {
                if (i % 3 == 0 || i % 5 == 0)
                    total = total + i;
            }

            Console.WriteLine("Answer: {0}\n", (total));
        }
    }
}
