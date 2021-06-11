
def root(a, b, c) :
  r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5)/(2 * a)
  r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5)/(2 * a)

  #python에서는 여러개의 값을 한번에 return이 가능하다
  return r1, r2

x = 2
y = -6
z = -8

#return값의 개수에 따라 변수 개수를 똑같이 주어야한다.
r1, r2 = root(x, y, z)
print('근은 {}'.format(r1, r2))

#문제 1
def add(a, b) :
    return a+b