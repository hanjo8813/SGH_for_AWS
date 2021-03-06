# 개발일지

### Please Graduate의 개발 과정을 기록합니다

<br>

## 개발/업데이트 기록

### 07/22
- 자연과학대, 생명과학대 소속 학과(8개) 기준 추가
- 화학과 기초교양 선택과목 예외처리 ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/49))

### 07/19
- 졸업요건 검사 알고리즘 리팩토링 ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/50))
- 전자정보통신공학과 전공 기준 오류 수정

### 07/16
- 지능기전공학부 검사 기준 오류 수정

### 07/13
> 총 방문자 수 : `1178` / 실사용자 수 : `434`
- 렌더링 방식 리팩토링 ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/46))
- Repo명 / 프로젝트 폴더명 / conf 설정 파일명 변경 ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/47))

### 07/12
- 검사 결과 버그 수정 
- 고전독서 렌더링 버그 수정 ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/44))
- 오늘 방문자 수 추가 ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/45))

### 07/05
- 도메인 변경 : `sejong-please-graduate.ml` -> `please-graduate.com` ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/40))

### 07/04
- 방문자 수 집계 방식 변경 ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/37))
- 팝업 창 다시보지 않기 기능 추가

### 06/29
> 총 방문자 수 : `1070` / 실사용자 수 : `421`
- **version 2.0 Beta 2 배포**
- 추천 알고리즘 변경 : 머신러닝 -> 이수 빈도수 ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/30))
- 회원탈퇴 기능 추가
- 업로드하는 기이수성적 엑셀 형식 변경
- 커스텀 버그 수정 ([자세히](https://github.com/hanjo8813/PleaseGraduate/issues/42))

### 03/28
- **version 2.0 Beta 1 배포**
- 기이수성적표를 크롤링해서 받아오는 방식을 -> 엑셀 업로드하는 방식으로 변경
- 회원가입 기능 추가
- 기이수과목 커스텀 기능 추가
- 비밀번호 변경 기능 추가
- 영어성적 입력 및 연계/복수 전공 기준 추가

### 02/15
> 총 방문자 수 : `512` / 총 검사 횟수 : `416` / 실사용자 수 : `260`
- 수강신청 기간이라 사용 못하도록 수정

### 02/14
- 기준 추가 후 재배포
- 추천 머신러닝 부분 수정

### 02/12
> 총 방문자 수 : `266` / 총 검사 횟수 : `260` / 실사용자 수 : `102`
- 전자정보통신공학과 기준 추가
- 공학인증 기준 DB 구조 변경 + 알고리즘 보완
- 머신러닝 추천시, 참고 데이터를 같은 학과로만 구성하도록 변경

### 02/11
- uis에서 특정 ip의 다수의 우회 로그인 감지시 당일 해당 ip 차단함을 알게됨
- 따라서 일단 보완점으로 재검사하는 사용자는 크롤링하지 않도록 방식 변경
- 보안 취약점 보완 , https 적용

### 02/10
- 장고 secret key , DB 정보 git hub 노출 관련 피드백 수정

### 02/09
> 총 방문자 수 : `152` / 총 검사 횟수 : `156`
- **version 1.0으로 첫 배포**
- 150회 이상의 검사로 uis의 우회 로그인 차단
- index 페이지에 공지 후 사이트 이용 차단 후 점검

### 01/31
- ID/PW 틀릴 시 예외처리 
- 해당 학과-학번의 기준이 없을 시 예외처리
- 크롤링 함수 병합 및 개발-배포 분리
- 사용자 정보를 더이상 세션에 담지 않고 DB에 저장
- 엑셀 파일 다운 -> DF화 -> DB에 저장 -> 엑셀 삭제 방식으로 변경

### 01/30
- 기존의 excel 파일 다운로드 방식을 변경
- user_info/user_grade 테이블 생성

### 01/18
- wsgi 패키지 설치
- nginx 설치 후 static 경로 설정
- 로컬 기준 경로 코드를 ubuntu 기준 추가
- 개발자 모드가 아닌 항시 배포상태 성공

### 01/17
- MySQL 설치 및 http-port 생성 후 연동.
- 크롬/크롬드라이버 설치
- Django settings 변경
- 개발자 모드(runserver)로 client 테스트.. 실패..

### 01/16
- AWS EC2 서버 생성
- 기본 패키지 설정
- python/pip 설치
- 가상환경(virtual-env)내에 py라이브러리 설치
- ubuntu에 git clone, 연동

<br>

## 설치한 라이브러리 목록
> venv를 사용하지 않기 때문에 기록

- `pip install pylint-django` (vs코드용)
- `pip install django`
- `pip install django-pandas`
- `pip install django-crontab`
- `pip install mysqlclient`
- `pip install pandas`
- `pip install xlrd`
- `pip install selenium`
- `pip install beautifulsoup4`
- `pip install surprise`
- `pip install openpyxl`
