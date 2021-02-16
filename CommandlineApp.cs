using System;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            // Ask the user to choose an option.
            Console.WriteLine("Choose an option from the following list:");
            Console.WriteLine("\t1 - De kleine Zeemeermin");
            Console.WriteLine("\t2 - Scarface");
            Console.WriteLine("\t3 - Zwartlicht");
            Console.WriteLine("\t4 - Documentaire, Blood Diamond");
            Console.Write("Your option? ");

            // Use a switch statement to do the math.
            switch (Console.ReadLine())
            {
                case "1":
                    Console.WriteLine($"  ");
                    break;
                case "2":
                    Console.WriteLine($"  ");
                    break;
                case "3":
                    Console.WriteLine($"  " );
                    break;
                case "4":
                    Console.WriteLine($"  ");
                    break;
            }
            // Wait for the user to respond before closing.
            Console.Write("Press any key to close the Cinema console app...");
            Console.ReadKey();
        }
    }
}
