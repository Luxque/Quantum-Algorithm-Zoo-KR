# 이산 로그

> * **영어 명칭**: Discrete-Log
> * **속도 향상**: 초다항적
> * **구현 코드**: [Classiq](https://short.classiq.io/discrete_log), [Qrisp](https://github.com/diehoq/quantum-elliptic-curve-logarithm)

임의의 $s$에 대하여 $b = a^s \mod N$를 만족하는 $n$비트 정수 $a$, $b$, $N$이 주어져 있다고 하자.
이 알고리즘은 $s$를 찾는다.
쇼어(Shor)가 보였듯이 [[82](/QAZKR/appendix/references.html#82)], 이는 양자 컴퓨터에서 $\operatorname{poly}(n)$ 시간에 찾을 수 있다.
알려진 가장 빠른 고전 알고리즘은 $n$에 대해 초다항 시간이 걸린다.
[[82](/QAZKR/appendix/references.html#)]에서 보인 비슷한 방법을 이용하여 양자 컴퓨터로 타원 곡선상의 이산 로그 문제를 풀 수 있음에 따라 타원 곡선을 이용한 암호 방식을 무력화시킬 수 있다.[[109](/QAZKR/appendix/references.html#109), [14](/QAZKR/appendix/references.html#14)].
쇼어 알고리즘에서 최적화를 가한 알고리즘은 [[385](/QAZKR/appendix/references.html#385), [432](/QAZKR/appendix/references.html#432)]에 설명되어 있다.
이 초다항적 속도 향상은 반군 상의 이산 로그 문제에 대해서도 확장 되어있다 [[203](/QAZKR/appendix/references.html#203), [204](/QAZKR/appendix/references.html#204)].
[아벨 숨은 부분군](/QAZKR/oracular/abelian-hidden-subgroup.html)을 참고.
