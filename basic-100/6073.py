'''
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

[입력예시]
5

[출력예시]
4
3
2
1
0
'''

start_num = int(input())
while start_num > 0:
    start_num -= 1
    print(start_num)