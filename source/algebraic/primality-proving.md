# 소수 판정

> * **영어 명칭**: Primality Proving
> * **속도 향상**: 다항적
> * **구현 코드**: ∅

$n$비트의 정수가 주어져 있을 때 소수 여부를 판정한다.
고전 알고리즘 중에서 가장 빠른 것은 AKS로 복잡도는 사실상 4차이고, ECPP도 가장 빠른 것의 휴리스틱 복잡도는 사실상 4차이다.
가장 빠른 양자 알고리즘은 도니스-벨라(Donis-Vela)와 가르시아-에스카르틴(Garcia-Escartin)이 제안한 방법으로 [[396](/QAZKR/appendix/references.html#396)], $O(n^2(\log n)^3\log\log n)$의 복잡도를 가진다.
이 알고리즘은 이전 $O(n^3\log n \log\log n)$의 복잡도를 가진 소인수분해에 기반한 양자 알고리즘에서 발전된 것이다 [[397](/QAZKR/appendix/references.html#397)].
최근에 발표된 하비(Harvey)와 반 데르 호벤(Van Der Hoeven)의 결과에 따르면 [[398](/QAZKR/appendix/references.html#398)], 소인수분해에 기반한 양자 알고리즘의 복잡도가 $O(n^3\log n)$까지 향상될 수 있다고 하며, 이와 비슷하게 도니-벨라-가르시아-에스카르틴 알고리즘의 복잡도를 $O(n^2(\log n)^3)$까지 낮출 수 있다고 한다 [[399](/QAZKR/appendix/references.html#399)]. 
