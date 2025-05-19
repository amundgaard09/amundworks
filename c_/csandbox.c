
#include <stdio.h>

int a, b;
a = 6;
b = 5;

int add(a, b) {
    return a+b;
}
int main() {
    printf(add(a,b));
}