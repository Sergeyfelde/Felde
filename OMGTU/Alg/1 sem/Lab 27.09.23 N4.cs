﻿// Л/Р задача 4 27.09.23

using System;
class Program
{
    static void Main()
    {
        int n, a, b = 0, l = 0;
        n = Convert.ToInt32(Console.ReadLine());
        int mnl = n;
        for (int i = 0; i < n; i++)
        {
            a = Convert.ToInt32(Console.ReadLine());
            if (a < 0)
            {
                if (b == 0)
                {
                    l += 1;
                }
                else
                {
                    l = 1;
                    b = 0;
                }
                if (i == n - 1)
                {
                    mnl = Math.Min(mnl, l);
                }
            }
            else
            {
                if (i != 0)
                {
                    b = a;
                    mnl = Math.Min(mnl, l);
                }
            }
        }
        Console.WriteLine(mnl);
    }
}
