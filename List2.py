#리스트 수정하기

list2 = [37, 23, 10, 33, 29, 40]
print(list2)

#list에 값 추가
#방법1(.append사용) -> 배열 맨 뒤에 추가 -> 배열 자체 변화
list2.append(16)
print(list2)

#방법2(new list = list + 추가할 값)
list3 = list2 + [16]
print(list3)

list4 = list2 + list3
print(list4)


#배열 내부에 값이 있는지 확인(in)
n = 12
ownership = n in list3
print(ownership) #true/false

n = 10
if n in list3 : 
  print("{}은 있어!".format(n))

#배열 값 삭제하기
#방법 1(del 리스트명[리스트인덱스]) -> 그 인덱스에 해당하는 값 삭제
del list4[12]
print(list4)

#방법 2(리스트명.remomve(값)) -> 괄호 내부의 값과 같은 리스트 내부의 값 삭제
#단, 중복값이 있을시 가장 앞의 값만 삭제됨 
list4.remove(49)
print(list4)


#문제1
list1=[1,2,3]
#이 곳에 4를 추가하는 코드를 입력해 보세요.
list1.append(4)

print(list1)

#문제2
list1=[1,2,3]
list2=[4,5,6]
list3 = list1 + list2
print(list3)

#문제3
numbers = [1,2,3,4,5]
if 5 in numbers :
  print("5가 있다")

#문제 4
list1=[1,2,3]
del list1[1]

print(list1)
