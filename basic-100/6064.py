'''
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.
'''
a, b, c = map(int, input().split())
min_between_ab = a if a < b else b
print(min_between_ab if min_between_ab < c else c)