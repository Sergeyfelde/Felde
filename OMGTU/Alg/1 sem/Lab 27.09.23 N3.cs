﻿// Л/Р задача 3 27.09.23

using System;
class Program
{
    static void Main()
    {
        int n, a1 = 0, a2, l = 1, mxl = 1;
        n = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            if (i == 0)
            {
                a1 = Convert.ToInt32(Console.ReadLine());
            } else
            {
                a2 = Convert.ToInt32(Console.ReadLine());
                if (a1 == a2)
                {
                    l += 1;
                    mxl = Math.Max(l, mxl);
                } else 
                {
                    l = 1;
                }
                a1 = a2;
            }
        }
        Console.WriteLine(mxl);
    }
}
