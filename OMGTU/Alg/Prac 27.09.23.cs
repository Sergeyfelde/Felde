// Практика за 27.09.23

using System;
class Program
{
    static void Main()
    {
        int n, a1, a2, sm = 0, d11 = 10000000, d2 = 10000000, d12 = 10000000, k = 0;
        n = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine("Введите первое число пары");
            a1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите второе число пары");
            a2 = Convert.ToInt32(Console.ReadLine());
            sm += Math.Max(a1, a2);
            if (Math.Abs(a1 - a2) % 3 == 1)
            {
                if (Math.Abs(a1 - a2) == d11)
                {
                    k += 1;
                }
                if (Math.Abs(a1 - a2) < d11)
                {
                    k = 1;
                    d12 = d11;
                    d11 = Math.Abs(a1 - a2);
                }
            }
            if (Math.Abs(a1 - a2) % 3 == 2)
            {
                d2 = Math.Min(Math.Abs(a1 - a2), d2);
            }

        }
        if (sm % 3 == 0)
        {
            Console.WriteLine("Максимальная сумма элементов, кратная 3: " + sm);
        }
        else
        {
            if (sm % 3 == 1)
            {
                sm -= d11;
            }
            else
            {
                if ((d2 < 10000000)&&(d2 < d11 + d12))
                {
                    sm -= d2;
                }
                else
                {
                    sm -= d11 + d12;
                }
            }
        }
        if (sm % 3 == 0)
        {
            Console.WriteLine("Максимальная сумма элементов, кратных 3: " + sm);
        }
        else
        {
            Console.WriteLine("Найти максимальную сумму элементов, кратную 3 невозможно");
        }
    }
}
