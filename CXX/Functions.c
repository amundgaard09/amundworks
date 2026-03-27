
#include <stdio.h>
#include <stdint.h>

// recursive functions

uint64_t factorial(int i) {
    if (i == 0 || i == 1) {
        return 1;
    } else {
        return (i * factorial(i - 1));
    }
}
uint64_t fibonacci(int i) {
    if (i==0) {
        return 0;
    } else if (i==1) {
        return 1;
    } else {
    return fibonacci(i-1) + fibonacci(i-2);
    }
}

int main() {
    int f1, f2;

    printf("Enter factorial: ");
    scanf("%d", &f1);
    printf("Enter fibonacci: ");
    scanf("%d", &f2);

    printf("%llu, %llu", factorial(f1), fibonacci(f2));
}