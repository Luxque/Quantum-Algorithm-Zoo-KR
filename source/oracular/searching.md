# 탐색

> * **영어 명칭**: Search
> * **속도 향상**: 다항적
> * **구현 코드**: [Classiq](https://short.classiq.io/quantum_counting), [Cirq](https://github.com/quantumlib/Cirq/blob/main/examples/grover.py), [PennyLane](https://pennylane.ai/qml/demos/tutorial_grovers_algorithm), [Cirq](https://github.com/quantumlib/Cirq/blob/main/examples/grover.py), [Qrisp (그로버)](https://qrisp.eu/reference/Algorithms/Grover.html), [Qrisp (양자 계수)](https://qrisp.eu/reference/Algorithms/quantum_counting.html), [Qrisp (진폭 증폭)](https://qrisp.eu/reference/Primitives/amplitude_amplification.html)

$N$개의 입력값을 받을 수 있는 오라클(oracle)이 주어져 있다고 하자.
그 중에서 단 하나의 입력값 $w$만이 $1$을 출력하고 그 외 입력값은 $0$을 출력한다.
이 알고리즘의 목표는 $w$를 찾는 것이다.
일반 컴퓨터에서는 $\Omega(N)$의 쿼리가 필요하다.
로브 그로버(Lov Grover)가 제시한 양자 알고리즘은 $O(\sqrt{N})$ 쿼리로 $w$를 찾을 수 있고 [[48](/QAZKR/appendix/references.html#48)], 이는 최선의 알고리즘이다 [[216](/QAZKR/appendix/references.html#216)].
