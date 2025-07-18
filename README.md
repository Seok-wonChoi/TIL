## 250716

GUI : 그래픽 유저 인터페이스
TUI : 텍스트 (이말은 잘 안씁니다.)

CLI : Command Line Interface

interface : 대상을 제어하는 수단 ( ex) 리모컨) )

========================================

Window OS의 Interface
GUI : Windows Shell
CLI : cmd(명령프롬프트), Power Shell

Linux OS의 Interface
GUI : GNOME
CLI : bash

왜 굳이 bash를 쓸까??
bash가 편해서 ---> Tab키 자동완성

Git을 다룰때 Interface
GUI : Github Desktop, 소스트리
CLI : git bash

결론 : GUI, CLI 둘다 쓸수는 있어야하지만 우리는 CLI를 쓸겁니다.

GUI의 장점 : 그래프 같은 복잡한 분석 보기 편하다
CLI의 장점 : 빠르다(Commit 명령어 3~4초면 끝)

====================================================

리눅스는 항상 HOME 디렉토리에서 시작 : ~
. : 현재 디렉토리
cd ~ : 홈 디렉토리
cd .. : 상위 디렉토리
cd - : 뒤로가기

touch : 파일생성
mkdir : 폴더생성
start : 파일 열기
rm : 파일 삭제
rm -rf : 폴더 삭제
cp : 복사

절대경로
~/Desktop/test/python/

상대경로(현재 티렉토리를 기준)
cd ./python
cd ../python2

=======================================================

python.org ---> python 설치 ---> 3.11.9
인터프리터

extension??
너 IDE 뭐써??
vscode는 IDE일까??
vscode는 텍스트 에디터 : 여기에 extension을 추가해서 마치 IDE처럼 쓴다.

IDE
Python : Pycharm, jupyter notebook
C : Visual Studio
Java : IntelliJ

node.js ---> 런타임
js 백엔드 프레임워크 ---> express.js 

====================================================================

Markdown : 로직 X 
README.md에 활용
: 내가 공부한내용, 프로젝트에 대한 간단한 설명(가독성, 편의성)

============================================================


git init  : git 시작 (로컬 저장소 생성)
rm -rf .git : git 삭제(git 종료)

git add . : staging area에 변경사항 올리기
git status : staging area의 작업 파일 확인

git config --global user.email "이메일주소"
git config --global user.name "이름"
git config --global -l

git commit -m "메시지명" : repository에(staging area의 변경사항을)올리기
git log : repository 작업 파일 확인 (커밋 이력 확인)

<img width="1338" height="617" alt="image" src="https://github.com/user-attachments/assets/6564f430-8f78-4755-be8c-da4e97b3c92a" />


===================================================

참고자료 

git commit --amend : vim 에디터가 열린다

수정 후(커서 위치를 확인 후 과감하게 타이핑)

ecs -> :q -> 저장하지 않고 종료
ecs -> :q! -> 저장하지 않고 강제 종료
ecs -> :wq -> 저장하고 종료

## 250717
# GIT 기본

**git** : 분산 버전 관리 시스템

**git** : 로컬저장소 // github : 원격저장소

**git init** : git 시작

**git add .** : staging area에 올리기
**git status** : staging area의 작업 파일 확인

<___git commit 전에___>

git config --global user.name "이름"

git config --global user.email "이메일"

git config --global -l : user.name과 user.email 확인

**git commit -m "메시지명"** : repository에 올리기
git log : 커밋 이력을 확인

**git remote add origin url** : 로컬 저장소와 원격저장소를 연결(origin은 별칭)
git remote -v : remote 목록 확인

git remote rm 별칭 : remote 이력 삭제


**git push origin +master** : 가장 최근에 commit 되어있던 것을 강제로 push
                                 (origin:별칭, master:branch명, +:강제로 진행)

==================================================

Q) clone과 pull의 차이점이 뭘까??
A) 새로운 환경에서 처음 다운로드 : clone

명령어 : git clone url

Q) clone을 받으면 remote를 할 필요가 있을까?
A) remote를 할 필요가 없다.

Q) clone과 pull의 차이?
A) 한번 clone을 받고 그 이후에는 pull로 진행

명령어 : git pull origin +master

==================================================

자리 옮긴후 

1. git clonfig --global -l 확인
user.name, user.email 확인

2. 제어판 -> 사용자 계정 -> window 자격 증명 -> github, gitlab 삭제


=================================================

Q) .gitignore 파일은 왜 만들까?
A) 수 백개의 파일을 일일이 git add 하기에는 불편하기 때문에
    .gitignore파일을 만들면 편하다

용량이 매우 크거나, 보안상 문제가 있거나, 청구 결제 관련된 파일들을
add 하지 않기 위해 .gitignore파일을 만든다(staging area에 올리지 않기 위해)

방법 : .gitignore 파일 생성 -> add 하지 않을 파일명이나 폴더명 작성하고 저장 

<img width="1248" height="476" alt="image" src="https://github.com/user-attachments/assets/8414a32a-3536-4d94-a037-68ee24850e7c" />

***

# GIT 심화

___commit 메시지 수정하기___

명령어 : git commit --amend

vim에디터에서 수정하고
esc -> :q! : 저장하지 않고 강제 종료
esc -> :wq! : 강제 저장하고 종료

====================================

___git revert___ : 특정 commit을 없었던 일로 만들기

a.txt 만들고 commit
b.txt 만들고 commit
c.txt 만들고 commit

git log -> 해시값 전체 복사(ctrl + shift + c), 붙여넣기(shift + insert)

명령어 :
git revert 해시값 : 이 특정 커밋을 없었던 일로 만든다.
vim 에디터 -> esc -> :wq

==========================================

**git reset** : 특정 commit으로 되돌리기

**git reflog** : 이전 과거 commit 기록들을 모두 볼 수 있음

명령어 : **git reset --hard HEAD@{번호}**

=========================================

staging area 있는 작업을 working directory로 옮기기

___git add 취소하기___

<git 2.23 버전 이전>

1. commit이 없는 경우
git rm --cached 파일명

2. 이전에 했던 commit이 있는경우(권장 방법)
git restore --staged 파일명
=============================================


## 250718
# API
<img width="845" height="563" alt="image" src="https://github.com/user-attachments/assets/1061f46d-ca08-4bdb-b727-97308c4ba6cf" />

### GPT API 활용 사례
+ 콘텐츠 생성: 블로그 게시물, 광고 카피, 소셜 미디어 콘텐츠 생성.
+ 고객 지원: 자동 응답 봇, FAQ 응답 시스템.
+ 교육: 학습 자료 생성, 문제 풀이 설명, 힌트 제공.
+ 연구: 데이터 분석, 논문 요약, 정보 검색.

### 1. 기본 사용 방법
+ API 파라미터 숙지
  + 아래 실습 코드의 `API 호출 부분`
+ GPT API에서 Role은 챗봇의 다양한 사용 사례에 따라 서로 다른 방식으로 응답을 생성할 수 있도록 하는 기능
```
    1. system:
      - 역할: 기본 지침을 설정하고 대화의 전체적인 방향을 설정합니다.
      - 특징: 대화의 톤, 스타일, 특정 규칙 등을 정의합니다.

    2. user:
      - 역할: 사용자의 입력을 나타냅니다.
      - 특징: 질문이나 명령 등 사용자가 챗봇에게 전달하는 메시지를 포함합니다. 챗봇은 이를 바탕으로 응답을 생성합니다.

    3. assistant:
      - 역할: 챗봇의 응답을 나타냅니다.
      - 특징: 시스템의 지침과 사용자의 입력을 토대로 생성된 응답을 나타냅니다.
```
+ `실습 내용`
  + GPT API의 파라미터를 바꿔가면서 어떠한 출력이 나오는지 확인한다.
    1. max_tokens의 값을 10으로 바꾸고 어떻게 출력되는지 본다.
    2. n=2로 바꿔서 값이 어떻게 출력되는지 본다.
    3. 질문의 content를 바꿔서 출력해본다.

+ `주의 사항`
  + n값을 너무 크게 설정하면 API호출 과비용 발생
 

### 2. 프롬프트 엔지니어링 실습
+ **2.1 명시적 지시**
  + 프롬프트 구조화, 질문에 대한 배경 정보 제공 및 명확한 지시는 더 나은 결과를 얻습니다.
    + 프롬프트 형식 지정, 맥락 제공, 페르소나 지정, 제한 사항 지정, 출력 형식 지정 등
  + 실습 : 면접 예상 질문 얻기
    + 아래와 같은 채용 공고에서 예상 면접 질문을 얻습니다
    + 하드 스킬과 소프트 스킬의 두 섹션에 대해 예상 면접 질문 받아야 합니다.
    + 각 섹션 마다 번호가 매겨진 목록으로 5개씩 예상 질문을 받으세요.
      
+ **2.2 퓨삿 프롬프트** (Few-Shot Prompt)
  + 프롬프트에 몇 가지 예시를 제공하여 모델이 특정한 방식으로 답변을 생성하도록 유도하는 방법
  + 예시:
  ```
    SYSTEM:
    아래와 같은 형태로 주어진 문장에 담긴 감정을 긍정, 부정, 또는 중립으로 분류하세요.

    1. 서비스에 매우 만족합니다.
      감정: 긍정

    2. 제품 품질이 형편없어서 환불을 원합니다.
      감정: 부정

    3. 오늘 날씨는 그냥 그래요.
      감정: 중립

    USER: 오늘 프롬프트 엔지니어링을 배워서 너무 기뻐요.

    ASSISTANT: 감정 : 긍정
  ```

  + 실습 : 삼행시 생성
    + GPT가 삼행시를 생성해 낼 수 있도록 퓨삿 프롬프트를 완성하세요.

+ **2.3 생각의 사슬 (Chain-of-Thought)**
  + **설명**:
   최종 답을 바로 도출하는 것이 아니라, 문제를 해결하기 위한 중간 단계를 거쳐 사고 과정을 설명함으로써 더 정확하고 일관된 답을 도출.
   단순히 "단계적으로 문제를 해결하세요.(Let's think step by step)" 라는 프롬프트를 넣어도 생각의 사슬 효과를 어느정도 얻을 수 있음.
   답변한 것을 토대로 "위의 답변이 올바른지 평가해보세요" 라는 프롬프트를 넣으면 평가하는 과정도 생성되어 올바른 결과를 답변할 가능성이 높아짐.
  + **원리**: GPT에게 결과에 대한 근거를 입력으로 줌으로써 올바른 결과 도출 유도함
  + **활용**: 계산 문제나 논리적 추론을 요하는 문제에서 유용.
    
+ **2.4 자기 일관성 (Self-Consistency)**
  + 거대 언어 모델(LLM)은 확률론적 성격을 지니고 있어, Chain-of-Thought와 같은 기법을 사용하더라도 단일 생성으로는 종종 잘못된 결과가 나올 수 있음.
  + 자기 일관성(Self-Consistency)은 다수의 생성을 통해 가장 빈번하게 나타나는 답을 선택함으로써 정확성을 높이는 방법.
  + 단점: 더 높은 계산 비용을 수반.
  
+ **2.5 인터넷 검색 기반 응답**
  외부 지식을 토대로 신뢰성 있는 답변 받기
  + 실습
    1. 위키피디아의 정보를 잘 가지고 오는지 `page_title`의 변수 값을 바꿔가보면서 출력되는 내용을 확인한다.
    2. GPT에게 질문할 내용을 위키피디아의 검색어로 사용할 수 있도록 GPT를 통해 질문의 키워드를 추출한다.
    3. 완성된 실습 코드에서 아래와 같은 예시 프롬프트로 실습해본다.
      + 위키피디아에 있는 정보 : 마이크로소프트의 최신 기술에 대해 알려줘.
      + 위키피디아에 없는 정보 : 사과 회사에 대한 핵심 기술에 대해 알려줘


# Vive Coding
<img width="1064" height="570" alt="image" src="https://github.com/user-attachments/assets/78aa4248-5caa-4bdf-8dfc-33fadc12d332" />
