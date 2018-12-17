using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("What's the radius of your circle?");
            string radiusI = Console.ReadLine();
            int areas = AreaofCircle.Area(radiusI);
            Console.WriteLine("The area of your circle is " + areas);
            Console.ReadLine();
        }
    }
}
