#format

#인사로봇
number = 20
greeting = '안녕하세요'
place = '문자열 포멧의 세계'
welcome = '환영합니다.'

#old way
print(number, '번 손님 ', greeting, '. ', 'place', '에 오신 것을 ', welcome) 

#new way
base = '{}번 손님 {}. {}에 오신것을 {}!'
new_way = base.format(number, greeting, place, welcome)

print(base)
print(new_way)

mine = '가위'
yours = '바위'
result = '졌다'

print('나는 {}, 너는 {}, 그래서 결과는 {}'. format(mine, yours, result))

#{}이 2개, format의 괄호안에 든 변수는 3개 -> 에러 발생 X, 앞에 2개 차레로 대입, 맨뒤는 버림
#{}이 4개, format의 괄호 안에 든 변수는 3개 -> 에러발생

#문제1
name = '토마토'
color = '빨간색'
print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))