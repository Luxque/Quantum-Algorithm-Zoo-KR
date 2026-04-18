# 들어가며

양자 컴퓨터는 우리가 일상적으로 사용하는 고전 컴퓨터보다 더욱 빠른 연산 능력을 약속합니다.
이에 따라 양자 컴퓨터에 직접적으로 실행해야 하는 양자 알고리즘에 대한 연구도 활발해지고 있습니다.
하지만, 대부분의 핵심 자료가 영어로 작성된 관계로 한국어가 모어인 사람이 심도 있는 양자 알고리즘을 학습하기가 어려운 실정입니다.
이러한 계기로 저는 양자 알고리즘 모음집인 [Quantum Algorithm Zoo](https://quantumalgorithmzoo.org/)를 한국어로 번역하게 되었습니다.

이 번역 프로젝트의 목표는 두 가지입니다:
1.  **접근성**: 언어의 장벽 없이 누구나 최신 양자 알고리즘 목록을 열람할 수 있도록 합니다.
2.  **정확성**: [한국수학회(KMS)](https://www.kms.or.kr/)와 [한국물리학회(KPS)](https://www.kps.or.kr/)의 표준 용어를 준수하여 학술적으로 더욱 정확한 번역을 제공합니다.

이 프로젝트는 [Quantum Algorithm Zoo](https://quantumalgorithmzoo.org/)에 소개된 알고리즘 설명문을 번역하는 것을 목표로 하지만 그 알고리즘을 제안한 논문의 번역까지 제공하지 못하는 점 양해 부탁드립니다.
그럼에도 더욱 심도 있는 학습을 위하여 원문과 참고문헌에 실려있는 자료들을 참조하여 주시길 바랍니다.
이 한국어 번역을 허락해 주신 [Stephen P. Jordan](https://scholar.google.com/citations?user=dcSsY4cAAAAJ&hl=en) 박사님께 깊은 감사를 표합니다.

## 일러두기

이 모음집에서는 알려진 가장 빠른 고전 알고리즘의 실행시간 $C(n)$과 양자 알고리즘의 실행시간 $Q(n)$이 $C = 2^{\Omega(Q^\alpha)}$을 만족하는 양의 상수 $\alpha$가 존재한다면, 이러한 속도향상을 초(超)다항적이라고 칭하도록 하겠습니다.
만약 아닐 경우, 다항적이라고 하겠습니다.
$O$, $\Omega$, $\Theta$, $\tilde{O}$, $\cdots$등과 같은 표기법은 [위키백과 문서](https://ko.wikipedia.org/wiki/%EC%A0%90%EA%B7%BC_%ED%91%9C%EA%B8%B0%EB%B2%95)를 참고하여 주시길 바랍니다.

## 기여하기

만약 번역문에 오류가 있거나 더욱 매끄러운 번역 제안이 있으시다면 이 프로젝트의 [이슈란](https://github.com/Luxque/Quantum-Algorithm-Zoo-KR/issues)에 문의를 남겨주십시오.
확인 후 최대한 조속히 수정 및 조치를 취하도록 하겠습니다.

만약 이 리포지터리에 동봉된 `script` Python 코드를 사용하시려면 다음 명령어를 입력하여 가상환경을 생성하시고 필수 패키지를 설치하십시오.

```bash
python3 -m venv .venv
source ./.venv/bin/activate
pip install tabulate
```

이 프로젝트를 위해 기여해주시는 모든 여러분께 깊이 감사드립니다.

## 출처

* 원문서: [Quantum Algorithm Zoo](https://quantumalgorithmzoo.org/)
* 원저자: [Stephen P. Jordan](https://scholar.google.com/citations?user=dcSsY4cAAAAJ&hl=en)
* 렌더링: [mdBook](https://github.com/rust-lang/mdBook), [mdBook-KaTeX](https://github.com/lzanini/mdbook-katex)
* 참고문헌: [참고문헌](/QAZKR/appendix/references.html)
