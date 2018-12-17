using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Perimeter
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //need input for length, width, create Class to handle computation
            Console.WriteLine("Length?");
            string lengthInput = Console.ReadLine();
            Console.WriteLine("Width?");
            string widthInput = Console.ReadLine();
            int perimeter = PerimeterCalc.Run(lengthInput, widthInput);
            Console.WriteLine(perimeter);
            Console.ReadLine();
                                                            
        }
    }
}
