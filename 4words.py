import random


# STEP1 : 모듈 import
def update_hint(guess,idiom,hint):
    for i in range(len(idiom)):
        if guess==idiom[i]:
            hint[i]==guess


# STEP2 : 변수 초기화
live=9
heart=u'\u2764'
hint=['?','?','?','?']
result=False
# STEP3 : 사자성어 리스트 만들기
words=["고진감래", "이심전심", "우공이산", "각골난망", "설상가상", "일석이조"]
pst=5
# STEP4 : 사자성어 random 선택
idiom=random.choice(words)
# STEP5 : 게임 시작 코딩하기
while live>0:
    print(hint)
    print('남은 생명'+heart*live)
    guess=input('사자성어를 맞춰보세요(한 글자 or 네 글자):')
# STEP6 : 힌트를 수정하는 함수
    if guess == idiom:
        result=True
        print('정답!(답:{})'.format(idiom))
        words.remove(idiom)
        idiom=random.choice(words)
        print('남은문제:',pst-1)
        continue
    elif guess in idiom and guess != idiom:
        update_hint(guess,idiom,hint)
        print()
    else:
        live-=1
        if live==0:
            print('you are dead. 사자성어:{}'.format(idiom))
            words.remove(idiom)
            idiom=random.choice(words)
            live=9
            print('남은문제:',pst-1)
            if 1==len(words):
                print('game over')
                
                restart=input('restart?(y/n)')
                if restart=='yes':
                    continue
                else:
                    print('game over')
                    break
# STEP7 : 최종 결과 출력
