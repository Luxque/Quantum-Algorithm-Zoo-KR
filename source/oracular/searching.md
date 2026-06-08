# 탐색

> * **영어 명칭**: Search
> * **속도 향상**: 다항적
> * **구현 코드**: [Classiq](https://short.classiq.io/quantum_counting), [Cirq](https://github.com/quantumlib/Cirq/blob/main/examples/grover.py), [PennyLane](https://pennylane.ai/qml/demos/tutorial_grovers_algorithm), [Cirq](https://github.com/quantumlib/Cirq/blob/main/examples/grover.py), [Qrisp (그로버)](https://qrisp.eu/reference/Algorithms/Grover.html), [Qrisp (양자 계수)](https://qrisp.eu/reference/Algorithms/quantum_counting.html), [Qrisp (진폭 증폭)](https://qrisp.eu/reference/Primitives/amplitude_amplification.html)

$N$개의 입력값을 받을 수 있는 오라클(oracle)이 주어져 있다고 하자.
그중에서 단 하나의 입력값 $w$만이 $1$을 출력하고 그 외의 입력값은 $0$을 출력한다.
이 알고리즘의 목표는 $w$(승자를 의미하는 'winner'의 머릿글자를 따옴)를 찾는 것이다.
일반 컴퓨터에서는 $\Omega(N)$의 쿼리가 필요하다.
로브 그로버(Lov Grover)가 제시한 양자 알고리즘은 $O(\sqrt{N})$ 쿼리로 $w$를 찾을 수 있고 [[48](/QAZKR/appendix/references.html#48)], 이는 최선의 알고리즘이다 [[216](/QAZKR/appendix/references.html#216)].
이 알고리즘은: 

* 여러 개의 $w$ 찾기 [[15](/QAZKR/appendix/references.html#15)]
* 임의 함수의 합 산출하기 [[15](/QAZKR/appendix/references.html#15), [16](/QAZKR/appendix/references.html#16), [73](/QAZKR/appendix/references.html#73)]
* 임의 함수의 평균, 중앙값, 전역 최솟값 찾기 [[35](/QAZKR/appendix/references.html#35), [75](/QAZKR/appendix/references.html#75), [255](/QAZKR/appendix/references.html#255), [465](/QAZKR/appendix/references.html#465), [472](/QAZKR/appendix/references.html#472)]
* 다른 초기 상태[[100](/QAZKR/appendix/references.html#100)] 및 비균등 확률 사전분포[[123](/QAZKR/appendix/references.html#123)]를 통한 이점 얻기
* 입력값 크기에 따라 실행시간이 달라지는 오라클로 작업하기 [[138](/QAZKR/appendix/references.html#138)]
* 정적분 값 근사하기 [[77](/QAZKR/appendix/references.html#77)]
* 고정값에 수렴하기 [[208](/QAZKR/appendix/references.html#208), [209](/QAZKR/appendix/references.html#209), [433](/QAZKR/appendix/references.html#433)]

의 경우에 대해서도 일반화되었다.
양자 탐색 회로의 깊이를 최적화하는 것은 [[405](/QAZKR/appendix/references.html#405)]에 제시되어 있다.
그로버 알고리즘의 일반화라고 알려진 진폭 추정[[17](/QAZKR/appendix/references.html#17)]은 중요한 초기 양자 알고리즘으로 여겨지고 있다.
진폭 추정은 중복 탐지와 그래프 성질에 관련된 양자 알고리즘의 근간을 이룬다.
그로버 탐색을 이용하여 3-SAT 문제와 같은 $\operatorname{NP}$-완전 문제의 답을 찾는 속도를 향상할 수 있다.
하지만 3-SAT 문제의 해를 찾는 고전 알고리즘은 무차별 대입(brute force search)이 아니기 때문에 양자 알고리즘을 통한 응용은 자명하지 않다.
그럼에도 [[133](/QAZKR/appendix/references.html#133)]에서 보였듯이, 진폭 추정은 3-SAT 문제의 해를 찾는 고전 알고리즘 중에서 가장 빠른 것보다 2차적 속도 향상을 얻을 수 있다.
다른 제약조건의 만족 문제에 대한 2차적 속도 향상도 [[134](/QAZKR/appendix/references.html#134)]에 제시되어 있다.
(진폭 증폭을 통해 무차별 대입에 비해 약간의 2차적 속도 향상을 얻는 것은 [[493](/QAZKR/appendix/references.html#493), [492](492)]에 제시되어 있다.)
그로버 탐색과 진폭 증폭의 더 많은 예시는 [[261](/QAZKR/appendix/references.html#261), [262](/QAZKR/appendix/references.html#262)]을 참조.
그로버 탐색과 깊게 연관되어 있으면서도 더 어려운 문제는 공간 탐색으로, 데이터베이스 쿼리가 일부 그래프 구조에 의해 한정되어 있다.
충분히 잘 연결된 그래프는 $O(\sqrt{n})$의 양자 쿼리 복잡도를 지니는 것이 가능하다 [[274](/QAZKR/appendix/references.html#274), [275](/QAZKR/appendix/references.html#275), [303](/QAZKR/appendix/references.html#303), [304](/QAZKR/appendix/references.html#304), [305](/QAZKR/appendix/references.html#305), [306](/QAZKR/appendix/references.html#306), [330](/QAZKR/appendix/references.html#330)].
