﻿// Л/Р задача 2 27.09.23 Выполнено вместе с Максимом Мельниковым на паре
class Program
{
    static void Main()
    {
        int n, a = 0, b = 0, res = 0;
        n = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            if (i == 0)
            {
                a = Convert.ToInt32(Console.ReadLine());
                continue;
            }
            if (i % 2 == 0)
            {
                a = Convert.ToInt32((Console.ReadLine()));
                if ((a*b) <0)
                {
                    res += 1;
                }
            } else
            {
                b = Convert.ToInt32((Console.ReadLine()));
                if ((a*b) <0)
                {
                    res += 1;
                }
            }    
        }
        Console.WriteLine(res);
    }
}
