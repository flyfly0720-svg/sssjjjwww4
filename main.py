
# YAP/TAZ 과활성화는 비만 관련 암 위험의 핵심 기전인가: Hippo 경로 이중성과 대사 조절 전략의 재탐색

## 1. 서론: 탐구 동기 및 목적

2학년 진로활동에서 예방적 관점의 비만 치료 전략으로 Hippo 경로 조절, 구체적으로는 LATS 억제를 통한 YAP/TAZ 활성화 유도 방안을 제안한 바 있다. 그러나 이 제안을 되짚어보는 과정에서, YAP/TAZ가 다수의 암종에서 종양원성 인자로 보고되어 있다는 사실을 접하면서 하나의 의문이 생겼다. 지방세포의 YAP/TAZ를 인위적으로 활성화하는 전략이 비만은 개선하되 암 발병 위험을 함께 높이는 것은 아닌가 하는 것이었다. 이 문제의식은 곧 검증 가능한 가설로 구체화되었다. 'YAP/TAZ 활성도가 높을수록 암 발병률도 높게 나타날 것이다'라는 가설을 세우고, 이를 공개된 대규모 유전자 발현 데이터베이스를 통해 실제로 검증해 보고자 한 것이 이 탐구의 출발점이다.

아래 그림은 문제의식에서 최종 결론에 이르기까지 탐구가 전개된 전체 흐름을 나타낸 것이다.

<svg viewBox="0 0 780 1070" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <defs>
    <marker id="arrow1" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L8,3 z" fill="#4a6fa5"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="780" height="1070" fill="#ffffff"/>

  <rect x="40" y="20" width="700" height="100" rx="10" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="60" y="46" font-size="15" font-weight="bold" fill="#1f3864">① 문제의식</text>
  <text x="60" y="70" font-size="13" fill="#333">비만 치료를 위해 YAP/TAZ를 활성화하는 것이</text>
  <text x="60" y="90" font-size="13" fill="#333">오히려 암 발병 위험을 높이는 것은 아닐까?</text>
  <line x1="390" y1="120" x2="390" y2="168" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow1)"/>

  <rect x="40" y="170" width="700" height="100" rx="10" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="60" y="196" font-size="15" font-weight="bold" fill="#1f3864">② 이론적 학습 (분자세포생물학 전공서)</text>
  <text x="60" y="220" font-size="13" fill="#333">Hippo 경로: LATS 억제 → YAP/TAZ 과활성화</text>
  <text x="60" y="240" font-size="13" fill="#333">→ TEAD 결합 → 암 발병 가능성이라는 이론적 서사 확인</text>
  <line x1="390" y1="270" x2="390" y2="318" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow1)"/>

  <rect x="40" y="320" width="700" height="100" rx="10" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="60" y="346" font-size="15" font-weight="bold" fill="#1f3864">③ 가설 검증 설계</text>
  <text x="60" y="370" font-size="13" fill="#333">GEPIA2의 TCGA 범암 데이터 활용</text>
  <text x="60" y="390" font-size="13" fill="#333">대리지표: CTGF · CYR61 · WWTR1 발현량으로 경로 활성도 추정</text>
  <line x1="390" y1="420" x2="390" y2="468" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow1)"/>

  <rect x="40" y="470" width="700" height="100" rx="10" fill="#fdeeee" stroke="#a54a4a" stroke-width="1.5"/>
  <text x="60" y="496" font-size="15" font-weight="bold" fill="#7a1f1f">④ 결과: 예상과 반대</text>
  <text x="60" y="520" font-size="13" fill="#333">YAP/TAZ 표적유전자 발현과 암종별 발병률 간</text>
  <text x="60" y="540" font-size="13" fill="#333">뚜렷한 양의 상관관계가 나타나지 않음</text>
  <line x1="390" y1="570" x2="390" y2="618" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow1)"/>

  <rect x="40" y="620" width="700" height="100" rx="10" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="60" y="646" font-size="15" font-weight="bold" fill="#1f3864">⑤ 원인 분석</text>
  <text x="60" y="670" font-size="13" fill="#333">전사체 발현량 ≠ 단백질 활성화 수준 (층위 차이)</text>
  <text x="60" y="690" font-size="13" fill="#333">지방조직이 아닌 기존 암조직 발현 데이터를 대체 사용</text>
  <line x1="390" y1="720" x2="390" y2="768" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow1)"/>

  <rect x="40" y="770" width="700" height="120" rx="10" fill="#eaf3ea" stroke="#4a7a4a" stroke-width="1.5"/>
  <text x="60" y="796" font-size="15" font-weight="bold" fill="#1f4a1f">⑥ 재해석 (핵심 통찰)</text>
  <text x="60" y="820" font-size="13" fill="#333">YAP/TAZ는 TEAD 결합(증식 촉진)과</text>
  <text x="60" y="840" font-size="13" fill="#333">BIM 억제(세포사멸 저지)라는 별개의 두 축을 가짐</text>
  <text x="60" y="862" font-size="13" fill="#333">→ 세포 분열 활성도만으로 암 발생률 단정 불가</text>
  <line x1="390" y1="890" x2="390" y2="938" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow1)"/>

  <rect x="40" y="940" width="700" height="100" rx="10" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="60" y="966" font-size="15" font-weight="bold" fill="#1f3864">⑦ 확장: 새로운 전략 제안</text>
  <text x="60" y="990" font-size="13" fill="#333">단일 분자 표적을 조작하는 대신</text>
  <text x="60" y="1010" font-size="13" fill="#333">자가포식 · 간헐적 단식 · 생체시계 리듬 기반 대사 조절 제안</text>
</svg>

## 2. 이론적 배경

### 2.1 Hippo 신호전달경로와 YAP/TAZ

Hippo 경로는 MST1/2-LATS1/2로 이어지는 인산화 연쇄반응을 통해 전사보조활성인자 YAP과 TAZ의 활성을 억제하는 종양억제 경로로 알려져 있다(Meng, Moroishi & Guan, 2016). Hippo 신호가 켜져 있으면 LATS가 YAP/TAZ를 인산화해 세포질에 붙잡아 두거나 분해를 유도하지만, 세포 밀도 저하나 기계적 신호 변화 등으로 Hippo 신호가 꺼지면 LATS 활성이 억제되어 YAP/TAZ가 인산화되지 않은 채 핵으로 이동한다. 핵으로 이동한 YAP/TAZ는 스스로 DNA에 결합하는 능력이 없어 TEAD 전사인자와 복합체를 이루어야 표적유전자를 발현시킬 수 있는데, 이때 대표적으로 유도되는 유전자가 CTGF, CYR61, WWTR1 등이다(Zanconato, Cordenonsi & Piccolo, 2016). 이 YAP/TAZ-TEAD-표적유전자 축이 세포 증식과 생존을 촉진해 다수의 암종에서 종양원성 경로로 작용한다는 것이 통상적으로 알려진 서사다.

### 2.2 비만과 YAP/TAZ 활성화: 가설의 출발점

지방세포 분화 및 지방 저장 억제에 YAP/TAZ가 관여한다는 점에서, 비만 치료의 한 축으로 YAP/TAZ 활성화 전략이 제안되어 왔다. 그러나 위 2.1의 서사를 그대로 적용하면, 지방조직에서 YAP/TAZ를 활성화하는 개입이 다른 조직에서의 종양원성 신호와 동일한 방향으로 작용해 암 발병 위험을 함께 높일 수 있다는 우려가 성립한다. 실제로 비만 자체가 여러 암종의 위험비(hazard ratio)를 높인다는 대규모 역학 연구도 보고되어 있어(Bhaskaran et al., 2014), 비만-YAP/TAZ-암이라는 세 항이 하나의 인과 사슬로 연결될 가능성은 이론적으로 충분히 검토할 만한 가설이었다.

## 3. 탐구 방법

### 3.1 데이터베이스 및 분석 도구

가설을 검증하기 위해 TCGA(The Cancer Genome Atlas)의 범암(pan-cancer) 발현 데이터를 시각화·분석할 수 있는 웹 서버인 GEPIA2를 활용하였다(Tang et al., 2019). GEPIA2는 TCGA와 GTEx의 종양·정상조직 발현 데이터를 기반으로 유전자별 발현량을 암종별로 비교할 수 있는 인터페이스를 제공한다.

### 3.2 대리 지표의 설정

애초의 계획은 YAP/TAZ 자체의 활성도(핵 내 존재비 또는 인산화 상태)를 암종별 발병률과 직접 비교하는 것이었다. 그러나 GEPIA2를 비롯한 공개 발현 데이터베이스에는 전사보조활성인자인 YAP/TAZ 단백질 자체의 활성 수준을 직접 나타내는 지표가 존재하지 않는다는 한계에 부딪혔다. 이를 보완하기 위해, YAP/TAZ-TEAD 결합에 의해 발현이 유도되는 대표적 표적유전자인 CTGF, CYR61, WWTR1의 mRNA 발현량을 YAP/TAZ 경로 활성도의 대리 지표로 설정하였다. 즉 표적유전자의 발현이 높을수록 상류의 YAP/TAZ-TEAD 경로 역시 활성화되어 있을 것이라는 논리로 지표를 우회적으로 구성한 것이다.

### 3.3 분석 절차

GEPIA2의 TCGA 범암 데이터를 이용해 CTGF·CYR61·WWTR1의 발현량을 암종별로 비교하고, 이를 각 암종의 발병률 지표와 대응시켜 상관관계를 분석하였다.

## 4. 탐구 결과

분석 결과는 애초의 가설과 반대 방향으로 나타났다. YAP/TAZ 표적유전자 발현이 높게 관찰된 암종이 반드시 발병률이 높은 암종과 일치하지 않았으며, 오히려 일부 구간에서는 음의 상관 경향이 관찰되었다. 즉 'YAP/TAZ 활성도가 높을수록 암 발병률도 높다'는 단순한 선형적 관계는 데이터상으로 지지되지 않았다.

## 5. 논의

### 5.1 예상과 다른 결과의 원인

이 반박 결과의 원인을 두 가지 층위에서 분석하였다. 첫째, 전사체 발현량과 단백질 활성화 수준 사이에는 층위 차이가 존재한다. mRNA 발현이 높다는 것이 곧 해당 단백질이 인산화되지 않은 활성 상태로 핵에 존재한다는 것을 의미하지 않는다. YAP/TAZ의 활성은 전사 이후 단계인 인산화·핵 이동이라는 번역 후 조절에 의해 최종적으로 결정되므로, mRNA 발현량만으로 경로 활성도를 추정하는 것 자체에 근본적인 간극이 있었다. 둘째, GEPIA2의 발현 데이터는 지방조직이 아닌 기존에 형성된 각 암종의 종양 조직에서 얻어진 것이다. 애초의 가설은 '지방조직에서 YAP/TAZ를 활성화했을 때'를 전제로 한 것인데, 실제 비교에 사용된 데이터는 지방조직이 아닌 이미 발생한 종양조직의 발현값이었다는 점에서 가설의 전제와 검증에 사용된 데이터의 성격이 서로 어긋나 있었다.

이 외에도 몇 가지 추가적인 오차 요인을 후속 논의로 남긴다. TCGA는 종양 덩어리 전체를 갈아 시퀀싱하는 벌크(bulk) RNA-seq 데이터이므로, CTGF·CYR61처럼 종양미세환경의 섬유아세포에서도 강하게 발현되는 유전자의 경우 종양세포 고유의 신호가 아닌 기질 조성 차이가 값에 섞여 들어갔을 가능성이 있다. 또한 CTGF·CYR61은 YAP/TAZ-TEAD 경로에 배타적인 표적유전자가 아니라 TGF-β 신호 등 다른 경로에 의해서도 유도될 수 있어, 대리 지표 자체의 특이성이 완전하지 않았을 가능성도 있다.

### 5.2 YAP/TAZ의 이중적 역할이 갖는 함의

원인 분석과 별개로, YAP/TAZ가 세포 안에서 수행하는 역할 자체가 단순히 '증식 촉진'으로 환원되지 않는다는 점도 확인하였다. YAP/TAZ는 핵 내에서 TEAD와 결합해 증식 관련 유전자 발현을 촉진하는 동시에, 세포사멸 관련 경로에도 관여해 생존 신호를 강화하는 것으로 보고되어 있다(LeBlanc, Ramirez & Kim, 2021). 즉 증식 촉진과 생존·사멸 조절은 YAP/TAZ가 수행하는 서로 구별되는 두 축이다. 아래 그림은 이 두 축이 하나의 상류 신호(TEAD 결합)에서 갈라져 나가는 구조를 나타낸 것이다.

<svg viewBox="0 0 760 720" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <defs>
    <marker id="arrow2" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L8,3 z" fill="#4a6fa5"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="760" height="720" fill="#ffffff"/>

  <rect x="230" y="20" width="300" height="60" rx="8" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="380" y="55" font-size="14" text-anchor="middle" fill="#1f3864">Hippo 신호 OFF (LATS 억제)</text>
  <line x1="380" y1="80" x2="380" y2="108" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow2)"/>

  <rect x="230" y="110" width="300" height="60" rx="8" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="380" y="145" font-size="14" text-anchor="middle" fill="#1f3864">YAP/TAZ 탈인산화 · 핵 이동</text>
  <line x1="380" y1="170" x2="380" y2="198" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow2)"/>

  <rect x="230" y="200" width="300" height="60" rx="8" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="380" y="235" font-size="14" text-anchor="middle" fill="#1f3864">TEAD와 결합 (전사보조인자)</text>

  <line x1="380" y1="260" x2="210" y2="298" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow2)"/>
  <line x1="380" y1="260" x2="550" y2="298" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow2)"/>

  <rect x="60" y="300" width="300" height="60" rx="8" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="210" y="328" font-size="13" text-anchor="middle" fill="#1f3864">증식 유전자 발현 촉진</text>
  <text x="210" y="348" font-size="12" text-anchor="middle" fill="#333">(CTGF · CYR61 · WWTR1)</text>

  <rect x="400" y="300" width="300" height="60" rx="8" fill="#f7eeee" stroke="#a54a4a" stroke-width="1.5"/>
  <text x="550" y="335" font-size="13" text-anchor="middle" fill="#7a1f1f">BIM 발현 억제</text>

  <line x1="210" y1="360" x2="210" y2="398" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow2)"/>
  <line x1="550" y1="360" x2="550" y2="398" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow2)"/>

  <rect x="60" y="400" width="300" height="60" rx="8" fill="#eef2f7" stroke="#4a6fa5" stroke-width="1.5"/>
  <text x="210" y="435" font-size="13" text-anchor="middle" fill="#1f3864">[증식 축] 세포 증식 촉진</text>

  <rect x="400" y="400" width="300" height="60" rx="8" fill="#f7eeee" stroke="#a54a4a" stroke-width="1.5"/>
  <text x="550" y="435" font-size="13" text-anchor="middle" fill="#7a1f1f">[생존 축] 세포사멸 저지</text>

  <line x1="210" y1="460" x2="380" y2="498" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow2)"/>
  <line x1="550" y1="460" x2="380" y2="498" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow2)"/>

  <rect x="230" y="500" width="300" height="60" rx="8" fill="#eaf3ea" stroke="#4a7a4a" stroke-width="1.5"/>
  <text x="380" y="535" font-size="13" text-anchor="middle" fill="#1f4a1f">종양원성에 기여 (증식 축 + 생존 축)</text>
  <line x1="380" y1="560" x2="380" y2="588" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrow2)"/>

  <rect x="40" y="590" width="680" height="110" rx="8" fill="#fff8e6" stroke="#b8860b" stroke-width="1.5"/>
  <text x="380" y="618" font-size="13" text-anchor="middle" font-weight="bold" fill="#6b4f00">⚠ 핵심 통찰</text>
  <text x="380" y="642" font-size="12.5" text-anchor="middle" fill="#333">세포 분열 활성도(증식 축)만 측정하면 생존 축(BIM 억제)의 기여를 놓치게 되어,</text>
  <text x="380" y="662" font-size="12.5" text-anchor="middle" fill="#333">단일 지표만으로는 YAP/TAZ의 전체 종양원성과 암 발생률을 단정할 수 없다.</text>
</svg>

세포 분열 활성도만으로 암 발생률을 단정할 수 없다는 결론은 이 두 축의 분기 구조에서 자연스럽게 도출된다.

### 5.3 탐구의 한계

대리 지표를 이용한 우회적 검증이라는 방법론적 한계, 그리고 mRNA 발현량과 단백질 활성 수준의 층위 차이를 완전히 통제하지 못했다는 한계는 이 탐구가 안고 있는 근본적인 제약이다. 인산화 특이적 항체를 이용한 단백질 수준의 정량, 혹은 단일세포 수준의 지방조직 발현 데이터를 확보할 수 있다면 보다 정밀한 검증이 가능할 것이다.

## 6. 결론 및 확장: 대사 조절 기반 비만 치료 전략

이상의 분석을 종합하면, YAP/TAZ 과활성화가 암 발병의 핵심 원인이라는 애초의 가설은 성립하지 않으며, 단일 분자·단일 지표에 근거해 치료 전략의 위험성을 단정하는 접근에는 한계가 있다는 결론에 이르렀다. 이 지점에서 탐구의 방향을 특정 분자 표적 하나를 조작하는 방식에서, 인체가 이미 갖추고 있는 대사 조절 시스템을 활용하는 방향으로 전환하였다.

에너지가 부족한 상태에서 세포가 손상된 세포내 구성요소를 분해·재활용하는 자가포식(autophagy) 과정이 촉진된다는 점에 주목하였다. 자가포식은 대사 항상성 유지와 세포 손상 억제에 기여하는 것으로 보고되어 있으며(de Cabo & Mattson, 2019), 공복 상태에서 인슐린·mTOR 신호가 낮아지면서 자연스럽게 유도된다. 기존의 비만 치료제들이 특정 분자를 표적으로 삼는 과정에서 예상치 못한 부작용을 동반할 수 있다는 점을 함께 고려하면, 간헐적 단식과 생체 시계 리듬을 연계해 자가포식을 유도하는 대사 조절 방식이 특정 유전자를 직접 조작하는 전략보다 장기적으로 더 안전한 비만 치료 전략이 될 수 있다는 결론에 도달하였다. 이는 하나의 분자를 표적으로 삼아 '켜고 끄는' 접근이 아니라, 인체가 진화적으로 갖추어 온 대사 전환 스위치를 시간생물학적으로 활용하는 접근이라는 점에서 애초의 YAP/TAZ 표적 전략과 근본적인 방향을 달리한다.

## 참고문헌

1. Tang, Z., Kang, B., Li, C., Chen, T., & Zhang, Z. (2019). GEPIA2: an enhanced web server for large-scale expression profiling and interactive analysis. *Nucleic Acids Research*, 47(W1), W556–W560.
2. Zanconato, F., Cordenonsi, M., & Piccolo, S. (2016). YAP/TAZ at the roots of cancer. *Cancer Cell*, 29(6), 783–803.
3. Meng, Z., Moroishi, T., & Guan, K. L. (2016). Mechanisms of Hippo pathway regulation. *Genes & Development*, 30(1), 1–17.
4. LeBlanc, L., Ramirez, N., & Kim, J. (2021). Context-dependent roles of YAP/TAZ in stem cell fates and cancer. *Cellular and Molecular Life Sciences*, 78.
5. Bhaskaran, K., Douglas, I., Forbes, H., dos-Santos-Silva, I., Leon, D. A., & Smeeth, L. (2014). Body-mass index and risk of 22 specific cancers: a population-based cohort study of 5·24 million UK adults. *The Lancet*, 384(9945), 755–765.
6. de Cabo, R., & Mattson, M. P. (2019). Effects of Intermittent Fasting on Health, Aging, and Disease. *New England Journal of Medicine*, 381(26), 2541–2551.
