#if문 사용법
#if (조건식) : 
#____(4칸 들여쓰기)실행내용(true일 경우 실행)
#(false일 경우 위 내용 실행하지 않고 바로 여기부터 실행) 다른코드

#사과
people = 3
apple = 20

if people<(apple / 5) : #3<(20/5) -> 3<4
  print('신나는 사과 파티! 배 터지게 먹자!')

if apple % people > 0 : #20%3=2 -> 2>0
  print('사과 수가 맞지 않아! 몇개는 쪼개 먹자!')

if people>apple : #3>20 -> false 실행 안함
  print('사람이 너무 많아 몇명은...')
print('\n')

#True/False
if True:  #bool type으로 true 반환
    print("조건식이 True이면 실행됩니다.")

if False: #bool type으로 false 반환
    print("조건식이 False이면 실행되지 않습니다.")
print('\n')

#대소비교(True, False로 반환))
print('0<10 = ', 0<10)
print('0>10 = ', 0>10)
print('10<=10 = ',10<=10)
print('10>=10 = ', 10>=10)
print('10==20 = ', 10==20)#같다
print('19!=10 = ', 19!=10)
print('\n')

#boolean 연산
#and연산 : 두 조건이 모두 참인지를 체크
print(True and True)
print(True and False)
print('\n')

#or연산 : 두 조건 중 하나라도 참인지 체크
print(True or True)
print(True or False)
print('\n')

#not연산 : true->false로, false->true로 변환하는 연산자
print(not True)
print(not False)

#문제1
#아래 두 줄의 코드는 변수 hour에 현재 시간을 저장합니다.
#이 코드가 어떻게 동작하는지는 이후 강의에서 다룹니다.
from datetime import datetime 
hour = datetime.now().hour

#현재 시간이 12시보다 작을때만 print문을 실행하도록 이 아래줄에 if문을 추가하세요.
if(hour<12) :
    print('오전입니다.')#if문을 추가한 이후 이 줄은 들여쓰기 되어야 합니다.

#문제2
number = 15
if number % 3 == 0: #number가 3의 배수인지 확인합니다.
    print("{}는 3의 배수입니다.".format(number))#이 코드는 실행됩니다.

number = 16
if number % 3 == 0: #number가 3의 배수인지 확인합니다.
    print("{}는 3의 배수입니다.".format(number))#이 코드는 실행되지 않습니다.

#문제3
#아래 두 줄의 코드는 변수 hour에 현재 시간을 저장합니다.
#이 코드가 어떻게 동작하는지는 이후 강의에서 다룹니다.
from datetime import datetime 
hour = datetime.now().hour

#현재 시간이 6의 배수일 때만 print문이 실행되도록 아래줄에 if문을 추가하세요
if hour%6==0 :
    print('종이 울립니다.')#if문을 추가한 이후 이 줄은 들여쓰기 되어야 합니다.