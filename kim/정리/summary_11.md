## 병행성
- 컴퓨터가 일을 수행하면서 뭔가 기다린다면, 보통 다음 두 가지 이유 중 하나다.
 * I/O 바운드: 대부분 이 경우에 해당한다. 컴퓨터의 CPU는 엄청나게 빠르다. 메모리보다 몇 백배, 디스크나 네트워크보다 몇 천배 빠르다.
 * CPU 바운드: 과학이나 그래픽 작업과 같이 엄청난 계산이 필요할 때 발생한다.

### 큐
- 일반적으로 큐는 메시지를 전달한다. 메시지는 모든 종류의 정보가 될 수 있다. 분산 작업 관리를 위한 큐의 경우 작업 큐라고 알려져있다.

### 프로세스 & 스레드
- 스레드는 한 프로세스 내에서 실행된다. 프로세스의 모든 자원에 접근 할 수 있으며, 다중인격과 비숫하다.
- multiprocessing 모듈과 threading 모듈의 한 가지 다른 점은 threading 모듈에는 terminate() 함수가 없다는 것이다.
- 스레드는 위험하다. C와 C++ 언어에서 메모리 관리를 수동으로 하는 것처럼, 매우 찾기 힘든 버그가 발생 할 수 있다.스레드를 사용하려면 프로그램의 모든 코드와 이 프로그램을 사용하는 외부 라이브러리에서 반드시 스레드-세이프한 코드를 작성해야 한다.
- 데이터를 안전하게 공유하는 일반적인 방법은 스레드에서 변수를 수정하기 전에 소프트웨어 락을 적용하는 것이다.
- 다음과 같이 파이썬을 사용할 것을 추천한다.
 * I/O 바운드 문제: 스레드 사용
 * CPU 바운드 문제: 프로세스, 네트워킹, 이벤트 사용

### 그린 스레드외 gevent
- 개발자들은 전통적으로 별도의 스레드나 프로세스를 실행하여 프로그램의 속도가 느린 부분을 피한다.
- 또 하나의 대안은 이벤트 기반 프로그래밍이다. 이벤트 기반 프로그램은 중앙 이벤트 루프를 실행하고, 모든 작업을 조금씩 실행하면서 루프를 반복한다.

## 네트워크
### 패턴
- 몇 가지 기본 패턴으로 네트워킹 애플리케이션을 만들 수 있다.
- 가장 일반적인 패턴은 요청-응답 패턴으로, 클라이언트-서버 패턴으로도 알려져 있다. 이 패턴은 동기적이다.
- 또 다른 일반적인 패턴은 푸시 또는 팬아웃 패턴이다. 데이터를 프로세스 풀에 있는 사용 가능한 워커로 전송된다.
- 푸시의 반대는 풀 또는 팬인이다. 하나이상의 소스로부터 데이터를 받는다. 예를 들어 멀티 프로세스에서 텍스트 메시지를 받아서, 하나의 로그 파일에 작성하는 로거가 있다.

### 발행-구독 모델
- 발행-구독은 큐가 아닌 브로드캐스트다. 하나 이상의 프로세스가 메시지를 발행한다. 각 구독자 프로세스는 수신하고자 하는 메시지의 타입을 표시한다. 각 메시지의 복사본은 타입과 일치하는 구독자에 전송된다.

### TCP/IP
- 인터넷은 커넥션을 맺고, 데이터를 교환하고, 커넥션을 종료하고, 타임아웃을 처리하는 등의 방법에 대한 규칙에 의거한다. 이것을 프로토콜이라고 하며 계층으로 정렬되어 있다.
- IP 계층에는 네트워크 위치 사이에서 바이트를 이동하는 방법을 기술하는 두 가지 프로토콜이 있다.
 * UDP (사용자 데이터 프로토콜): 짧은 데이터 교환에 사용된다. 데이터그램은 엽서의 짧은 글처럼, 한 단위로 전송되는 작은 메시지다.
 * TCP (전송 제어 프로토콜): 이 프로토콜은 수명이 긴 커넥션에 사용된다. TCP는 바이트 스트림이 중복없이 순서대로 도착하는 것을 보장한다.

