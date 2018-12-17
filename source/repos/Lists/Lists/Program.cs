using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Class2PracticeProblems
{
    public class Program
    {
        static void Main(string[] args)
        {
            int avg = AverageofEvenNumbers.Run();
            Console.WriteLine("The average of your list of numbers is " + avg);
            Console.ReadLine();
        }
}
