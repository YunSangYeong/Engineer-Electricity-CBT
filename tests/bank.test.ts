import { createHash } from 'node:crypto';
import baseline from './fixtures/baseline-200.json';
import { expandedEvaluators } from './expanded-equations';
import { describe, expect, it } from 'vitest';
import { BASE_BANK as bank, SUBJECTS, fingerprint, validateQuestion } from '../src/model';
// Different implementation/language from authoring: equations are independently rearranged.
const evaluators: Record<string, (v: number[]) => number> = {
  ...expandedEvaluators,
  'parallel-capacitance': ([a, d]) => 8854 * a / d,
  'line-field': ([n, r]) => n / (2 * Math.PI * 0.008854 * r),
  'toroid-field': ([n, i, r]) => (n / (2 * Math.PI * r)) * i,
  'motional-emf': ([b, l, v]) => v * l * b,
  'line-loss': ([i, r]) => (i * r) * i * 0.003,
  'voltage-drop': ([i, r, x, c, s]) => (r*c*i + x*s*i) * 1.732,
  'short-circuit-capacity': ([s,z]) => s * (1/z),
  'power-factor-correction': ([p,t1,t2]) => p*t1-p*t2,
  'shaft-torque': ([p,n]) => p / (n / 9550),
  'rotor-frequency': ([f,s]) => f / 100 * s,
  'synchronous-emf': ([f,n,phi,k]) => (n*phi)*(f*4.44*k),
  'transformer-efficiency': ([p,iron,copper]) => 100 / (1+(iron+copper)/p),
  'series-impedance': ([r,x]) => Math.sqrt(r*r+x*x),
  'resonance': ([l,c]) => Math.sqrt(1/(l*c*1e-9))/(2*Math.PI),
  'feedback-gain': ([k]) => 1-1/(1+k),
  'first-order-response': ([a,tau,t]) => a - a/Math.exp(t/tau),
};
describe('전기기사 자체 문제은행 검수', () => {
  it('실제 1000개: 과목별 200개, 기출/복원 0, 중복과 허위 연도 없음', () => {
    expect(bank).toHaveLength(1000);
    expect(new Set(bank.map(q=>q.id)).size).toBe(1000);
    expect(new Set(bank.map(fingerprint)).size).toBe(1000);
    SUBJECTS.forEach(subject=>expect(bank.filter(q=>q.subject===subject)).toHaveLength(200));
    bank.forEach(q=>{
      expect(()=>validateQuestion(q)).not.toThrow();
      expect(q.type).toBe('original');
      expect(q.year).toBeNull(); expect(q.session).toBeNull();
      expect(q.verificationStatus).toBe('reviewed');
      expect(q.reviewNote).toContain('내부');
      expect(q.explanation.length).toBeGreaterThan(40);
    });
  });
  it('96개 계산 유형 × 10조건 = 960문항, 개념 40문항. 의미상 변형은 family로 공개', () => {
    const numerical=bank.filter(q=>q.calculation);
    expect(numerical).toHaveLength(960);
    const families=new Set(numerical.map(q=>q.family)); expect(families.size).toBe(96);
    families.forEach(f=>{
      const group=numerical.filter(q=>q.family===f); expect(group).toHaveLength(10);
      expect(new Set(group.map(q=>JSON.stringify(q.calculation?.values))).size).toBe(10);
    });
  });
  it('기존 200개 문항의 모든 필드와 ID를 그대로 보존한다',()=>{
    const ids=new Set(baseline.ids);
    const retained=bank.filter(q=>ids.has(q.id));
    expect(retained).toHaveLength(200);
    expect(createHash('sha256').update(JSON.stringify(retained)).digest('hex')).toBe(baseline.sha256);
  });
  it('정확한 반올림 경계 0.875는 0.88로 수록한다', () => {
    expect(bank.find(q=>q.id==='EE-feedback-gain-07')!.calculation!.result).toBe(0.88);
  });
  for(const q of bank.filter(q=>q.calculation)) it(`독립 재계산·보기 동치·단위 ${q.id}`,()=>{
    const c=q.calculation!;
    expect(evaluators[c.kind]).toBeDefined();
    const exact=evaluators[c.kind](c.values);
    const rounded=Math.round((exact+Number.EPSILON)*100)/100;
    expect(c.result).toBeCloseTo(rounded,8);
    const answer=q.choices[q.answer-1];
    expect(answer).toBe(`${c.result} ${c.unit}`);
    expect(q.choices.filter(choice=>{
      const number=Number(choice.slice(0,choice.lastIndexOf(' ')));
      expect(choice.endsWith(' '+c.unit)).toBe(true);
      return Math.abs(number-rounded)<1e-9;
    })).toHaveLength(1);
    expect(Math.abs(exact-c.result)).toBeLessThanOrEqual(0.005000001);
  });
});
