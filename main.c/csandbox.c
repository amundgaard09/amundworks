
#include <stdio.h>

int a, b;

int add(int x, int y) {
    return x + y;
}
int subtract(int x, int y) {
    return x - y;
}
int multiply(int x, int y) {
    return x * y;
}
double divide(int x, int y) {
    if (y == 0) {
        printf("Error: Division by zero\n");
        return 0;
    }
    else {
        return (double)x / y;
    }
}

int main() {
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    printf("Addition: %d\n", add(a, b));
    printf("Subtraction: %d\n", subtract(a, b));
    printf("Multiplication: %d\n", multiply(a, b));
    printf("Division: %.2f\n", divide(a, b));
    return 0;
}