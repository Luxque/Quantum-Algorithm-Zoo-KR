# 정렬 탐색

> * **영어 명칭**: Ordered Search
> * **속도 향상**: 상수 인자
> * **구현 코드**: (없음)

수 크기에 따라 순서대로 나열된 $N$개의 원소를 가진 배열과 그것에 접근할 수 있는 오라클이 주어졌다고 하자.
수 $x$가 주어졌을 때, 이 알고리즘의 목표는 배열 내에서 주어진 수의 알맞은 위치를 찾는 것이다.
고전적으로 최상의 알고리즘은 이전 탐색이며 $\log_2 N$개의 질의가 필요하다.
파히(Farhi) 등은 양자 컴퓨터가 이를 $0.53\log_2 N$개의 질의로 수행할 수 있음을 보였다 [[39](/QAZKR/appendix/references.html#39)].
현재로써 알려진 결정적 양자 알고리즘은 $0.433\log_2 N$개의 질의만을 사용한다 [[103](/QAZKR/appendix/references.html#103)].
이 문제에 대한 하한은 $\frac{\ln 2}{\pi}\log_2 N$개의 양자 질의임이 증명되었다 [[219](/QAZKR/appendix/references.html#219), [24](/QAZKR/appendix/references.html#24)].
문헌 [[10](/QAZKR/appendix/references.html#10)]에서는 무작위 양자 알고리즘에 대해서 다루었는데 질의 복잡도가 $\frac{1}{3}\log_2 N$보다 낮을 것으로 예상한다.
