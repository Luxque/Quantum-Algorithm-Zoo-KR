# 지수 합동식

> * **영어 명칭**: Solving Exponential Congruences
> * **속도 향상**: 다항적
> * **구현 코드**: ∅

$a, b, c, f, g \in \mathbb{F}_q$가 주어져 있을 때 $af^x + bg^y = c$를 만족하는 $x$와 $y$를 찾는다.
[[111](/QAZKR/appendix/references.html#111)]에서 보였다시피, 양자 컴퓨터는 이 문제를 $\tilde{O}(q^{3/8})$ 시간 내로 해결할 수 있지만, 가장 빠른 고전 알고리즘으로는 $\tilde{O}(q^{9/8})$의 시간이 걸린다.
[[111](/QAZKR/appendix/references.html#111)]의 알고리즘은 양자 이산 로그와 탐색법에 기초한다.
