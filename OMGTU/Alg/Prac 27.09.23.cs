// Практика за 27.09.23

using System;
class Program
{
    static void Main()
    {
        int n, a1, a2, sm = 0, d = 10000000;
        n = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine("Введите первое число пары");
            a1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите второе число пары");
            a2 = Convert.ToInt32(Console.ReadLine());
            sm += Math.Max(a1, a2);
            d = Math.Min(Math.Abs(a1-a2),d);
        }
        if (sm % 3 == 0)
        {
            Console.WriteLine("Максимальная сумма элементов, кратных 3: " + sm);
        }
        else
        {
            sm -= d;
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
}