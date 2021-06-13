#모듈만들기
def random_rap() : 
  """가위바위보 랜던"""
  import random
  return random.choice(['가위', '바위', '보'])

PAPER = '보'
SCISSOR = '가위'
ROCK = '바위'