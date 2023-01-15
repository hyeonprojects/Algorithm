#include <stdio.h>
#include <limits.h>
#include <stdint.h>
#include <float.h>

int main() {
    const int co1 = 10;
    int num1 = 0;
    int size;

    size = sizeof num1;

    printf("num1 : %d\n", size);
    return 0;
}
