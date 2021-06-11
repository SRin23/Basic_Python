#if~else구문으로 가위바위보 게임 만들기
#else : if의 조건이 맞지 않은 경우 항상 실행
#반드시 if뒤에 나와야한다.
SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼다'
DRAW = '비겼다'
LOSE = '졌다ㅠㅜ'

mine = SCISSOR
yours = ROCK

if mine==yours : 
  result = DRAW

else : 
  if mine == SCISSOR : 
    if yours == ROCK : 
      result = LOSE
    else : 
      result = WIN
  else : 
    if mine == ROCK : 
      if yours == PAPER : 
        result = LOSE
      else :
        result = WIN
    else :
      if mine == PAPER :
        if yours == SCISSOR : 
          result = LOSE
        else : 
          result = WIN
      else : 
        print('이상해요')

# elif -> else + if
#조건이 맞지 않는 경우 다른 경우를 검사
#if~else구문과 기능의 차이가 아닌, 보이는 것의 차이
if mine==yours : 
  result = DRAW

else : 
  if mine == SCISSOR : 
    if yours == ROCK : 
      result = LOSE
    else : 
      result = WIN
  elif mine == ROCK : 
    if yours == PAPER : 
      result = LOSE
    else :
      result = WIN
  elif mine == PAPER :
    if yours == SCISSOR : 
      result = LOSE
    else : 
      result = WIN
  else : 
    print('이상해요')


#문제 1. 
mine = '가위'
yours = '바위'
if mine == yours:
    print("비겼습니다.")
#이 아래줄에 else문을 추가해서 비기지 않은 경우에만 아래 print문이 실행되도록 만들어 보세요
else : 
    print("비기지 않았습니다.")#else문이 추가되고 나면 이 줄은 들여쓰기 되어야 합니다.

#문제 2
gender = "남자"
#이 아래줄에 if문을 추가하세요
if gender == "남자" : 
    print("남자입니다.")
#이 아래줄에 elif문을 추가하세요
elif gender == "여자" : 
    print("여자입니다.")
#이 아래줄에 else문을 추가하세요
else : 
    print("논바이너리입니다")