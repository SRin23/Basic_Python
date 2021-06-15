#함수 정의
#함수 정의 시 추가로 전달받을 매개변수를 함께 정의할 수 있다. 
#매개변수여러개 구분시 ,(콤마)로 연결/ 매개변수와 실행인자이 개수는 같아야한다.
#괄호 내부(매개변수)
# a = x, b = y, c = z
def print_sqrt(a, b, c) :
  r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5)/(2 * a)
  r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5)/(2 * a)

  print('해는 {} 또는 {}'.format(r1, r2))

x = 2
y = -6
z = -8

#함수 사용
#괄호 내부(실행인자))
print_sqrt(x, y, z)

#반올림 함수
def print_round(number) : 
  rounded = round(number)
  print(rounded)

#괄호 내부에는 변수, 정수, 문자열 등 다양하게 들어갈 수 있다
print_round(4.6)
print_round(2.2)
print_round(-3.7)

#문제 1
def add(a,b):
    #함수 add에서 a와 b를 입력받아서 두 값을 더한 값을 result에 저장하고 출력하도록 만들어 보세요.
    result =  a + b
    print( "{} + {} = {}".format(a,b,result) )#print문은 수정하지 마세요.

add(10,5)