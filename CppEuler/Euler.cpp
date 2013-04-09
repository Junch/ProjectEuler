#include <algorithm>
#include <iostream>
#include <ctime>
#include <boost/format.hpp>

//#pragma warning(push)
//#pragma warning(disable:4267)
//#include <boost/multiprecision/cpp_int.hpp>
//#pragma warning(pop)
//using boost::multiprecision::cpp_int;

#define cpp_int unsigned long long

void problem_57()
{
    auto digits=[](cpp_int n) -> int {
        int count = 0;
        do {
            count++;
            n = n/10;
        }while(n > 0);

        return count;
    };

    int count = 0;
    cpp_int n=1, d=1;
    for (int i=0; i<1000; ++i) {
        cpp_int t = n + d;
        n = t + d;
        d = t;
        int ndigit = digits(n);
        int ddigit = digits(d);

        if (ndigit > ddigit)
            ++count;
    }

    std::cout << "n=" << n << std::endl;
    std::cout << "d=" << d << std::endl;
    std::cout << "count=" << count << std::endl;
}

void problem_58()
{
    auto prime=[](cpp_int n)->bool {
        if (n < 2)
            return false;

        for (cpp_int i = 2; i*i < n + 1; i++)
            if (n % i == 0)
                return false;
        return true;
    };

    cpp_int n = 0;
    int nCount = 1;
    int nPrime = 0;
    while(true)
    {
        ++n;
        cpp_int rt = 4*n*n - 2*n + 1; // right top
        cpp_int lt = rt + 2*n; // left top
        cpp_int lb = lt + 2*n; // left below
        cpp_int rb = lb + 2*n; // left right

        if (prime(rt)) ++nPrime;
        if (prime(lt)) ++nPrime;
        if (prime(lb)) ++nPrime;
        if (prime(rb)) ++nPrime;

        nCount += 4;

        double rate = double(nPrime)/nCount;
        if (rate < 0.1f)
            break;
    }

    std::cout << boost::format("side length=%1%")%(2*n+1)<< std::endl;
}

int main(int argc, char* argv)
{
    clock_t begin = clock();

    //problem_57(); // This one must use the big integer
    problem_58();

    clock_t end = clock();
    double elapsed_secs = double(end-begin)/CLOCKS_PER_SEC;
    std::cout << "elapsed time=" << elapsed_secs << std::endl;
    std::system("PAUSE");
}