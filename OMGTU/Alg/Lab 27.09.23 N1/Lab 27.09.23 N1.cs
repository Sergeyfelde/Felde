﻿// Л/Р задача 1 27.09.23
class Program
{
    static void Main()
    {
        int n, res = 0, a1 = 0, a2 = 0, a3 = 0;
        n = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            if (i == 0)
            {
                a1 = Convert.ToInt32(Console.ReadLine());
            }
            else
            {
                if (i == 1)
                {
                    a2 = Convert.ToInt32(Console.ReadLine());
                }
                else
                {
                    a3 = Convert.ToInt32(Console.ReadLine());
                    if ((a1 > a2) && (a2 < a3))
                    {
                        res += 1;

                    }
                    a1 = a2; a2 = a3;
                }

            }

        }
        Console.WriteLine(res);
    }
}