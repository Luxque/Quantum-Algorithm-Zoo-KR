# 아벨 숨은 부분군

> * **영어 명칭**: Abelian Hidden Subgroup
> * **속도 향상**: 초다항적
> * **구현 코드**: [Classiq](https://short.classiq.io/simon), [Cirq](https://github.com/quantumlib/Cirq/blob/main/examples/simon_algorithm.py)

$G$는 유한하게 생성된 아벨군, $H$는 $G / H$를 유한하게 하는 $G$의 부분군이라고 하자.
그리고 $f$를 $g_1, g_2 \in G$에 대해 $f(g_1) = f(g_2)$임과 $g_1$과 $g_2$가 $H$의 좌잉여류에 속하는 것이 동치로 하는 $G$에 대한 함수라고 하자.
이 알고리즘의 목표는 $f$의 질의를 만들어 $H$(즉, $H$ 생성자의 집합)를 찾는 것이다.
고전적으로는 $\Omega(|G|)$ 질의가 필요하지만, 양자 컴퓨터는 $O(\log|G|)$ 질의만으로도 해결할 수 있다.
이 알고리즘은 완전한 일반화까지 포함해 보네(Boneh)와 립턴(Lipton)에 의해 정형화되었다 [[14](/QAZKR/appendix/references.html#14)].
그러나 [[76](/QAZKR/appendix/references.html#76)]의 5장에 설명되었듯이, 다음과 같은 알고리즘이 포함하기 때문에 이 알고리즘에 대한 적절한 공로를 인정하기 어렵다.
여기에는 사이먼(Simon)의 알고리즘이 포함되는데 [[108](/QAZKR/appendix/references.html#108)], 이는 쇼어(Shor)의 소인수분해 및 이산 로그 알고리즘의 핵심을 이루는 주기 찾기 알고리즘에 영감을 주었다.
아벨 숨은 부분군 알고리즘은 펠 방정식, 주아이디얼, 가역원군, 유군 알고리즘의 핵심이기도 하다.
특정한 경우에는 아벨 숨은 부분군 문제는 [[30](/QAZKR/appendix/references.html#30)]에서 보였듯이 $\log(|G|)$ 질의가 아닌 단 한개의 질의로 해결할 수 있다.
보통 주기를 찾을 때 $x - y = s$가 아닌 이상 함수는 $f(x) \neq f(y)$인 것으로 간주한다 (여기에서 $s$는 주기).
이러한 제약 조건이 완화되는 경우에도 적용되는 양자 알고리즘은 [[388](/QAZKR/appendix/references.html#388)]에 제시되어 있다.
주기 찾기는 기반 함수의 몇 개의 최상위 비트만 알 수 있는 오라클에 적용되도록 일반화되었다 [[389](/QAZKR/appendix/references.html#389)].
