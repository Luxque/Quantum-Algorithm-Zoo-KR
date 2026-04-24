# 소인수분해

> * **영어 명칭**: Factoring
> * **속도 향상**: 초다항적
> * **구현 코드**: [Classiq](https://short.classiq.io/shor), [Cirq](https://github.com/quantumlib/Cirq/blob/main/examples/shor.py), [PennyLane](https://pennylane.ai/codebook/shors-algorithm), [Qrisp](https://qrisp.eu/reference/Algorithms/Shor.html#shor)

주어진 $n$비트 정수의 소인수분해를 찾는다.
피터 쇼어(Peter Shor)가 고안한 알고리즘은 이를 $O(n^3)$ 시간에 찾는다 [[82](/QAZKR/appendix/references.html#82), [125](/QAZKR/appendix/references.html#125)].
고전 알고리즘 중에서 소인수분해를 찾는 가장 빠른 알고리즘은 수체 체로, $2^{\tilde{O}(n^{1/3})}$의 시간에 이를 수행한다고 알려져있다.
[[252](/QAZKR/appendix/references.html#252), [362](/QAZKR/appendix/references.html#362)]에서 발전하여 수학적으로 엄밀하게 증명된 고전 소인수분해 알고리즘 중에서 최적의 상한은 [[542](/QAZKR/appendix/references.html#542)]에서 보이듯 $O(2^{n/5 + o(1)})$이다.
쇼어의 소인수분해 알고리즘은 RSA 암호를 무력화시키며, 이에 깊게 관련된 양자 이산 로그 알고리즘은 DSA/ECDSA 전자 서명 방식과 디피(Diffie)-헬먼(Hellman) 키 교환 프로토콜을 무력화한다.
특히 쇼어의 알고리즘보다 빠르게 반(半)소수의 소인수분해를 찾는 알고리즘은 암호학에 널리 쓰이고 있으며, 이는 [[271](/QAZKR/appendix/references.html#271)]에 설명되어 있다.
만약 작은 소인수가 존재한다면, 그로버(Grover) 탐색법을 이용한 양자 알고리즘이 타원곡선 소인수분해를 쇼어 알고리즘보다 더욱 빠르게 수행한다 [[366](/QAZKR/appendix/references.html#366)].
더 많은 최적화된 쇼어 알고리즘은 [[384](/QAZKR/appendix/references.html#384), [386](/QAZKR/appendix/references.html#386), [431](/QAZKR/appendix/references.html#431)]에서 찾을 수 있다.
양자 알고리즘으로도 무력화되지 않을 것으로 보이는 고전 공개키 암호 방식이 발의되어 있다 [[248](/QAZKR/appendix/references.html#248)].
쇼어 알고리즘의 핵심은 차수 찾기로, 양자 푸리에(Fourier) 변환을 통해 아벨 숨은 부분군 문제로 환산할 수 있다.
여러 다른 문제가 홀수 차수 상의 행렬군에 대한 원소 판정 문제를 포함한 소인수분해 문제와 양자 회로 합성에 관련된 일부 디오판토스(Diophantine) 방정식 문제로 환산 가능하다고 알려져 있다 [[254](/QAZKR/appendix/references.html#254)].
