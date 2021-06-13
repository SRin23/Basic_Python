#0, 1, 2, 3, 4를 순서대로 출력하려면?
for i in [0, 1, 2, 3, 4] : 
  print(i)

for i in range(10) : #0, 1, 2, 3, 4, 5, 6, ,7, 8, 9
  print(i)

names = ['철수', '영희', '바둑이', '심청이', '흥부']
for i in range(len(names)) : 
  name = names[i]
  print('{}번 : {}'.format(i + 1, name))

#enumerate사용시 한번에 순서와 리스트의 값을 전달함
#list가 있는 경우 enumerate를 사용하는게 더 용이함
for i, name in enumerate(names) : 
  print('{}번 : {}'.format(i, name))

for i in range(11172) : 
  #0~11172까지를 i에 대입
  print(chr(44032 + i), end = ' ')


#for~in list : 순회할 리스트가 정해져 있을때
#for~in range : 순회할 횟수가 정해져 있을때

#문제 1
for i in range(4) :
  print(i)

#문제 2
rainbow=["빨","주","노","초","파","남","보"]
for i in range(len(rainbow) :
    color = rainbow[i]
    print('{}번째 색은 {}'.format(i+1,color))

#문제 3
rainbow=["빨","주","노","초","파","남","보"]
for i,color in enumerate(rainbow):
    print('{}번째 색은 {}'.format(i+1,color))

#문제 4
days = [31,29,31,30,31,30,31,31,30,31,30,31]

for i, day in enumerate(days) :
    print('{}월의 날짜수는 {}일 입니다.'.format(i + 1, day))

for i in range(len(days)) :
    print('{}월의 날짜수는 {}일 입니다.'.format(i + 1, days[i]))