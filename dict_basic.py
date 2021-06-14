#dictionary
#여러 값을 저장해두고 필요한 값을 꺼내 쓰는 기능
#이릉표를 이용하여 값을 꺼내 사용
"""
딕셔너리명 = {
  '이름표1' : '값1', 
  '이름표2' : '값2'
}
"""
wintable = {
  '가위' : '보',
  '바위' : '가위',
  '보' : '바위'
}

def rsp(mine, yours) : 
  if mine == yours : 
    return 'draw'
  elif wintable[mine] == yours :
    return 'win'
  else : 
    return 'lose'

result = rsp('가위', '바위')
print(result)
print(wintable['가위'])

message = {
  'win' : '이겼다',
  'draw' : '비겼다', 
  'lose;' : '졌다'
}
print(message[result])

#list
words = ['a', 'b', 'c']
print(words[1])

#문제1
days_in_month = {
    #여기에 코드를 완성해 보세요.
    '1월' : 31, 
    '2월' : 28,
    '3월' : 31    
 }

print(days_in_month)

#문제2
#            ↓ 이름표는 문자열 또는 숫자를 주로 사용하지만
dict = {     "이름표"    :    [1,2,3] }
#                           ↑ 값은 리스트를 포함해서 무엇이든 올 수 있습니다.

print( dict["이름표"] )