'''
정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

[입력]
정수 1개가 입력된다.
(0 ~ 100)

[출력]
0부터 그 수까지 줄을 바꿔 한 개씩 출력한다.

[입력예시]
4

[출력예시]
0
1
2
3
4
'''

num = int(input())
diff = num

while num-diff <= num:
    print(num - diff)
    diff -= 1