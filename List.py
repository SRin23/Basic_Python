list1 = ['가위', '바위', '보']
list2 = [27, 23, 15, 26, 74, 85]

print(list1)
print(list2)

#첫번쨰에 있는 값을 가져오고 싶다면 [0]을 사용해야한다.
#프로그램에서는 숫자가 1대신에 0부터 시작하는게 대다수이다.
#list의 첫번째 인덱스는 0부터 시작한다.
print(list1[0])
print(list1[1])
print(list1[2])
#print(list1[3]) #범위 벗어남

#값 수정
list[0] = '바위'
print(list1[0])
print(list1)

#리스트 가장 마지막(뒤에서 첫번째)
print(list1[-1]) #보
print(list1[-2]) #바위
print(list1[-3]) #바위
#print(list1[-4]) #범위 벗어남

#문제1
rainbow=['빨강','주황','노랑','초록','파랑','남색','보라']
#rainbow를 이용해서 first_color에 값을 저장하세요
#첫번째 값은 0부터 시작합니다.
first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color) )