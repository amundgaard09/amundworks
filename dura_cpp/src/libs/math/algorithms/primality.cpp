
#include <vector>
#include "primality.hpp"

// Check if `Number` is prime
// Uses trial division to check for factors of `Number` up to the square root of `Number`.
bool isprime(int n) {
    if (n <= 1) {
        return false;
    }

    for (int i = 2; i * i < n; ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

std::vector<int> primefactorize(int n) {
    std::vector<int> factors;
    int div = 2;

    if (n <= 1) return factors;

    while (div * div <= n) {
        while (n % div == 0) {
            factors.push_back(div);
            n /= div;
        }
        div++;
    }

    if (n > 1) { factors.push_back(n); }
    return factors;
}
