#include <algorithm>
#include <iostream>

int maxdiv(long m, long n)
{
    long a = m % n;
    while (a != 0) {
        m = n;
        n = a;
        a = m % n;
    }

    return n;
}

void normal(long& m, long& n)
{
    long div = maxdiv(m, n);
    m /= div;
    n /= div;
}

void problem_57()
{
    using namespace std;
    typedef pair<long, long> ND;
    ND a(3,2);
    long n = a.first + 2*a.second;
    long d = a.first + a.second;
    normal(n,d);
    cout << n << " " << d << endl;
}

int main(int argc, char* argv)
{
    problem_57();

    std::system("PAUSE");
}