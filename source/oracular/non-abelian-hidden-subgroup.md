# 비아벨 숨은 부분군

> * **영어 명칭**: Non-Abelian Hidden Subgroup
> * **속도 향상**: 초다항적
> * **구현 코드**: ∅

$G$는 유한하게 생성된 군, $H$는 유한한 좌잉여류를 가지는 $G$의 부분군이라고 하자.
그리고 $f$를 $g_1, g_2 \in G$에 대해 $f(g_1) = f(g_2)$임과 $g_1$과 $g_2$가 $H$의 좌잉여류에 속하는 것이 동치로 하는 $G$에 대한 함수라고 하자.
이 알고리즘의 목표는 $f$의 쿼리를 만들어 $H$(즉, $H$ 생성자의 집합)를 찾는 것이다.
고전적으로는 $\Omega(|G|)$ 쿼리가 필요하지만, 양자 컴퓨터는 $O(\log|G|)$ 쿼리만으로도 해결할 수 있다 [[37](/QAZKR/appendix/references.html#37), [51](/QAZKR/appendix/references.html#51)].
그러나 이 알고리즘은 효율적이라고 할 수 없는데, 그 이유는 쿼리에 따른 양자 상태를 준비하기 위해서 지수적 시간이 소요될 수 있기 때문이다.
특정 비아벨군을 위한 효율적인 숨은 부분군 양자 알고리즘은 알려져 있다 [[81](/QAZKR/appendix/references.html#81), [55](/QAZKR/appendix/references.html#55), [72](/QAZKR/appendix/references.html#72), [53](/QAZKR/appendix/references.html#53), [9](/QAZKR/appendix/references.html#9), [22](/QAZKR/appendix/references.html#22), [56](/QAZKR/appendix/references.html#56), [71](/QAZKR/appendix/references.html#71), [57](/QAZKR/appendix/references.html#57), [43](/QAZKR/appendix/references.html#43), [44](/QAZKR/appendix/references.html#44), [28](/QAZKR/appendix/references.html#28), [126](/QAZKR/appendix/references.html#126), [207](/QAZKR/appendix/references.html#207), [273](/QAZKR/appendix/references.html#273)].
약간 오래된 논의는 [[69](/QAZKR/appendix/references.html#69)]를 참조.
특히 주목되는 것은 대칭군과 이면체군이다.
대칭군의 해는 그래프 동형사상 문제를 풀 수 있고, 이면체군의 해는 특정 격자 문제를 풀 수 있다 [[78](/QAZKR/appendix/references.html#78)].
수많은 연구에도 불구하고 특정한 경우를 제외하면 이 군들의 해를 찾는 다항시간 알고리즘은 알려지지 않았다 [[312](/QAZKR/appendix/references.html#312)].
그러나 쿠퍼버그(Kuperberg)는 이면체군 $D_N$의 숨은 부분군을 찾는 시간복잡도 $2^{O(\sqrt{\log{N}})}$의 알고리즘을 발견했다 [[66](/QAZKR/appendix/references.html#66)].
레게브(Regev)는 곧이어 부(副)지수적 시간뿐만 아니라 다항적 공간을 쓰는 알고리즘으로 개선하였다 [[79](/QAZKR/appendix/references.html#79)].
점근적으로 늘어나는 필요한 큐비트의 수를 개선한 알고리즘은 [[218](/QAZKR/appendix/references.html#218)]에 제시되어 있다.
순열 집합에 대해 동형사상임을 판별하는 더욱 일반적인 문제의 양자 쿼리 속도 향상(게이트 개수로 따지면 효율적인 양자 알고리즘이 아닐 수 있음)은 [[311](/QAZKR/appendix/references.html#311)]에 제시되어 있다.
