# 논리식 평가

> * **영어 명칭**: Formula Evaluation
> * **속도 향상**: 다항적
> * **구현 코드**: (없음)

각 변수가 한 번씩만 사용될 때, 그 부울(Boole) 표현식을 논리식이라고 한다.
논리식은 팬아웃이 없는 회로에 해당하며, 결과적으로 수형적(트리) 구조를 갖게 된다.
라이카르트(Reichardt)의 스팬 프로그램 형식론은 $O(1)$의 팬인과 $N$개의 변수에 대해서 $\Theta(\sqrt{N})$의 양자 질의 복잡도를 갖는 것으로 현재 알려져 있다 [[158](/QAZKR/appendix/references.html#158)].
이 결과는 거듭된 연구 끝에 나온 것으로 [[27](/QAZKR/appendix/references.html#27), [8](/QAZKR/appendix/references.html#8), [80](/QAZKR/appendix/references.html#80), [159](/QAZKR/appendix/references.html#159), [160](/QAZKR/appendix/references.html#160)], NAND 트리 상의 변수 $2^n$개를 평가할 때 고전 컴퓨터는 $\Omega(2^{0.753n})$의 질의를 요구하는 반면, 양자 컴퓨터는 연속 시간 양자 보행을 통해 $O(2^{0.5n})$의 시간으로 수행할 수 있다는 것을 발견한 파히(Farhi) 등의 연구로부터 시작된 것이다.
많은 경우에는 양자 논리식 평가 알고리즘은 질의 복잡도뿐만 아니라 시간 복잡도까지 효율적이다.
스팬 프로그램 형식론은 양자 질의 복잡도의 하한 또한 도출해 낸다 [[149](/QAZKR/appendix/references.html#149)].
서로 다른 시각에서 발견된 것이지만, Grover(그로버) 알고리즘은 모든 게이트가 OR인 특별한 경우라고 볼 수 있다.
비(非)부울 논리식 평가의 양자 복잡도를 알아보려는 시도는 있었으나 [[29](/QAZKR/appendix/references.html#29)] 완전히 규명되지 않았다.
차일즈(Childs) 등은 입력 변수가 반복되는 경우에 대해서 일반화했다 (이를테면, 회로의 첫 번째 층에 팬아웃이 있을 수 있음.) [[101](/QAZKR/appendix/references.html#101)].
그들은 $O(\min\{N, \sqrt{S}, N^{1/2}, G^{1/4}\})$의 질의를 사용하는 양자 알고리즘을 발견하였다 (여기에서 $N$은 중복도를 포함하지 않은 입력 변수의 개수, $S$는 중복도를 포함한 입력 변수의 개수, $G$는 논리식에 있는 게이트의 개수를 의미함).
각각 다른 입력을 받는 NAND 게이트의 개수가 제한된 NAND 트리 문제에 대해서는 [[164](/QAZKR/appendix/references.html#164), [165](/QAZKR/appendix/references.html#165), [269](/QAZKR/appendix/references.html#269)]를 참조.
몇몇 경우에는 고전 질의 복잡도보다 초다항적 속도 향상을 얻을 수 있다.
