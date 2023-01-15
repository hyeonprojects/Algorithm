#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

//팰린드롬, 앞뒤 문자를 바꿔도 같은 문자인 경우를 체크함.
//영어 챜팅이 안되는데.
bool isPalindrome(char word[])
{
    int length;                  // 문자열 길이
    bool isPalindrome = true;    // 회문 판별값을 저장할 변수, 초깃값은 true

//    printf("단어를 입력하세요: ");
//    scanf("%s", word);

    length = strlen(word);    // 문자열의 길이를 구함

    // 0부터 문자열 길이의 절반만큼 반복
    for (int i = 0; i < length / 2; i++)
    {
        // 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        if (word[i] != word[length - 1 - i])
        {
            // 회문이 아님
            isPalindrome = false;
            break;
        }
    }

    printf("%d\n", isPalindrome);    // 회문 판별값 출력

    return isPalindrome;
}


