# 번스타인-바지라니

> * **영어 명칭**: Bernstein-Vazirani
> * **속도 향상**: 다항적 (직접), 초다항적 (재귀)
> * **구현 코드**: [Classiq](https://short.classiq.io/bernstein_vazirani), [Cirq](https://github.com/quantumlib/Cirq/blob/main/examples/bernstein_vazirani.py), [PennyLane](https://pennylane.ai/qml/demos/tutorial_qutrits_bernstein_vazirani)

$n$비트를 입력받고 1비트를 출력하는 오라클이 주어져 있다고 하자.
주어진 입력 $x \in \{0, 1\}^n$에 대하여, 출력은 $x \odot h$다 (여기에서 $h$는 숨겨진 비트, $\odot$은 법(모듈로) 2에 대한 비트 단위 내적을 의미함).
이 알고리즘의 목표는 $h$를 찾는 것이다.
고전 컴퓨터는 $n$개의 질의가 필요하다.
번스타인(Bernstein)과 바자라니(Vazarani)가 보인 바와 같이 [[11](/QAZKR/appendix/references.html#11)], 양자 컴퓨터에서는 1개의 질의만으로 이를 수행할 수 있다.
더 나아가, 이 문제를 재귀적으로 바꾸면 재귀 푸리에(Fourier) 추출 문제가 되는데, 양자 컴퓨터는 고전 컴퓨터보다 지수적으로 적은 질의만을 요구한다 [[11](/QAZKR/appendix/references.html#11)].
포괄적인 양자 회로를 통한 양자 속도 향상의 편재성에 관해서는 [[256](/QAZKR/appendix/references.html#256), [257](/QAZKR/appendix/references.html#257)]를, 오라클 함수와 다른 함수의 푸리에 변환 상관관계 감지의 양자 속도 향상에 관해서는 [[258](/QAZKR/appendix/references.html#258), [270](/QAZKR/appendix/references.html#270)]를 참조.
