# CaBul (사물인식 머신러닝 기반 카테고리 자동 분류 커뮤니티)

## 프로젝트


### CaBul

시연 영상 :

[https://youtu.be/Sg0NXNq49mw/](hhttps://youtu.be/Sg0NXNq49mw/)

프로젝트 일정 : 2022.10.17 ~ 2022.10.21

백엔드  Repository :[https://github.com/devjunseok/CaBul](https://github.com/devjunseok/CaBul)

S.A 링크 : [B-1팀 사물인식 서비스](hhttps://iodized-justice-c7c.notion.site/B1-56fb2a3285fe4d8cb53e1f9f5494d948)

## 1. 프로젝트 주제

### Pytorch, yolo를 활용하여 사용자가 업로드한 이미지를 사물인식 하여 자동으로 카테고리 생성 및 분류 하는 커뮤니티

사물인식 서비스를 접목한 간단한 커뮤니티 사이트

## 2. 기술 스택

- 백엔드
    - Python 3.10
    - Django 4.1.3
    - Pytorch 1.13.0

## 3. 싸지방 팀 팀원 및 역할

### 박준석 - [devjunseok - Overview](https://github.com/devjunseok)

팀장 / 프로젝트 기획 / 사이트 배포 / user 기능/ DB 모델링 / 머신러닝 코드 작성

### 노우석 - [WooSeok-Nho - Overview](https://github.com/WooSeok-Nho/)

팀원 / 프로젝트 기획 / user기능 / user기능 관련 프론트 API 연결 및 제작 / 팔로우,팔로워기능 / 이메일 인증기능

### 성창남 - [SungChangNam - Overview](https://github.com/SungChangNam)

팀원 / 게시글 업로드 / 회원가입 / 로그인-템플릿,게시글 CRUD

### 양기철 - [hanmariyang - Overview](https://github.com/hanmariyang)

팀원 / 프로젝트 기획 / contents 기능 / DB 모델링 / 머신러닝 코드 작성

### 이태겸 - [poro625 - Overview](https://github.com/poro625)

팀원 / 댓글기능 구축

## 4. 프로젝트 기능

### User 기능(회원가입/로그인 - simple jwt 사용)
- 회원가입 시, 비밀번호 유효성 검사 기눙
- 회원정보 CRUD 기능
- 소셜로그인 기능(카카오톡)
- 팔로우, 팔로워

### contents 기능 (게시글, 댓글, 사물인식)

- 게시글 CRUD
- 댓글 CRUD
- 게시글 검색
- Pytorch, yolo 사용 업로드한 이미지 사물인식
 
## 4-1. 트러블 슈팅

### 박준석

**문제 : 카카오 소셜로그인 구현 중 프로필 이미지, 이름 데이터를 가져오지 못하는 현상 발생*

**해결 : 카카오 developer 공식문서를 보고 해결 https://developers.kakao.com/docs** 


### 양기철

**문제 : 게시글 작성시 이미지 카테고리를 머신러닝으로 자동 분류해주어야하는데 게시글 작성시 request 데이터에있는 파일로는 머신러닝에서 파일을 찾을 수 없다고 에러가 발생 하였다.**

**해결 : 게시글을 작성하는 로직에 먼저 save를 해주고 저장된 게시글에 이미지 파일을 불러와서 yolo5를 이용해 카테고리 자동 분류를 실행한 후 해당 게시글에 이미지를 추가 저장하여 해결 하였다.**
### 노우석

**문제 : 팔로우 기능을 작성하던 중 토글 형식으로 작동하게 하고 싶었다.**

**해결 : 함수가 작동할때 팔로우를 하는 사람이 팔로우를 당하는 사람의 팔로워 목록안에 있는지를 확인하는 조건문을 줘서 함수가 실행될 때마다 조건문으로 확인하여 해결**

### 이태겸

**문제 : 댓글기능을 구현하고자 할때 댓글을 DB에 받고자 하기위해 코드를 POST하였으나 GET으로만 받아지는 현상이 발생**

**해결 :<form></form>  <-이런식으로 한번더 위에 했더니 POST형식으로 받아져졌다**

### 성창남

**문제 : 회원가입 작성 페이지 백엔드 부분 구현은 잘되었으나 Django 템플릿 사용하여 구현할 때 오타로 인한 실수로 구현이 안되었다.**

**해결 :단순 오타여서 문제 해결**


## 5. 와이어프레임

[https://www.figma.com/file/MFJqOD0rR4XhZFmudkHHLz?embed_host=share&kind=&node-id=0%3A1&viewer=1](https://www.figma.com/file/MFJqOD0rR4XhZFmudkHHLz?embed_host=share&kind=&node-id=0%3A1&viewer=1)

![cabul_wire](https://user-images.githubusercontent.com/111295065/210206167-bae91427-a32e-43ac-94a5-40276dd235c5.png)

(94kB)

## 6. DB 설계 ERD

![cabul_erd](https://user-images.githubusercontent.com/111295065/210206143-27630a55-b59e-4804-95ae-29008f8b1602.png)