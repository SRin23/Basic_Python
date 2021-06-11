def add_10(value) : 
  """value에 10을 더한 값을 반환하는 함수"""
  #return 10
  #여기에 return을 쓴다면 무조건 10이 반환되고 아래 문제는 실행되지 않는다. -> 바로 함수가 끝남

  #이렇게 특정값에만 바로 함수가 종료되게 할 수 있따.
  if value<10 : 
    return 10
  result = value + 10
  #return은 함수가 실행결과로 값을 갖도록 한다.
  #함수를 호출한 결과를 전해줌
  return result

#n에 add_10에서 반환한 값을 저장함
#함수 사용은 함수안의 코드를 모두 실행 후, n자리에 return에 있는 값을 넣은것과 같다.
n = add_10(42)

print(n)