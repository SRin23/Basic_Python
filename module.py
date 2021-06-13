#모듈 : 미리 만들어진 코드를 가져와 쓰는 방법
#import 모듈명

import math
r = 10
print(2*math.pi*r)
print(math.ceil(2.5))
print(math.floor(2.5))


import random
candidates = ['가위', '바위', '보']
selected = random.choice(candidates)
print(selected)

#웹사이트의 내용 즉, html을 나타냄
def get_web(url) : 
  """URL을 넣으면 페이지 내용을 올려주는 함수"""
  import urllib.request
  response = urllib.request.urlopen(url)
  data = response.read()
  decoded = data.decode('utf-8')
  return decoded

url = input('웹페이지 주소>')
content = get_web(url)
print(content)

#문제1
print("파이의 값은 {}입니다.".format(math.pi))

#문제2
import datetime
print(datetime.date.today())

#문제 3
list = ["빨","주","노","초","파","남","보"]
random_element = random.choice(list)
print(random_element)

#문제 4
random_number = random.randint(2,5)
print(random_number)

#문제 5
list = ["빨","주","노","초","파","남","보"]
random.shuffle(list)
print(list)