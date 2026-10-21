"""800 new original questions: 80 equation templates, ten stated conditions each.
No textbook, past-paper text or unverified statutory thresholds are used.
"""
import math


def extend_bank(add, subjects):
    def put(s, family, i, topic, prompt, value, unit, working, inputs):
        # General assumptions are in each prompt. Every explanation shows units,
        # substituted inputs, and the final rounded result (added by add()).
        q = add(subjects[s], family, i, topic, prompt, value, unit, working, inputs)
        q["sourceUrl"] = "https://github.com/YunSangYeong/Engineer-Electricity-CBT/blob/feat/question-bank-1000-20261021/docs/question-review.md"

    for i in range(10):
        n = i + 1
        # Electric and magnetic fields: 16 new families, 160 questions.
        put(0, 'point-potential', i, '점전하 전위',
            f'진공 중 +{n} μC 점전하에서 2 m 떨어진 점의 전위는? 무한원 전위는 0, 쿨롱 상수는 9×10⁹ N·m²/C²이다.',
            9*n/2, 'kV', f'점전하 전위 V=kq/r이다. q={n}×10⁻⁶ C를 넣으면 V=9×10⁹×{n}×10⁻⁶/2 V이다. V를 1,000으로 나누어 kV로 환산한다. 전위는 전계와 달리 거리의 제곱이 아닌 거리에 반비례한다.', [n, 2])
        put(0, 'coulomb-force', i, '쿨롱 법칙',
            f'진공 중 +{n} μC와 +2 μC 점전하가 0.1 m 떨어져 있다. 두 전하 사이 반발력의 크기는? k=9×10⁹ N·m²/C²이다.',
            1.8*n, 'N', f'F=k|q₁q₂|/r²=9×10⁹×({n}×10⁻⁶)×(2×10⁻⁶)/0.1² N이다. 두 전하는 같은 부호여서 반발한다. μC의 변환을 두 번 적용한다.', [n, 2, .1])
        c, v = 2*n, 10
        put(0, 'electric-energy', i, '전계 에너지',
            f'정전용량 {c} μF인 이상 콘덴서를 10 V로 충전했다. 저장 에너지는?',
            .5*c*1e-6*v*v*1000, 'mJ', f'전계 에너지 W=CV²/2이다. C={c}×10⁻⁶ F, V=10 V를 대입하면 W=({c}×10⁻⁶)×10²/2 J이다. J에 1,000을 곱하여 mJ로 표시한다.', [c, v])
        e = 10+2*i
        put(0, 'dielectric-flux', i, '전속밀도',
            f'선형 등방 유전체의 비유전율은 4이고 균일 전계는 {e} kV/m이다. 전속밀도 D의 크기는? ε₀=8.854×10⁻¹² F/m이다.',
            4*8.854e-12*e*1000*1e6, 'μC/m²', f'D=εE=ε₀εrE이다. E={e}×10³ V/m이므로 D=8.854×10⁻¹²×4×{e}×10³ C/m²이다. C/m²에서 μC/m²로 10⁶배 환산한다.', [4, e])
        a = 5*n
        put(0, 'field-integral', i, '전계와 전위차',
            f'x축 전계가 Eₓ(x)={a}x V/m이다(x의 단위 m). x=0과 x=2 m 사이 전위차 V(0)−V(2)는?',
            2*a, 'V', f'V(0)−V(2)=∫₀²Eₓdx=∫₀²{a}x dx이다. 적분하면 {a}×[x²/2]₀²={a}×2 V이다. 전계 방향으로 이동하면 전위가 낮아지므로 주어진 차이는 양수이다.', [a, 2])
        r = 2*n
        put(0, 'sphere-capacitance', i, '고립 도체 구',
            f'진공 속 반지름 {r} cm의 고립 도체 구의 정전용량은? 기준 전위는 무한원, ε₀=8.854×10⁻¹² F/m, π=3.141592653589793이다.',
            4*math.pi*8.854e-12*r*.01*1e12, 'pF', f'고립 도체 구에서 V=Q/(4πε₀r)이므로 C=Q/V=4πε₀r이다. r={r}/100 m를 대입한다. 결과 F에 10¹²을 곱하여 pF로 표시한다. 접지된 동심 구의 정전용량과는 구별한다.', [r])
        area = .01+.002*i
        put(0, 'layered-capacitor', i, '다층 유전체',
            f'면적 {area:g} m²의 평행판 사이에 두 유전체가 전계 방향으로 직렬 배치되어 있다. 두께/비유전율은 각각 1 mm/2, 2 mm/4이다. 가장자리 효과를 무시할 때 합성 정전용량은? ε₀=8.854×10⁻¹² F/m이다.',
            8.854e-12*area/(.001/2+.002/4)*1e12, 'pF', f'각 층의 전압강하를 더하면 1/C=(d₁/εr₁+d₂/εr₂)/(ε₀A)이다. C=8.854×10⁻¹²×{area:g}/(0.001/2+0.002/4) F로 계산하고 10¹²을 곱해 pF로 바꾼다. 층들은 면적을 나누는 병렬 배치가 아니다.', [area, 1, 2, 2, 4])
        ratio = 2+i
        put(0, 'coax-capacitance', i, '동축 원통',
            f'충분히 긴 공기 동축 원통의 외부 도체 안쪽 반지름/내부 도체 반지름 비가 {ratio}이다. 단위 길이당 정전용량은? ε₀=8.854×10⁻¹² F/m, π=3.141592653589793, ln은 자연로그이다.',
            2*math.pi*8.854e-12/math.log(ratio)*1e12, 'pF/m', f'가우스 법칙을 적용하고 전계를 반지름 방향으로 적분하면 C′=2πε₀/ln(b/a)이다. b/a={ratio}를 넣은 2π×8.854×10⁻¹²/ln({ratio}) F/m를 pF/m로 10¹²배 환산한다.', [ratio])
        put(0, 'wire-flux', i, '직선 전류 자계',
            f'진공 중 무한히 긴 직선 도체에 {n} A가 흐른다. 도체에서 0.05 m 떨어진 곳의 자속밀도는? μ₀=4π×10⁻⁷ H/m이다.',
            .2*n/.05, 'μT', f'B=μ₀I/(2πr)이다. μ₀를 넣으면 B=2×10⁻⁷×{n}/0.05 T이다. T에 10⁶을 곱하여 μT로 표시한다. 자계 H가 아닌 자속밀도 B를 계산한다.', [n, .05])
        current = 50+10*i
        put(0, 'parallel-wire-force', i, '전류 사이 힘',
            f'진공 중 평행한 긴 두 도체의 간격은 0.1 m이며 같은 방향 전류 {current} A와 20 A가 흐른다. 단위 길이당 인력의 크기는? μ₀=4π×10⁻⁷ H/m이다.',
            2e-7*current*20/.1*1000, 'mN/m', f'F/ℓ=μ₀I₁I₂/(2πd)=2×10⁻⁷×{current}×20/0.1 N/m이다. 1,000배하여 mN/m로 쓴다. 같은 방향 전류 사이에는 인력이 작용하며 부호가 아닌 크기를 묻는다.', [current, 20, .1])
        area = 4+i
        put(0, 'magnetic-reluctance', i, '자기 회로',
            f'균일 철심의 자로 길이는 0.5 m, 단면적은 {area} cm², 비투자율은 일정한 1,000이다. 누설·공극을 무시할 때 자기저항은? μ₀=4π×10⁻⁷ H/m, π=3.141592653589793이다.',
            .5/(4*math.pi*1e-7*1000*area*1e-4)/1000, 'kA/Wb', f'자기저항 ℜ=ℓ/(μ₀μrA)이다. A={area}×10⁻⁴ m²이므로 ℜ=0.5/(4π×10⁻⁷×1000×{area}×10⁻⁴) A/Wb이다. 1,000으로 나누어 kA/Wb로 환산한다. 철심 포화는 무시한 선형 조건이다.', [area, .5, 1000])
        turns = 20+10*i
        put(0, 'self-inductance', i, '쇄교자속',
            f'선형 자기회로의 자기저항이 100,000 A/Wb이고 권수는 {turns}회이다. 모든 자속이 전 권선과 쇄교한다고 할 때 자기 인덕턴스는?',
            turns**2/100000*1000, 'mH', f'Φ=NI/ℜ, 쇄교자속 λ=NΦ=N²I/ℜ이다. L=λ/I=N²/ℜ={turns}²/100000 H이다. 1,000을 곱해 mH로 바꾸며 누설 자속은 무시한다.', [turns, 100000])
        k = .2+.05*i
        put(0, 'mutual-inductance', i, '상호 유도',
            f'두 코일의 자기 인덕턴스가 100 mH와 25 mH, 결합계수 크기가 {k:g}이다. 상호 인덕턴스의 크기는?',
            k*math.sqrt(100*25), 'mH', f'상호 인덕턴스 크기는 M=k√(L₁L₂)이다. 두 인덕턴스 단위가 같으므로 M={k:g}×√(100×25) mH로 계산한다. 극성 부호가 아닌 크기를 묻고 k는 무차원이다.', [k, 100, 25])
        turns = 20+10*i
        put(0, 'faraday-average', i, '변압기 기전력',
            f'{turns}회 코일의 매회 쇄교자속이 0.05 s 동안 2 mWb에서 5 mWb로 단조 증가했다. 그 구간 평균 유도기전력의 크기는?',
            turns*.003/.05, 'V', f'평균 기전력 크기 |e평균|=N|ΔΦ|/Δt이다. ΔΦ=(5−2)×10⁻³ Wb이므로 {turns}×0.003/0.05 V이다. 렌츠 법칙의 부호는 방향을 나타내며 여기서는 크기만 계산한다.', [turns, 2, 5, .05])
        put(0, 'magnetic-energy', i, '자계 에너지',
            f'선형 인덕터의 인덕턴스는 100 mH이며 {n} A가 흐른다. 저장된 자계 에너지는?',
            .5*.1*n*n*1000, 'mJ', f'W=LI²/2이다. L=100×10⁻³ H=0.1 H와 I={n} A를 대입하면 W=0.1×{n}²/2 J이다. J에서 mJ로 1,000배 환산한다. 인덕턴스의 전류 의존성과 손실은 무시한다.', [100, n])
        er = 4+i
        put(0, 'wave-speed', i, '전자파',
            f'손실 없는 균질 유전체의 비유전율은 {er}, 비투자율은 1이다. 평면 전자파 속도는? 진공 광속은 300 Mm/s로 둔다.',
            300/math.sqrt(er), 'Mm/s', f'전파 속도 v=1/√(με)=c/√(μrεr)이다. c=300 Mm/s, μr=1, εr={er}를 넣어 300/√{er} Mm/s로 계산한다. Mm/s는 10⁶ m/s이며 손실·분산을 무시한 조건이다.', [300, er, 1])

        # Power systems: 16 new families, 160 questions.
        maximum = 30+5*i
        put(1, 'demand-factor', i, '수요율',
            f'설비용량 100 kW인 부하군의 최대수요전력이 {maximum} kW이다. 수요율은?',
            maximum, '%', f'수요율=최대수요전력/설비용량×100이다. {maximum}/100×100 %로 구한다. 서로 다른 부하군 최대수요의 동시성을 나타내는 부등률과 구별한다.', [maximum, 100])
        total = 100+10*i
        put(1, 'diversity-factor', i, '부등률',
            f'여러 부하군의 개별 최대수요전력 합계는 {total} kW이고 합성 최대수요전력은 80 kW이다. 부등률은?',
            total/80, '배', f'부등률=개별 최대수요 합/합성 최대수요이다. {total}/80을 계산한다. 개별 최대가 반드시 동시에 발생하지 않으므로 이 값은 1 이상이며 단위는 상쇄된다.', [total, 80])
        energy = 240+24*i
        put(1, 'load-factor', i, '부하율',
            f'하루 24시간 동안 사용 전력량은 {energy} kWh, 그날 최대수요전력은 40 kW였다. 일 부하율은?',
            energy/(24*40)*100, '%', f'평균전력은 E/t={energy}/24 kW이다. 부하율=평균전력/최대수요×100={energy}/(24×40)×100 %이다. 에너지와 전력의 단위를 혼동하지 않는다.', [energy, 24, 40])
        voltage = 10+2*i
        put(1, 'base-impedance', i, '단위법 기준량',
            f'3상 계통의 기준 선간전압은 {voltage} kV, 기준 3상 용량은 100 MVA이다. 상당 기준 임피던스는?',
            voltage**2/100, 'Ω', f'Zbase=V선간²/S3상이다. (kV)²/MVA는 Ω와 같으므로 {voltage}²/100 Ω로 계산한다. 선간전압과 3상 전체 용량의 조합에서 √3은 서로 상쇄된다.', [voltage, 100])
        new_s = 20+10*i
        put(1, 'pu-base-conversion', i, '기준 용량 환산',
            f'기준 100 MVA에서 리액턴스는 0.1 pu이다. 기준 전압을 바꾸지 않고 기준 용량만 {new_s} MVA로 바꾸면 새 리액턴스는?',
            .1*new_s/100, 'pu', f'같은 실제 임피던스에서 Zpu새=Zpu옛×(S새/S옛)×(V옛/V새)²이다. 전압 기준이 같으므로 0.1×{new_s}/100 pu이다. 용량 기준과 실제 임피던스 자체의 변화를 구별한다.', [.1, 100, new_s])
        capacity = 50+10*i
        put(1, 'three-phase-fault-current', i, '3상 단락 전류',
            f'선간전압 6.6 kV인 계통의 3상 단락 용량은 {capacity} MVA이다. 대칭 단락전류 실효값은? √3=1.732를 사용한다.',
            capacity/(1.732*6.6), 'kA', f'Ssc=√3VI이므로 I=Ssc/(√3V)이다. {capacity}/(1.732×6.6) kA로 계산한다. MVA/kV=kA이고 비대칭 직류분이나 첫 파고를 구하는 문제가 아니다.', [capacity, 6.6])
        z0 = 2+i
        put(1, 'single-ground-fault', i, '대칭좌표법 고장',
            f'고장 전 상전압 6,000 V이며 정상·역상·영상 임피던스가 각각 j2 Ω, j2 Ω, j{z0} Ω이다. 고장 임피던스 0인 1선 지락전류 크기는? 모든 전원은 정상분으로만 나타낸다.',
            3*6000/(4+z0)/1000, 'kA', f'1선 완전 지락에서 세 대칭분 회로가 직렬이므로 |If|=3|V상|/|Z₁+Z₂+Z₀|이다. 분모는 j(2+2+{z0})의 크기이고 3×6000/(4+{z0}) A를 1,000으로 나누어 kA로 환산한다.', [6000, 2, 2, z0])
        angle = 10+2*i
        rad = math.radians(angle)
        put(1, 'ferranti-no-load', i, '장거리 선로 무부하',
            f'손실 없는 선로의 무부하 수전단에서 Iᵣ=0이다. 송전단 전압은 100 kV이고 ABCD 상수 A=cos({angle}°)일 때 수전단 전압 크기는? 같은 전압 기준을 사용한다.',
            100/math.cos(rad), 'kV', f'송전단 전압 Vs=AVr+BIr이다. Ir=0이므로 Vr=Vs/A=100/cos({angle}°) kV이다. A가 1보다 작아 수전단 전압이 더 커지는 무부하 전압 상승이다.', [100, angle])
        put(1, 'power-angle', i, '전력각 특성',
            f'저항을 무시한 3상 송전선로의 양단 선간전압 크기는 모두 66 kV, 상당 리액턴스는 20 Ω, 송수전단 위상차는 {angle}°이다. 송전 유효전력은?',
            66**2/20*math.sin(rad), 'MW', f'손실 없는 상당 회로의 3상 전력은 P=(Vs선간Vr선간/X)sinδ이다. 66×66/20×sin({angle}°) MW로 구한다. kV²/Ω는 MW이며 발전기 내부 전압 대신 주어진 양단 전압을 사용한다.', [66, 66, 20, angle])
        inductance = 1+.1*i
        put(1, 'surge-impedance', i, '선로 특성 임피던스',
            f'손실 없는 선로의 단위 길이 인덕턴스는 {inductance:g} mH/km, 정전용량은 0.01 μF/km이다. 특성 임피던스 크기는?',
            math.sqrt(inductance*1e-3/(.01*1e-6)), 'Ω', f'손실 없는 선로에서 Zc=√(L′/C′)이다. L′={inductance:g}×10⁻³ H/km, C′=0.01×10⁻⁶ F/km를 대입한다. 길이 단위 km는 비에서 상쇄되며 결과는 Ω이다.', [inductance, .01])
        voltage = 33+5*i
        put(1, 'surge-loading', i, '자연 부하',
            f'손실 없는 3상 선로의 선간전압은 {voltage} kV, 특성 임피던스는 300 Ω이다. 자연 부하(SIL)는?',
            voltage**2/300, 'MW', f'자연 부하 Pn=V선간²/Zc이다. {voltage}²/300 MW로 계산한다. 상당 전압으로 계산하면 3배가 필요하지만 이미 선간전압을 사용하므로 다시 3을 곱하지 않는다.', [voltage, 300])
        length = 10+5*i
        put(1, 'surge-travel-time', i, '진행파 전달',
            f'서지가 선로를 200,000 km/s 속도로 진행한다. 길이 {length} km의 선로를 한 번 통과하는 시간은? 반사와 분산은 무시한다.',
            length/200000*1e6, 'μs', f't=ℓ/v={length}/200000 s이다. 1 s=10⁶ μs이므로 10⁶을 곱한다. 편도 도달 시간이며 왕복 반사 시간을 구하는 것이 아니므로 2를 곱하지 않는다.', [length, 200000])
        load = 400+50*i
        put(1, 'surge-reflection', i, '진행파 반사',
            f'특성 임피던스 300 Ω 선로가 저항 {load} Ω으로 종단된다. 입사 전압에 대한 반사 전압의 계수는?',
            (load-300)/(load+300), '배', f'전압 반사계수 Γ=(ZL−Zc)/(ZL+Zc)=({load}−300)/({load}+300)이다. 부하저항이 특성 임피던스보다 커서 양수이다. 전류 반사계수의 부호와 구별한다.', [load, 300])
        capacitance = .2+.1*i
        put(1, 'cable-charging', i, '충전 전류',
            f'평형 3상 케이블의 전체 길이에 대한 상당 대지 정전용량은 {capacitance:g} μF이다. 주파수 50 Hz, 선간전압 10 kV에서 상당 충전전류는? √3=1.732, π=3.141592653589793이다.',
            2*math.pi*50*capacitance*1e-6*10000/1.732, 'A', f'각 상의 충전전류 I=ωCV상이다. V상=10000/1.732 V, C={capacitance:g}×10⁻⁶ F를 사용하여 2π×50×{capacitance:g}×10⁻⁶×10000/1.732 A로 계산한다. C는 이미 전체 길이의 값이다.', [capacitance, 50, 10])
        put(1, 'hydro-output', i, '수력 발전',
            f'수차발전기 계통의 유량은 {n} m³/s, 유효 낙차는 20 m, 종합 효율은 0.8이다. 물 밀도 1,000 kg/m³, g=9.81 m/s²일 때 전기 출력은?',
            1000*9.81*n*20*.8/1000, 'kW', f'물의 위치에너지율에 효율을 곱해 P=ρgQHη이다. 1000×9.81×{n}×20×0.8 W를 1,000으로 나누어 kW로 환산한다. 유효 낙차이므로 수로 손실을 별도로 다시 빼지 않는다.', [n, 20, .8])
        output = 50+10*i
        put(1, 'thermal-plant-efficiency', i, '화력 발전 효율',
            f'발전소의 연료 소비는 10 kg/s이고 저위발열량은 20 MJ/kg이다. 전기 출력 {output} MW일 때 주어진 발열량 기준 효율은? 별도 보조 동력 차감은 없다.',
            output/(10*20)*100, '%', f'연료 열입력=질량유량×발열량=10×20 MJ/s=200 MW이다. 효율 η={output}/200×100 %로 계산한다. 발열량 기준을 고위발열량으로 바꾸지 않는다.', [output, 10, 20])

        # Electrical machines: 16 new families, 160 questions.
        turns = 100+20*i
        put(2, 'transformer-ratio', i, '이상 변압기',
            f'이상 변압기의 1차 권수는 1,000회, 2차 권수는 {turns}회이다. 1차 전압 200 V일 때 2차 전압은?',
            200*turns/1000, 'V', f'이상 변압기에서 V₂/V₁=N₂/N₁이다. V₂=200×{turns}/1000 V로 계산한다. 누설과 권선 전압강하를 무시한 조건이므로 부하 전압 변동을 추가하지 않는다.', [200, 1000, turns])
        loss = 10+5*i
        put(2, 'transformer-core-resistance', i, '무부하 시험',
            f'변압기 무부하 시험의 인가 전압은 100 V, 유효전력은 {loss} W이다. 무부하 동손은 무시한다. 이 측으로 환산한 병렬 철손저항 Rc는?',
            10000/loss, 'Ω', f'병렬 철손저항에서 P₀≈V₀²/Rc이다. 따라서 Rc=100²/{loss} Ω이다. 무부하 전류 전체가 저항 성분이라고 가정하는 것이 아니며 전력계의 유효전력 성분을 사용한다.', [100, loss])
        loss = 20+10*i
        put(2, 'transformer-series-resistance', i, '단락 시험',
            f'변압기 단락 시험에서 시험 전류는 10 A, 유효전력은 {loss} W였다. 철손을 무시할 때 시험 측 환산 직렬 등가저항은?',
            loss/100, 'Ω', f'시험 전력이 권선 동손이면 Psc=Isc²Req이다. Req={loss}/10² Ω로 구한다. 전압/전류 비로 구하는 임피던스 크기와 저항 성분은 다르다.', [10, loss])
        ratio = .2+.05*i
        put(2, 'transformer-load-copper', i, '부하율과 동손',
            f'정격 부하에서 변압기의 동손은 1,000 W이다. 전압과 권선저항이 일정하고 부하전류가 정격의 {ratio:g}배일 때 동손은?',
            1000*ratio**2, 'W', f'동손은 I²R에 비례하므로 Pcu=x²Pcu정격이다. x={ratio:g}를 넣어 {ratio:g}²×1000 W로 계산한다. 철손까지 같은 비율로 바꾸는 것은 아니다.', [1000, ratio])
        iron = 10+5*i
        put(2, 'transformer-max-efficiency', i, '최대 효율 조건',
            f'변압기의 일정 철손은 {iron} W, 정격 동손은 400 W이다. 역률이 일정할 때 효율이 최대가 되는 정격전류 대비 부하전류 비 x는?',
            math.sqrt(iron/400), 'pu', f'고정 철손과 가변 동손이 같을 때 최대 효율이다. x²×400={iron}이므로 x=√({iron}/400)이다. 양의 부하율을 택하며 이 관계는 전압·저항 및 역률이 일정한 모델에서 사용한다.', [iron, 400])
        speed = 600+100*i
        put(2, 'dc-generator-emf', i, '직류 발전기',
            f'직류 발전기의 극수 P=4, 전기자 총 도체수 Z=100, 병렬회로수 A=2, 매극 자속 Φ=0.02 Wb, 회전속도 {speed} rpm이다. 유도기전력은?',
            4*.02*100*speed/(60*2), 'V', f'직류기 유도기전력 E=PΦZn/(60A)이다. 4×0.02×100×{speed}/(60×2) V로 계산한다. n은 rpm이므로 초 단위 변환 계수 60이 분모에 들어간다.', [4, .02, 100, speed, 2])
        current = 10+2*i
        put(2, 'dc-motor-back-emf', i, '직류 전동기',
            f'직류 전동기 단자전압은 100 V, 전기자저항은 0.5 Ω, 전기자전류는 {current} A이다. 브러시 전압강하를 무시한 역기전력은?',
            100-.5*current, 'V', f'전동기 전기자 회로에서 V=E+IaRa이므로 E=V−IaRa=100−{current}×0.5 V이다. 발전기의 단자전압 식과 전류 방향을 혼동하지 않는다.', [100, .5, current])
        current = 2+i
        put(2, 'dc-electromagnetic-torque', i, '직류기 전자 토크',
            f'직류 전동기의 토크식은 T=kΦIa이며 이 운전점에서 kΦ=1.5 N·m/A이다. 전기자전류 {current} A일 때 전자 토크는? 기계 손실 토크는 별도이다.',
            1.5*current, 'N·m', f'주어진 kΦ는 기계 상수와 자속의 곱이다. T=(1.5 N·m/A)×{current} A로 대입하면 A가 상쇄되어 N·m가 된다. 이는 전자 토크이며 손실을 뺀 축 토크를 묻지 않는다.', [1.5, current])
        emf = 60+5*i
        put(2, 'dc-constant-flux-speed', i, '직류기 속도',
            f'자속이 일정한 직류 전동기가 역기전력 100 V에서 1,000 rpm으로 돈다. 자속은 그대로 두고 역기전력을 {emf} V로 바꾸면 속도는?',
            1000*emf/100, 'rpm', f'E=kΦn이므로 자속이 같으면 n₂/n₁=E₂/E₁이다. n₂=1000×{emf}/100 rpm이다. 단자전압의 비가 아니라 권선 강하를 제외한 역기전력의 비를 사용한다.', [1000, 100, emf])
        capacity = 10+5*i
        put(2, 'transformer-rated-line-current', i, '3상 변압기 정격',
            f'3상 변압기의 정격용량은 {capacity} kVA, 정격 선간전압은 400 V이다. 정격 선전류는? √3=1.732로 계산한다.',
            capacity*1000/(1.732*400), 'A', f'S=√3V선간I선이다. I={capacity}×1000/(1.732×400) A로 구한다. kVA를 VA로 바꾸고 정격 피상전력에는 역률을 곱하거나 나누지 않는다.', [capacity, 400])
        poles = 2*n
        put(2, 'synchronous-speed', i, '회전자계 속도',
            f'주파수 50 Hz, 극수 {poles}인 교류기의 동기속도는?',
            120*50/poles, 'rpm', f'극쌍 수는 P/2이고 1초 회전수는 f/(P/2)이다. rpm으로 환산하면 ns=120f/P=120×50/{poles} rpm이다. 이 값은 유도전동기의 실제 회전속도가 아닌 회전자계 속도이다.', [50, poles])
        slip = 1+i
        put(2, 'rotor-copper-loss', i, '유도기 전력 흐름',
            f'유도전동기의 공극전력은 20 kW, 슬립은 {slip}%이다. 회전자 동손은? 회전자 철손은 무시한다.',
            20*slip/100, 'kW', f'회전자 동손 Pcu₂=sPg이다. 슬립을 {slip}/100으로 바꾸어 20×{slip}/100 kW를 계산한다. 고정자 손실은 이미 공극전력 이전에서 제외된 것으로 본다.', [20, slip])
        put(2, 'induction-developed-power', i, '유도기 기계적 변환',
            f'유도전동기의 공극전력은 30 kW, 슬립은 {slip}%이다. 회전자 철손을 무시할 때 발생 기계출력은? 마찰·풍손을 뺀 축 출력이 아니다.',
            30*(1-slip/100), 'kW', f'공극전력에서 회전자 동손 sPg를 빼면 Pm=(1−s)Pg이다. (1−{slip}/100)×30 kW로 구한다. 발생 기계출력에서 기계 손실을 더 빼야 축 출력이 되지만 여기서는 빼지 않는다.', [30, slip])
        resistance = .1+.1*i
        put(2, 'induction-max-torque-slip', i, '유도기 최대 토크',
            f'고정자 임피던스를 무시한 유도전동기 모델에서 회전자 정지 저항은 {resistance:g} Ω, 정지 리액턴스는 2 Ω이다. 최대 토크가 발생하는 슬립 크기는?',
            resistance/2, 'pu', f'주어진 근사 모델에서 토크는 sR₂/(R₂²+(sX₂)²)에 비례한다. 최대 조건은 sX₂=R₂이므로 sm={resistance:g}/2이다. 결과는 pu 슬립이고 백분율이 아니다.', [resistance, 2])
        alpha = 10+10*i
        put(2, 'pitch-factor', i, '단절권',
            f'기본파에 대해 코일이 전절권보다 전기각 {alpha}°만큼 짧게 감겨 있다. 단절권 계수의 크기는?',
            math.cos(math.radians(alpha/2)), '배', f'두 코일변 기전력의 벡터합으로 kp=cos(α/2)이다. 단절각 α={alpha}°이므로 cos({alpha}/2°)를 계산한다. 코일 피치각 자체가 아닌 전절권에서 부족한 각을 사용한다.', [alpha])
        beta = 10+2*i
        put(2, 'distribution-factor', i, '분포권',
            f'한 권선군에 같은 크기의 슬롯 기전력 3개가 있고 인접 기전력의 전기각 차가 β={beta}°이다. 기본파 분포권 계수는?',
            math.sin(math.radians(3*beta/2))/(3*math.sin(math.radians(beta/2))), '배', f'같은 크기 슬롯 기전력 세 개의 벡터합으로 kd=sin(qβ/2)/(qsin(β/2))이다. q=3, β={beta}°를 넣는다. 모든 각은 전기각이며 코일 단절에 따른 kp와는 별개이다.', [3, beta])

        # Circuits and control: 16 new families, 160 questions.
        resistance = 6+3*i
        put(3, 'delta-star', i, '저항망 변환',
            f'각 변이 {resistance} Ω인 평형 Δ 저항망을 등가 Y 저항망으로 바꾼다. Y의 한 팔 저항은?',
            resistance/3, 'Ω', f'Δ-Y 변환에서 한 팔은 인접 두 Δ 저항의 곱을 세 Δ 저항의 합으로 나눈 값이다. {resistance}²/(3×{resistance})={resistance}/3 Ω이다. 평형인 경우에만 간단히 3으로 나눌 수 있다.', [resistance])
        voltage = 10+i
        put(3, 'nodal-voltage', i, '절점 해석',
            f'접지 기준 +{voltage} V인 이상 전압원 단자와 절점 사이에 2 Ω, 그 절점과 접지 사이에 3 Ω이 있다. 다른 가지가 없을 때 절점 전압은?',
            voltage*3/5, 'V', f'절점 KCL은 (v−{voltage})/2+v/3=0이다. 양변에 6을 곱해 5v=3×{voltage}, 따라서 v=3×{voltage}/5 V이다. 부하가 추가되지 않은 두 저항 연결이다.', [voltage, 2, 3])
        voltage = 10+2*i
        put(3, 'maximum-power-transfer', i, '최대 전력 전달',
            f'직류 테브난 등가전압은 {voltage} V, 내부저항은 5 Ω이다. 양의 가변 부하저항에 전달 가능한 최대 전력은?',
            voltage**2/(4*5), 'W', f'부하전력 P=Vth²RL/(Rth+RL)²는 RL=Rth에서 최대이다. Pmax={voltage}²/(4×5) W이다. 부하전압은 이때 개방전압의 절반이며 전원 전체 소비전력과 구별한다.', [voltage, 5])
        voltage = 100+10*i
        put(3, 'single-phase-real-power', i, '정현파 유효전력',
            f'정현파 단상 부하의 전압 실효값은 {voltage} V, 전류 실효값은 2 A, 역률은 0.8이다. 유효전력은?',
            voltage*2*.8, 'W', f'정현파 단상 유효전력은 P=VIcosφ이다. {voltage}×2×0.8 W로 구한다. 전압과 전류가 이미 실효값이므로 √2로 다시 나누지 않으며 단상이라 √3도 쓰지 않는다.', [voltage, 2, .8])
        resistance = 10+i
        put(3, 'admittance-conductance', i, '복소 어드미턴스',
            f'부하 임피던스가 {resistance}+j20 Ω이다. 어드미턴스의 실수 성분 컨덕턴스 G는?',
            resistance/(resistance**2+400)*1000, 'mS', f'Y=1/(R+jX)=(R−jX)/(R²+X²)이다. G={resistance}/({resistance}²+20²) S이며 1,000을 곱해 mS로 쓴다. 임피던스 실수부의 역수 1/R과는 다르다.', [resistance, 20])
        inductance = 10+10*i
        put(3, 'series-quality-factor', i, '공진 품질계수',
            f'직렬 RLC의 공진 각주파수는 1,000 rad/s, 인덕턴스는 {inductance} mH, 저항은 2 Ω이다. 직렬 공진 품질계수 Q는?',
            1000*inductance*.001/2, '배', f'직렬 공진에서 Q=ω₀L/R이다. L={inductance}×10⁻³ H를 대입해 1000×{inductance}×10⁻³/2로 계산한다. 주어진 값이 각주파수이므로 2π를 다시 곱하지 않는다.', [1000, inductance, 2])
        voltage = 2+i
        put(3, 'inductor-initial-slope', i, 'RL 과도현상',
            f'초기 전류 0인 직렬 RL 회로에 t=0에서 {voltage} V 직류를 인가했다. L=0.5 H일 때 t=0⁺의 전류 변화율은? 저항은 유한한 양수이다.',
            voltage/.5, 'A/s', f'회로식 V=Ri+Ldi/dt에서 0⁺의 인덕터 전류는 0이다. 따라서 Ri=0이고 di/dt=V/L={voltage}/0.5 A/s이다. 전류 자체가 순간적으로 뛰는 것이 아니다.', [voltage, .5])
        ia = 10+i
        put(3, 'zero-sequence-current', i, '대칭분',
            f'동일 주파수의 상전류 페이저가 Ia={ia}+j0 A, Ib=−2+j0 A, Ic=1+j0 A이다. 영상전류 페이저 I₀의 실수부는?',
            (ia-2+1)/3, 'A', f'영상분은 I₀=(Ia+Ib+Ic)/3이다. 모두 실수축의 주어진 페이저이므로 ({ia}−2+1)/3 A이다. 중성선 전류의 기준 방향에 따른 3I₀와 구별한다.', [ia, -2, 1])
        wn = 2+i
        put(3, 'second-order-settling', i, '2차계 응답',
            f'표준 2차계의 감쇠비는 0.5, 고유각주파수는 {wn} rad/s이다. 2% 정착시간 근사식 ts≈4/(ζωn)을 적용한 시간은?',
            4/(.5*wn), 's', f'문제에서 지정한 2% 근사식을 사용한다. ζ=0.5와 ωn={wn} rad/s를 넣어 ts≈4/(0.5×{wn}) s이다. 정확한 최초 정착시각이나 다른 허용대역의 정착시간을 구하는 문제가 아니다.', [.5, wn])
        zeta = .1+.05*i
        put(3, 'second-order-overshoot', i, '2차계 오버슈트',
            f'영점 없는 표준 2차 단위이득계의 감쇠비는 {zeta:g}이다. 단위 계단응답의 최대 오버슈트율은? 0<ζ<1이고 Mp=exp(−πζ/√(1−ζ²))×100을 사용한다. π=3.141592653589793이다.',
            math.exp(-math.pi*zeta/math.sqrt(1-zeta*zeta))*100, '%', f'감쇠 진동계의 첫 최대값과 최종값 차이를 최종값으로 나눈 비율이다. ζ={zeta:g}를 식에 넣어 exp(−π×{zeta:g}/√(1−{zeta:g}²))×100 %로 구한다. 출력의 최대값 전체가 아닌 초과 비율이다.', [zeta])
        a = 3+i
        put(3, 'routh-cubic-boundary', i, '라우스 안정 판별',
            f'특성다항식 s³+2s²+{a}s+b에서 b>0이다. 점근 안정인 범위를 0<b<B로 표시할 때 경계값 B는?',
            2*a, '단위', f'라우스 첫 열은 1, 2, (2×{a}−b)/2, b이다. 모두 양수이려면 b>0 및 b<2×{a}여야 한다. 따라서 B=2×{a}이다. 경계 b=B 자체는 점근 안정 범위에 포함하지 않는다.', [2, a])
        gain = 1+i
        put(3, 'ramp-steady-error', i, '정상상태 편차',
            f'단위 음의 피드백에서 개루프 G(s)={gain}/[s(s+1)]이다. 단위 램프 r(t)=t에 대한 정상상태 오차는? 폐루프는 안정하다.',
            1/gain, '단위', f'속도 오차상수 Kv=lim(s→0)sG(s)={gain}이다. 안정한 1형 계에서 단위 램프 정상 오차 ess=1/Kv=1/{gain}이다. 계단 입력의 오차와 구별하며 램프 기울기는 1이다.', [gain])
        gain = 2+i
        put(3, 'gain-decibels', i, '보드 선도',
            f'어느 주파수에서 전달함수 크기가 {gain}이다. 진폭 이득을 dB로 나타내면? 진폭비에는 20log₁₀을 사용한다.',
            20*math.log10(gain), 'dB', f'진폭비의 dB값은 20log₁₀|G|이다. |G|={gain}이므로 20log₁₀({gain}) dB이다. 전력비에 사용하는 10log₁₀과 혼동하지 않는다.', [gain])
        alpha = .1+.05*i
        put(3, 'lead-maximum-phase', i, '위상 진상 보상',
            f'진상 보상기 Gc(s)=(1+Ts)/(1+αTs)에서 T>0, α={alpha:g}이다. 최대 위상 진상각은? sinφmax=(1−α)/(1+α)이고 결과는 도 단위이다.',
            math.degrees(math.asin((1-alpha)/(1+alpha))), '°', f'0<α<1이므로 진상 보상이다. φmax=arcsin((1−{alpha:g})/(1+{alpha:g}))의 주값을 구한 후 180/π를 곱해 도로 환산한다. 보상기의 극·영점 위치가 아닌 최대 위상각을 계산한다.', [alpha])
        real = .1+.05*i
        put(3, 'discrete-pole-radius', i, '이산시간 극점',
            f'이산시간 시스템 극점 z={real:g}+j0.2의 크기 |z|는? 점근 안정 판정에는 단위원 내부 조건을 적용한다.',
            math.hypot(real, .2), '배', f'복소수 크기 |z|=√(Re(z)²+Im(z)²)=√({real:g}²+0.2²)이다. 실수부만으로 판정하지 않는다. 계산한 반지름은 1보다 작지만 이 문항은 주어진 한 극점의 크기를 묻는다.', [real, .2])
        put(3, 'laplace-initial-value', i, '초기값 정리',
            f'어떤 유한 초기값 신호의 라플라스 변환이 Y(s)=({n}s+3)/[s(s+2)]이다. 충격 성분은 없을 때 y(0⁺)는?',
            n, '단위', f'초기값 정리 y(0⁺)=lim(s→∞)sY(s)를 사용한다. lim(s→∞)({n}s+3)/(s+2)={n}이다. 최종값 정리의 s→0 극한과 다르며 Y(s)는 주어진 조건에서 초기 충격 성분을 갖지 않는다.', [n, 3, 2])

        # Installation engineering calculations; no claimed KEC thresholds.
        current = 1000+100*i
        put(4, 'conductor-adiabatic-area', i, '도체 단락 열 검토',
            f'가정한 단열 모델 A=I√t/k를 사용한다. 고장전류는 {current} A, 차단시간은 0.25 s, 문제에서 주어진 재료계수 k는 100 A·√s/mm²이다. 요구 단면적은? 표준 규격 선정이나 법정 기준을 묻지 않는다.',
            current*math.sqrt(.25)/100, 'mm²', f'단열 모델 I²t=k²A²를 A에 대해 풀면 A=I√t/k이다. {current}×√0.25/100 mm²로 구한다. k는 이 문제에서 지정한 가정값이며 특정 KEC 적용계수라고 인용하지 않는다.', [current, .25, 100])
        put(4, 'earth-potential-rise', i, '접지 전위 상승',
            f'대지로 흐르는 고장전류가 {n} A이고 단순 저항 모델의 접지저항은 10 Ω이다. 원격 대지에 대한 접지극 전위 상승은? 허용 접촉전압 판정은 하지 않는다.',
            n*10, 'V', f'단순 저항 모델에서 전위 상승 Ue=IeRe이다. {n}×10 V로 계산한다. 이것이 곧 인체 접촉전압이나 안전 허용값이라는 뜻은 아니며 전위 분포·본딩·접촉 조건은 별도이다.', [n, 10])
        returning = 1-.01*n
        put(4, 'residual-current', i, '잔류전류 검출',
            f'단상 회로에서 나가는 전류 실효값은 1 A, 되돌아오는 전류는 {returning:g} A이다. 두 전류의 위상은 같으며 방향만 반대이다. 감시 도체 전류합의 잔류 크기는?',
            (1-returning)*1000, 'mA', f'지정된 같은 위상 조건에서는 잔류전류 크기가 |I가는−I오는|이다. |1−{returning:g}| A에 1,000을 곱해 mA로 환산한다. 특정 보호장치의 법정 동작 감도나 모든 감전 보호를 판정하지 않는다.', [1, returning])
        put(4, 'insulation-test-resistance', i, '절연 시험 원리',
            f'500 V 직류 절연 시험에서 정상 누설전류가 {n} μA이다. 충전 과도전류와 계기 오차를 무시할 때 절연저항은? 합격 기준은 별도이다.',
            500/n, 'MΩ', f'옴의 법칙 R=V/I를 쓴다. 500/({n}×10⁻⁶) Ω를 10⁶으로 나누면 500/{n} MΩ이다. 측정값 계산이며 법정 최소 절연저항이나 시험 전압 선정의 적합성을 확인한 것이 아니다.', [500, n])
        temp = 30+10*i
        put(4, 'conductor-temperature-resistance', i, '도체 온도 영향',
            f'도체의 20°C 저항은 2 Ω, 20°C 기준 선형 온도계수는 0.004/°C이다. {temp}°C에서 저항은? 주어진 선형 근사를 적용한다.',
            2*(1+.004*(temp-20)), 'Ω', f'Rθ=R20[1+α20(θ−20)]이다. 2×[1+0.004×({temp}−20)] Ω로 구한다. 온도차는 °C 차와 K 차가 같고 이 근사는 문제에서 지정한 범위의 모델이다.', [2, .004, temp])
        base = 100+10*i
        put(4, 'cable-correction-factors', i, '허용전류 보정 계산',
            f'설계 계산에서 기본 허용전류를 {base} A, 온도 보정계수를 0.8, 집합 보정계수를 0.7로 가정한다. 두 계수를 곱한 보정 허용전류는? 계수는 문제 가정이며 공식 표 인용이 아니다.',
            base*.8*.7, 'A', f'주어진 곱셈 보정 모델 Iz=I기본×Ct×Cg에 대입한다. {base}×0.8×0.7 A이다. 실제 설계에서는 전선 종류·포설·온도에 맞는 공식 표의 계수와 다른 보호 조건을 따로 확인해야 한다.', [base, .8, .7])
        energy = 100*n
        put(4, 'ups-battery-capacity', i, '예비 전원 용량',
            f'UPS 부하에 {energy} Wh를 공급해야 한다. 배터리 전압 48 V, 변환 효율 0.9, 사용 가능한 방전 비율 0.8을 일정하게 가정할 때 필요한 공칭 용량은? 열화·방전율 영향은 무시한다.',
            energy/(48*.9*.8), 'Ah', f'공급 에너지 E=V×C(Ah)×η×사용비율이다. C={energy}/(48×0.9×0.8) Ah로 구한다. 모든 조건은 문제에서 준 설계 가정이며 실제 배터리 선정에는 온도·열화·방전 특성도 고려한다.', [energy, 48, .9, .8])
        area = 12+6*i
        put(4, 'lumen-method-count', i, '조명 계산',
            f'평균 조도 200 lx를 목표로 면적 {area} m²에 등기구를 설치한다. 등기구당 광속은 3,000 lm, 이용률은 0.6, 유지율은 0.8이다. 광속법 N=EA/(FUM)에서 최소 정수 등기구 수는? 법정 조도 기준이 아닌 주어진 목표값이다.',
            math.ceil(200*area/(3000*.6*.8)), '개', f'계산상 수량 N계산=200×{area}/(3000×0.6×0.8)이다. 요구 조도를 넘도록 정수로 올림한다. 소수 자리를 반올림하여 수량을 줄이지 않는다. 실제 배치·눈부심·균제도 검토는 별도이다.', [200, area, 3000, .6, .8])
        power = 2+i
        put(4, 'motor-supply-current', i, '전동기 부하전류',
            f'3상 전동기의 축 출력은 {power} kW, 선간전압 400 V, 효율 0.9, 역률 0.8이다. 정격 운전 시 선전류는? √3=1.732로 계산하며 보호장치 정격 선정은 별도이다.',
            power*1000/(1.732*400*.9*.8), 'A', f'전기 입력 P입력=P축/η=√3VIcosφ이다. I={power}×1000/(1.732×400×0.9×0.8) A로 계산한다. 축 출력이므로 효율로 나누며 이 전류만으로 차단기 규격을 확정하지 않는다.', [power, 400, .9, .8])
        put(4, 'flat-energy-charge', i, '사용 전력량',
            f'소비전력이 일정한 {n} kW 부하를 2시간 사용했다. 전력량 요금만 100 원/kWh의 단일 단가로 가정할 때 금액은? 기본요금·세금·실제 요금제는 적용하지 않는다.',
            n*2*100, '원', f'전력량 E=Pt={n}×2 kWh이다. 여기에 문제의 가상 단가 100 원/kWh를 곱하면 {n}×2×100 원이다. 실제 전기요금이나 계약종별 규정을 인용한 문제가 아니다.', [n, 2, 100])
        modules = 2+i
        put(4, 'pv-cold-open-circuit', i, '태양광 전압 검토',
            f'기준 25°C에서 모듈 개방전압은 40 V, 선형 전압 온도계수는 −0.003/°C이다. 셀 온도 −10°C에서 모듈 {modules}개를 직렬 연결했을 때 개방전압은? 모듈은 동일하며 주어진 선형 모델을 적용한다.',
            modules*40*(1+(-.003)*(-10-25)), 'V', f'온도차 ΔT=−10−25=−35°C이다. 직렬 총전압 V=N×40×[1+(−0.003)×(−35)]={modules}×40×1.105 V이다. 음의 온도계수 때문에 저온에서 전압이 증가한다. 기기 최대허용전압 판정은 별도이다.', [modules, 40, -.003, -10, 25])
        count = 2+i
        put(4, 'parallel-insulation', i, '분기 절연 등가',
            f'각 절연저항이 100 MΩ인 동일 분기 {count}개가 측정 단자와 대지 사이에 병렬로 연결된다. 다른 누설 경로가 없을 때 등가 절연저항은?',
            100/count, 'MΩ', f'병렬 절연 경로의 컨덕턴스는 더해진다. 1/Req={count}/100 (MΩ)⁻¹이므로 Req=100/{count} MΩ이다. 분기 수만큼 저항을 더하는 직렬 계산과 다르다. 합격 기준을 묻지 않는다.', [100, count])
        current = 2+i
        put(4, 'dc-drop-design-length', i, '직류 배선 설계',
            f'24 V 직류 2선식 배선에서 설계 목표 전압강하를 2%로 정한다. 도체 단면적 4 mm², 저항률 0.0175 Ω·mm²/m, 전류 {current} A일 때 편도 최대 길이는? 접속 저항·온도 변화는 무시하고 2%는 법정값이 아닌 설계 가정이다.',
            (.02*24)*4/(2*.0175*current), 'm', f'왕복 도체 저항은 2ρℓ/A이고 ΔV=2ρℓI/A이다. 목표 ΔV=24×0.02=0.48 V이므로 ℓ=0.48×4/(2×0.0175×{current}) m이다. 편도 길이를 묻기 때문에 왕복 계수 2를 유지한다.', [24, 2, 4, .0175, current])
        heat = 10*n
        put(4, 'enclosure-thermal-rise', i, '외함 발열 모델',
            f'외함 내부 손실이 {heat} W이고 정상상태 방열 컨덕턴스를 5 W/K로 가정한다. 주변 대비 평균 온도 상승은? 일사·열용량·국부 온도차는 무시한다.',
            heat/5, 'K', f'주어진 정상상태 열 모델 P=GthΔT에서 ΔT=P/Gth={heat}/5 K이다. 열저항 K/W가 아니라 열 컨덕턴스 W/K를 주었으므로 나눈다. 부품의 법정 허용온도나 실제 국부 최고온도 판정은 별도이다.', [heat, 5])
        first = 25+5*i
        put(4, 'independent-earth-parallel', i, '접지극 병렬 모델',
            f'두 접지극의 저항이 {first} Ω과 100 Ω이다. 상호간섭이 없고 연결 도체 저항이 0인 이상 병렬 모델에서 합성저항은?',
            first*100/(first+100), 'Ω', f'독립 병렬 모델의 합성저항은 Req=R₁R₂/(R₁+R₂)={first}×100/({first}+100) Ω이다. 실제 가까운 접지극은 상호간섭으로 이 단순식과 다를 수 있다. 허용 접지저항 판정은 하지 않는다.', [first, 100])
        voltage = 100+10*i
        put(4, 'capacitor-discharge-time', i, '잔류 전압 방전',
            f'100 μF 콘덴서가 {voltage} V로 충전된 뒤 100 kΩ 저항으로만 방전된다. 전압이 주어진 관리 목표 10 V가 되기까지 시간은? 10 V를 법정 안전 한계로 해석하지 않는다. ln은 자연로그이다.',
            100000*100e-6*math.log(voltage/10), 's', f'v(t)=V₀exp(−t/RC)를 t에 대해 풀면 t=RC ln(V₀/V목표)이다. R=100×10³ Ω, C=100×10⁻⁶ F여서 RC=10 s이고 t=10ln({voltage}/10) s이다. 실제 작업의 무전압 확인을 대신하지 않는다.', [100, 100, voltage, 10])
