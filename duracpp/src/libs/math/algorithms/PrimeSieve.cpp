
#include <iostream>
#include <vector>
#include <chrono>

// Sieve of Eratosthenes
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int upper;

    std::cout << "Welcome to the Prime Checker!" << std::endl;
    std::cout << "Enter the upper bound:" << std::endl;
    std::cin >> upper;

    auto start = std::chrono::high_resolution_clock::now();

    std::vector<bool> is_prime(upper, true);
    is_prime[0] = false;
    is_prime[1] = false;

    for (int i = 2; i * i < upper; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j < upper; j += i) {
                is_prime[j] = false;
            }
        }
    }

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    for (int i = 2; i < upper; ++i) {
        if (is_prime[i]) {
            std::cout << i << "\n";
        }
    }

    std::cout << "Time taken" << duration.count() << "ms" << std::endl;
    return 0;
}
