//
// Created by hyeonproject on 2023-01-12.
//

#ifndef ALGORITHM_LIBS_H
#define ALGORITHM_LIBS_H


// 구조체

// 자료구조 관련

// Linked List

// Node 구현
typedef struct node {
    int val;
    struct  node *next;
} node_t;



// Palindrome 팰린드롬 : 꺼꾸로 읽어도 똑같은 문장이나 단어를 뜻함.
// 팰린드롬 체크 하는 함수
// inlcude list: string.h,
bool isPalindrome(char word[]);

// 이진 탐색

// 

#endif; //ALGORITHM_LIBS_H
