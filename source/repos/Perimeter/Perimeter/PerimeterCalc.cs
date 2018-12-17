using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Perimeter
{
    public class PerimeterCalc
    {
        public static int Run(string lengthInput, string widthInput)
        {
            int length = int.Parse(lengthInput);
            int width = int.Parse(widthInput);
            int message = (2 * length) + (2 * width);
            return message;
        }
    }
}
