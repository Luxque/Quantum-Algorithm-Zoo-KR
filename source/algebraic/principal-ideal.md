# 주아이디얼

> * **영어 명칭**: Principal Ideal
> * **속도 향상**: 초다항적
> * **구현 코드**: ∅

$n$비트 정수 $d$와 환 $\mathbb{Z}[\sqrt{d}]$의 가역 아이디얼 $I$가 주어져 있다고 하자.
만약 $I = \alpha\mathbb{Z}[\sqrt{d}]$를 만족하는 $\alpha \in \mathbb{Q}(\sqrt{d})$가 존재한다면 $I$는 주(主)아이디얼이다.
여기서 $\alpha$는 $d$보다 지수적으로 클 수 있다.
그러므로 $\alpha$는 일반적으로 다항 시간 내로 쓸 수 없다.
하지만 $\lfloor \log(\alpha) \rceil$는 $\alpha$를 유일하게 특정한다.
이 알고리즘은 $I$가 주아이디얼인지 판별하고 만약 그렇다면 $\lfloor \log(\alpha) \rceil$를 찾는다.
홀그렌(Hallgren)이 보인 바와 같이, 이는 양자 컴퓨터로 다항 시간 내로 수행할 수 있다 [[49](/QAZKR/appendix/references.html#49)].
적은 큐비트를 사용하는 수정된 양자 알고리즘은 [[131](/QAZKR/appendix/references.html#131)]에 설명되어 있다.
임의 차수의 수체에서 주아이디얼을 찾는 양자 알고리즘은 (이를테면, 차수에 따라 다항적으로 커지는) [[329](/QAZKR/appendix/references.html#329)]에 설명되어 있다.
소인수분해 문제는 펠 방정식 문제로 환산할 수 있고, 또 펠 방정식 문제는 주아이디얼 문제로 환산할 수 있다.
그리하여 주아이디얼 문제는 적어도 소인수분해 문제만큼 어려우므로 $\text{P}$에 속하지 않을 수 있다.
[아벨 숨은 부분군](/QAZKR/oracular/abelian-hidden-subgroup.html)을 참고.
