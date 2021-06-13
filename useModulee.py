#만든 모듈 사용하기(같은폴더에 저장)
#import 파일명
import makeModule
selected = (makeModule.random_rsp())
print(selected)
print('가위?', makeModule.SCISSOR == selected)