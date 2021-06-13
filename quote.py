#따옴표
#문자열/string타입을 만듦

string = 'Some text'
string2 = '어떤 텍스트'
string3 = '{}도 {}도 지금 이것도 문자열'.format(string, string2)

print(string, string2, string3)

#""나 ''는 큰차이 없다
quote = '문법 검사기 왈 "직접인용은 큰따옴표다!"'
emphasize = "'문법검사기'를 인용하다니"
#error = "엄마친구아들이 "파이썬이 좋아"라고 했데

#long_string = '이렇게하면
#안되겠지?'

long_string2 = '''이렇게
적으면 여러줄 작성도 괜찮다'''

print(long_string2)

quote1 = "가끔은 '와'" + '"를 모두 쓰기도 한다.'

#"""하나안에 "와 '모두 쓸 수 있음
quote2 = """가끔은 '와 "를 모두 쓰기도 해 """

#하지만 양쪽은 맞추어 주어야한다.
#error = "이렇게 하면 에러가 난다'

#문제1
#string1을 선언하세요.
string1 = """다스베이더가 말했다.
"내가 니 애비다!"
그 말을 들은 루크는 '깜짝' 놀랐다."""

print(string1)