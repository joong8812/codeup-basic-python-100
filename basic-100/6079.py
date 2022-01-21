'''
1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.

즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.

[입력]
정수 1개가 입력된다.

[출력]
1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,
입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.

[입력 예시]
55

[출력 예시]
10
'''

input_num = int(input())
sum = 0
add_num = 0

# for
# for num in range(input_num+1):
#     sum += num
#     if sum >= input_num:
#         print(num)
#         break

# while
while sum < input_num:
    add_num += 1
    sum += add_num
print(add_num)
