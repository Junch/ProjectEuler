#include <algorithm>
#include <iostream>

#define LLONG long long

LLONG maxdiv(LLONG m, LLONG n)
{
    LLONG a = m % n;
    while (a != 0) {
        m = n;
        n = a;
        a = m % n;
    }

    return n;
}

void normal(LLONG& m, LLONG& n)
{
    LLONG div = maxdiv(m, n);
    m /= div;
    n /= div;
}

int digits(LLONG n)
{
    int count = 0;
    do {
        count++;
        n = n/10;
    }while(n > 0);

    return count;
}

void problem_57()
{
    int count = 0;
    LLONG n=1, d=1;
    for (int i=0; i<1000; ++i)
    {
        LLONG t = n;
        n = t + 2*d;
        d = t + d;
        normal(n,d);
        int ndigit = digits(n);
        int ddigit = digits(d);

        if (ndigit > ddigit)
            ++count;
    }

    std::cout << "n=" << n << " d=" << d << std::endl;
    std::cout << "count=" << count << std::endl;
}

int main(int argc, char* argv)
{
    problem_57();

    std::system("PAUSE");
}