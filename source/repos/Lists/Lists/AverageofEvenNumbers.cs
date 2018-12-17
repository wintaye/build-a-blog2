using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lists
{
    public class AverageofEvenNumbers
    {
        public static int Run
            {
                List<int> ListofNumbers = new List<int>();
                List<int> EvenNumbers = new List<int>();
                string NewNumber;
                int sum;
                Console.WriteLine("Keep entering numbers until your fingers fall off or hit 'Enter' when done.");
                do
                {
                    NewNumber = Console.ReadLine();
                    if (NewNumber != "")
                    {
                        int NumberToAdd = int.Parse(NewNumber);
                        ListofNumbers.Add(NumberToAdd);
                    }
                }
                while (NewNumber != "");
                foreach (int i in ListofNumbers)
                {
                    if (i % 2 == 0)
                    {
                        EvenNumbers.Add(i);
                    }
                }
                sum = EvenNumbers.Sum();
                int avg = sum / ListofNumbers.Count;
            }
        }
    }
}
