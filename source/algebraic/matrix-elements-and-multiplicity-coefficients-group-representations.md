# 군 표현의 행렬 원소와 중복도 계수

> * **영어 명칭**: Matrix Elements and Multiplicity Coefficients of Group Representations
> * **속도 향상**: 초다항적
> * **구현 코드**: ∅

유한군의 모든 표현과 콤팩트 선형군은 적절한 기저가 주어져 있을 때 유니터리행렬로 쓸 수 있다.
군 상에서 양자 푸리에(Fourier) 변환을 통해 정칙표현의 켤레를 구하면 그 군의 기약표현 직합이 나온다.
그러므로 아다마르(Hadamard) 테스트를 동반한 대칭군 상에서의 효율적인 양자 푸리에 변환은 [[196](/QAZKR/appendix/references.html#196)] $S_n$의 임의 기약표현의 행렬 원소를 각각 가법적으로 근사하는 빠른 양자 알고리즘을 산출한다.
이와 비슷하게 양자 슈어(Schur) 변환을 이용하면 [[197](/QAZKR/appendix/references.html#197)] $\operatorname{SU}(n)$의 기약표현 행렬 원소를 효율적으로 근사할 수 있다.
효율적인 양자 알고리즘을 통한 군 $\operatorname{U}(n)$, $\operatorname{SU}(n)$, $\operatorname{SO}(n)$, $A_n$ 상 개별표현의 구현은 [[106](/QAZKR/appendix/references.html#106)]에 설명되어 있다.
알려진 고전 알고리즘으로 해결하기 지수적으로 어려운 예시들도 [[106](/QAZKR/appendix/references.html#106)]에 설명되어 있다.
크로네커(Kronecker) 계수는 주어진 기약표현 쌍의 텐서곱 상에서 기약표현의 중복도를 산출한다.
대칭군에서의 정규화된 크로네커 계수는 다항 시간 양자 알고리즘으로 가법적인 다항식 역수 오차 내로 근사할 수 있지만, 이를 수행하는 다항 시간 고전 알고리즘은 알려지지 않았다 [[460](/QAZKR/appendix/references.html#460)].
이러한 양자 알고리즘을 통한 속도 향상은 대칭군 상에서의 다른 중복도 계수에 대해서도 일반화 되어있다 [[516](/QAZKR/appendix/references.html#516)].
또 이러한 결과를 뒷받침하여 크로네커 계수와 다른 중복도 계수를 계산하는 고전 알고리즘이 향상되었다 [[515](/QAZKR/appendix/references.html#515)].
하지만 [[516](/QAZKR/appendix/references.html#516)]에서 논했듯이 고전 알고리즘의 발전이 중복도 계수를 근사하는 모든 양자 알고리즘을 대체할 수는 없다.
