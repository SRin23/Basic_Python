#정수와 실수

#five1 != five2 == five3
five1 = 5
five2 = 5.0
five3 = 5.0000

print(five1)
print(five2)
print(five3)

#정수만 다룸
five4 = 5 * 1

#실수만 다룸
five5 = 5 * 1.0

print(five4)
print(five5)

#예외 : 나눗셈은 항상 소수로 나온다
print(6/5) #1이 나오려면?
print(10/5)

#나머지는 정수로 나옴
print(6%5)
print(10%5)

#몫만 구하고 싶다면?
print(6//5)
print(10//5)

a = 6 
b = 5
print(a == (a//b) + (a%b)) #a = 몫 + 나머지

#부동소수점은 정확하진 않지만 소수가 필요할 때 사용
print(0.1 + 0.1 == 0.2) #True
print(0.1 + 0.1 + 0.1== 0.3) #False

#정수는 그냥 완전 정확
print(1 + 1 == 2)
print(1 + 1 + 1 == 3)

#형변환
print(int(5.0)) #부동소수점 -> 정수
print(float(5)) #정수 -> 부동소수점
print(5 * 1.0) #부동소수점으로

#문제 1
age = 400
height = 123.4
print('나의 나이는 {}이고, 키는 {}입니다.'.format(age, height))

#문제2(몫구하기)
a=23
b=5

div = a//b

print("변수 div는 {}입니다.".format(div))