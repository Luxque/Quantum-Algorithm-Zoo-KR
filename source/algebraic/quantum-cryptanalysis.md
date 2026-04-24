# 양자 암호 해독

> * **영어 명칭**: Quantum Cryptoanalysis
> * **속도 향상**: 상이함
> * **구현 코드**: ∅

쇼어(Shor) 알고리즘과 이산 로그 알고리즘이 [[82](/QAZKR/appendix/references.html#82), [125](/QAZKR/appendix/references.html#125)] RSA 암호화와 타원 곡선 응용을 포함한 [[109](/QAZKR/appendix/references.html#109), [14](/QAZKR/appendix/references.html#14)] 디피(Diffie)-헬먼(Hellman) 암호 체계를 완전히 무력화시킬 수 있다는 것은 잘 알려진 사실이다.
(수많은 '양자 후 암호' 공개키 암호 체계는 이러한 기존의 체계를 대체하기 위해 제시되었으며, 양자 공격에도 취약하지 않을 것으로 알려져 있다.)
쇼어 알고리즘 말고도 암호 체계 뚫기 위한 양자 알고리즘의 연구가 활발히 진행 중이다.
대체로 세 개의 유형으로 분류될 수 있다.
첫 번째는 기존의 가정하에 다항 및 준지수 시간 양자 알고리즘을 제시하는 것이다.
특히 차일즈(Childs), 자오(Jao), 수하레프(Soukharev)가 제시한 알고리즘은 타원곡선의 동류사상을 준지수 시간에 찾아내 쇼어 알고리즘은 불가능했던 특정 타원 곡선 암호 체계를 무력화시킨다 [[283](/QAZKR/appendix/references.html#283)].
엘다(Eldar)와 홀그렌(Hallgren)이 제시한 양자 알고리즘은 특정 격자 문제[[537](/QAZKR/appendix/references.html#537)]의 해를 제공하며, 문제 사례의 매개변수 영역이 적절하게 책정된다면 고전 알고리즘 대비 속도 향상을 기대할 수 있다 [[538](/QAZKR/appendix/references.html#538)].
다변수 암호 체계에 대해 고전 공격 방식 대비하여 강점이 확실히 알려지지 않은 양자 공격 방식은 [[539](/QAZKR/appendix/references.html#539), [540](/QAZKR/appendix/references.html#540), [541](/QAZKR/appendix/references.html#541)]에 제시되어 있다.
두 번째 유형은 그로버(Grover) 탐색 알고리즘 및 양자 중복 감지법(quantum collision finding) 등을 활용해 고전 알고리즘 구성 요소의 속도를 향상해 고전 공격 대비 다항적 속도 향상을 달성하는 것이다.
이러한 공개키와[[284](/QAZKR/appendix/references.html#284), [285](/QAZKR/appendix/references.html#285), [288](/QAZKR/appendix/references.html#288), [315](/QAZKR/appendix/references.html#315), [316](/QAZKR/appendix/references.html#316)]과 비공개키[[262](/QAZKR/appendix/references.html#262), [287](/QAZKR/appendix/references.html#287), [536](/QAZKR/appendix/references.html#536)]기본 요소에 대한 공격은 관련 암호 체계의 사용을 배제하지 않지만, 키 크기의 선택에는 영향을 줄 수 있다.
세 번째 유형은 양자 중첩 쿼리를 통한 암호 방지 공격이다.
이러한 공격은 많은 경우 암호 기본 요소들을 완전히 무력화한다 [[290](/QAZKR/appendix/references.html#290), [291](/QAZKR/appendix/references.html#291), [292](/QAZKR/appendix/references.html#292)].
하지만 실질적으로 이러한 중첩 쿼리는 실현될 수 없다.
