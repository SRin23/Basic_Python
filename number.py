
#문자열 (사람을 위한 텍스트를 프로그래머가 부르는 방법)
my_name = 'Python'
#숫자
my_age = 25 

#출력
print(my_name, '은 이제', my_age, '살')

#파이썬은 문자보다 숫자에 더 강력하다
my_next_age = my_age + 1
print('내년에는 ', my_next_age, '살 입니다.')

print('\n')

#숫자의 사칙연산
add = 19 + 25    #더하기
minus = 45 - 20   #빼기
multiply = 9 * 9  #곱하기
divide = 30 / 5   #나누기
power = 2 ** 10 #제곱(2의 10제곱)
reminder = 15 % 4 #나머지(15/4의 나머지)

print('19 + 25 = ', add)
print('45 - 20 = ', minus)
print('9 * 9 = ', multiply)
print('30 / 5 = ', divide)
print('2 ** 10 = ', power)
print('15 % 4 = ', reminder)

print('\n')

#문자열의 사칙연산?
text = '2015' + '1991'
number = 2014 + 1991

#문자열에서의 +는 각각의 문자열을 연결하는 용도이다
print('문자 : ', text)
print('숫자 : ', number)
