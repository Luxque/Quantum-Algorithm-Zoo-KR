# 다항식 보간

> * **영어 명칭**: Polynomial Interpolatoin
> * **속도 향상**: 상이함
> * **구현 코드**: (없음)

$p(x) = a_dx^d + \cdots + a_1x + a_0$를 유한체 $\operatorname{GF}(q)$ 상에서의 다항식이라고 하자.
주어진 $x \in \operatorname{GF}(q)$에 대해 $p(x)$를 반환하는 오라클이 주어져 있다고 하자.
다항식 복원 문제는 이 오라클에 질의를 넣어 다항식 계수 $a_d, \cdots, a_0$을 찾는다.
고전적으로는 $d + 1$개의 질의가 적당하다.
(몇몇 문헌에서는 보간이라는 용어 대신 복원을 사용한다.)
양자 컴퓨터에서는 $d/2 + 1/2$개의 질의가 필요하고 $d/2 + 1$개의 질의는 충분하다 [[360](/QAZKR/appendix/references.html#360), [361](/QAZKR/appendix/references.html#361)].
차수가 $d$이고 $n$개의 변수를 가지는 다변수 다항식은 $\binom{n+d}{d}$의 고전 질의 복잡도를 가진다.
[[387](/QAZKR/appendix/references.html#387)]에서 보였듯이, $\mathbb{R}$과 $\mathbb{C}$ 상에서는 $O(\frac{1}{n+1}\binom{n+d}{d})$의 양자 질의 복잡도를, 충분히 큰 $q$의 $\mathbb{F}_q$ 상에서는 $O(\frac{d}{n+d}\binom{n+d}{d})$의 양자 질의 복잡도를 갖는다.
$\chi$가 $\operatorname{GF}(q)$의 이차 지표라고 할 때, $\chi(f(x))$를 반환하는 오라클과 $f(x)^e$를 반환하는 오라클의 양자 알고리즘 또한 발견되었다 [[390](/QAZKR/appendix/references.html#390)].
이들은 [[89](/QAZKR/appendix/references.html#89)]의 숨은 이동 알고리즘을 일반화하고 고전 컴퓨팅 방식보다 지수적 속도 향상을 달성한다.
함숫값에 접근 가능한 소음이 있는 불완전한 오라클로 유한체 상의 유리함수를 복원하는 양자 알고리즘은 [[391](/QAZKR/appendix/references.html#391)]에 주어져있다.
