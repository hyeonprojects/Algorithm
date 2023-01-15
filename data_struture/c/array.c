#include <stdio.h>

int main() {
    int array[3]; // 정수형 3개의 배열
    int i;

    array[0] = 100;
    array[1] = 200;
    array[2] = 300;

    for (i = 0; i < 3; i++) {
        printf("array[%d] value : %d\n", i, array[i]);
    }

    int array2[] = {4, 1, 6, 2, 46, 62, 46, 3462, 4};

    // C언어는 char 형태로 문자 하나씩만 있고 문자열 형태가 없다
    return 0;
}