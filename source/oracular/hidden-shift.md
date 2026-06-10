# 숨은 이동

> * **영어 명칭**: Hidden Shift
> * **속도 향상**: 초다항적
> * **구현 코드**: [Classiq](https://short.classiq.io/hidden_shift), [Cirq](https://github.com/quantumlib/Cirq/blob/main/examples/hidden_shift_algorithm.py)

$\mathbb{Z}_N$ 상에서 어떤 함수 $f$의 오라클만 주어져 있다,
이때 $g$는 알려진 함수이고 $s$는 알려지지 않은 평행이라고 하고, 우리는 $f(x) = g(x+s)$임을 알고 있다고 하자.
숨은 이동 문제의 목표는 $s$를 찾는 것이다.
Grover(그로버) 문제를 환산하면 일반적으로 숨은 이동 문제를 풀기 위해서는 적어도 $\sqrt{N}$개의 질의가 필요하다는 것은 자명해 보인다.
그러나 몇몇 특정한 경우에는 양자 컴퓨터를 통해 $O(1)$의 질의만으로도 숨은 이동 문제를 풀 수 있다.
특히 van Dam(반 담) 등은 만약 함수 $f$가 유한환 및 유한체의 곱셈 지표라면 이를 수행할 수 있음을 보였다 [[89](/QAZKR/appendix/references.html#89)].
르장드르(Legendre) 기호 $(\frac{x}{p})$는 $\mathbb{F}_p$의 곱셈 지표이므로, 이전에 발견된 르장드르 기호 알고리즘[[88](/QAZKR/appendix/references.html#88), [86](/QAZKR/appendix/references.html#86)]은 이 문제의 특별한 경우라고 여겨진다.
이러한 문제들을 $O(\operatorname{polylog}(N))$의 시간으로 해결하는 고전 알고리즘은 알려지지 않았다.
더 나아가, 이동 르장드르 기호 문제의 양자 알고리즘은 양자 질의를 통해 특정 암호용 유사난수 생성기를 무력화시킬 수 있다 [[89](/QAZKR/appendix/references.html#89)].
차집합(difference set) 숨은 이동 문제의 양자 속도 향상은 [[312](/QAZKR/appendix/references.html#312)]에 주어져 있고, 이 또한 르장드르 기호 문제를 특별한 경우로 포함한다.
뢰텔러(Roeteller)는 비선형 부울(Boole) 함수의 숨은 이동을 찾는 지수적 양자 속도 향상을 발견했다 [[105](/QAZKR/appendix/references.html#105), [130](/QAZKR/appendix/references.html#130)].
이를 기반으로 가빈스키(Gavinsky), 뢰텔러, 롤랑(Roland)[[142](/QAZKR/appendix/references.html#)]은 임의 부울 함수 $f: \mathbb{Z}_2^n \rightarrow \mathbb{Z}_2$의 숨은 이동 문제의 고전 질의 복잡도가 $\Omega(2^{n/2})$일 때, 양자 질의는 평균적으로 $O(n)$의 복잡도를 갖는 것을 발견했다.
결과 [[143](/QAZKR/appendix/references.html#143)]은 이면체군의 숨은 부분군 문제로 서술되어 있지만, $\mathbb{Z}_N$을 정의역으로 하는 단사함수의 숨은 이동 문제는 고전 질의 복잡도가 $\Theta(\sqrt{N})$일 때 양자 질의 복잡도는 $O(\log n)$임을 나타낸다.
그러나 알려진 $\mathbb{Z}_N$ 상의 숨은 단사 함수 이동의 양자 회로 복잡도의 최선은 $O(2^{C\sqrt{\log N}})$으로, 쿠퍼버그(Kuperberg) 체 알고리즘을 통해 얻은 것이다 [[66](/QAZKR/appendix/references.html#66)].
문헌 [[408](/QAZKR/appendix/references.html#408), [43](/QAZKR/appendix/references.html#43)]의 성과를 발전시킨 최근의 한 연구 결과는 숨은 다중 이동 문제를 포함한 숨은 이동 문제의 몇 가지 일반화에 대해 지수적 양자 속도 향상을 달성했다.
이 다중 이동 문제에서는 허용된 범위 $s$에 걸쳐 $f_s(x) = f(x-hs)$를 질의할 수 있으며, 이를 통해 $h$를 찾는다.
