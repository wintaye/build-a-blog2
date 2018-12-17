using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CountingCharacters
{
    public static class Program
    {
        static void Main(string[] args)
        {
            string Message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan " +
                "sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus " +
                "justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. " +
                "Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit" +
                " non ligula efficitur luctus.";
            List<char> letters = new List<char>();
            Dictionary<char, int> CharacterIndex = new Dictionary<char, int>();
            //for each char in message if char == letter already in list, ++ dict[letter]
            //else append <letter, count/1>
            //not a do/while loop because don't have an unpredictable # of char
            foreach (char character in Message)
            {
                if (CharacterIndex.ContainsKey(character))
                {
                    CharacterIndex[character]++;
                }
                else
                {
                    CharacterIndex.Add(character, 1);
                }
            }
            foreach (KeyValuePair<char, int> kvp in CharacterIndex)
            {
                string NewMessage = String.Format("Letter:{0}, Count:{1}", kvp.Key, kvp.Value);
                Console.WriteLine(NewMessage);
            }
            Console.ReadLine();
        }

    }
}
