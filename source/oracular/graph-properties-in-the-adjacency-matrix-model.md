# 인접 행렬 모델 상에서의 그래프 성질

> * **영어 명칭**: Graph Properties in the Adjacency Matrix Model
> * **속도 향상**: 다항적
> * **구현 코드**: (없음)

$G$를 $n$개의 꼭짓점으로 이루어진 그래프라고 하자.
$\{1, 2, \cdots, n\}$에 속한 정수의 쌍을 주면 해당하는 꼭짓점들이 모서리로 이어졌는지를 알려주는 오라클이 주어져 있다.
선행 연구 [[35](/QAZKR/appendix/references.html#35), [52](/QAZKR/appendix/references.html#52), [36](/QAZKR/appendix/references.html#36)]에 기반하여, 뒤르(Dürr) 등[[34](/QAZKR/appendix/references.html#34)]은 최소 생성나무 찾기와 유향그래프 및 무향그래프의 연결성을 판별하는 것은 $\Theta(n^{3/2})$, 최소의 가중 경로를 찾는 것은 $O(n^{3/2}\log^2 n)$의 양자 질의 복잡도를 가짐을 보였다.
[[13](/QAZKR/appendix/references.html#13), [272](/QAZKR/appendix/references.html#272), [318](/QAZKR/appendix/references.html#218)]에서 발전한 [[317](/QAZKR/appendix/references.html#317)]은 이분그래프 판별하기, 순환 판별하기, 주어진 꼭짓점이 다른 꼭짓점으로부터 닿을 수 있는지를 판별하기(st-연결성)는 $\tilde{O}(n^{3/2})$로 늘어나는 질의와 양자 게이트, 로그로 늘어나는 큐비트로 풀 수 있음을 보였다.
$\tilde{O}(n)$ 시간에 주어진 크기의 트리를 마이너(minor) 탐지하는 스팬 프로그램에 기초한 양자 알고리즘은 [[240](/QAZKR/appendix/references.html#240)]에 제시되어 있다.
만약 어떠한 성질을 갖고 있는 모든 그래프의 모서리와 꼭짓점의 비율이 거의 $c$인 상수 $c$가 존재한다면, 그 그래프의 성질은 희박하다고 한다.
차일즈(Childs)와 코타리(Kothari)는 만약 모든 희박한 성질이 금지된 부분그래프의 나열로 특정될 수 없을 경우의 질의 복잡도는 $\Theta(n^{2/3})$이고, 만약 가능하다면 $o(n^{2/3})$([스몰-o 표기법](https://ko.wikipedia.org/wiki/%EC%A0%90%EA%B7%BC_%ED%91%9C%EA%B8%B0%EB%B2%95#%EC%8A%A4%EB%AA%B0-o_%ED%91%9C%EA%B8%B0%EB%B2%95))가 됨을 보였다 [[140](/QAZKR/appendix/references.html#140)].
전자의 알고리즘은 그로버(Grover) 탐색에 기초했고 [[140](/QAZKR/appendix/references.html#140)], 후자는 양자 보행 형식론에 기초한다 [[141](/QAZKR/appendix/references.html#141)].
마더(Mader)의 정리에 의해 희박한 그래프 성질은 모든 비자명한 마이너에 대해 닫힌 성질을 포함한다.
이러한 성질에는 평면성, 숲의 성질, 주어진 길이의 경로를 포함하지 않는 성질 등이 있다.
폭넓게 믿어지고 있는 안데라(Aanderaa)-카프(Karp)-로젠베르크(Rosenberg) 추측에 의하면 위의 모든 문제는 $\Omega(n^2)$의 고전적 질의 복잡도를 가진다고 한다.
또 다른 흥미로운 문제는 주어진 그래프 $G$에서 부분그래프 $H$를 찾는 것이다.
이 문제의 가장 간단한 경우는 삼각형을 찾는 것으로, 즉 크기가 3인 클리크를 찾는 것이다.
[[276](/QAZKR/appendix/references.html#276), [175](/QAZKR/appendix/references.html#175), [171](/QAZKR/appendix/references.html#171), [70](/QAZKR/appendix/references.html#70), [152](/QAZKR/appendix/references.html#152), [21](/QAZKR/appendix/references.html#21)]에서 발전된 알려진 가장 빠른 양자 알고리즘은 이를 $O(n^{5/4})$ 양자 질의로 찾는다 [[319](/QAZKR/appendix/references.html#319)].
그래프가 충분히 희박할 때의 더욱 강력한 양자 질의 복잡도 상한도 알려져 있다 [[319](/QAZKR/appendix/references.html#319), [320](/QAZKR/appendix/references.html#320)].
고전적으로 삼각형을 찾기 위해서는 $\Omega(n^2)$개의 질의가 필요하다 [[21](/QAZKR/appendix/references.html#21)].
더 일반적으로, 양자 컴퓨터는 임의의 꼭짓점이 $k$개인 부분그래프 $H$를 $O(n^{2-2/k-t})$개의 질의로 찾을 수 있다 (여기에서 $t = (2k-d-3)/(k(d+1)(m+2))$이고, $H$에는 차수가 $d$인 꼭짓점과 $m+d$개의 모서리가 있음).
이는 이전의 알고리즘 [[70](/QAZKR/appendix/references.html#70)]에서 발전된 것이다.
몇몇 경우에는 이 알고리즘보다 [[140](/QAZKR/appendix/references.html#140)]의 알고리즘이 더 나은 성능을 보이는데, $G$가 희박할 때 $\tilde{O}(n^{\frac{3}{2}-\frac{1}{\operatorname{vc}(H)+1}})$개의 질의로 $H$를 찾는다 (여기에서 $\operatorname{vc}(H)$는 $H$의 최소 꼭짓점 덮개의 개수를 의미함).
3-균일 하이퍼그래프 상에서 상수 크기의 부분하이퍼그래프를 $O(n^{1.883})$개의 질의로 찾는 양자 알고리즘은 [[241](/QAZKR/appendix/references.html#241)]에 제시되어 있다.
