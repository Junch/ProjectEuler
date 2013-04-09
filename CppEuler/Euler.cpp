#include <algorithm>
#include <iostream>
#include <ctime>

#pragma warning(push)
#pragma warning(disable:4267)
#include <boost/multiprecision/cpp_int.hpp>
#pragma warning(pop)
using boost::multiprecision::cpp_int;

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

int main(int argc, char* argv)
{
    clock_t begin = clock();

    problem_57();

    clock_t end = clock();
    double elapsed_secs = double(end-begin)/CLOCKS_PER_SEC;
    std::cout << "elapsed time=" << elapsed_secs << std::endl;
    std::system("PAUSE");
}