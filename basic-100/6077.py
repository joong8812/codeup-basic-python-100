'''
정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

[입력]
정수 1개가 입력된다.
(0 ~ 100)

[출력]
1부터 그 수까지 짝수만 합해 출력한다.

[입력예시]
5

[출력예시]
6
'''
input_num = int(input())
sum = 0

for num in range(0, input_num+1, 2):
    sum += num

print(sum)