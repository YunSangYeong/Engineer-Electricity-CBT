"""Audit registered counts, exact duplicates, deterministic output and family inventory."""
import hashlib
import json
import subprocess
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = ['src/data/questions-main.json', 'public/templates/questions.json', 'public/templates/questions.csv']
def hashes():
    return {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in paths}
before = hashes()
subprocess.run(['python3', str(ROOT/'scripts/generate_bank.py')], cwd=ROOT, check=True)
assert hashes() == before, 'Authoring outputs are stale or generation is nondeterministic'
bank = json.loads((ROOT/paths[0]).read_text())
assert len(bank) == 1000
ids, fingerprints = set(), set()
for q in bank:
    assert q['id'] not in ids, q['id']
    ids.add(q['id'])
    text = '|'.join([q['question'], *sorted(q['choices'])])
    fingerprint = ''.join(unicodedata.normalize('NFKC', text).split()).lower()
    assert fingerprint not in fingerprints, q['id']
    fingerprints.add(fingerprint)
    assert q['type'] == 'original' and q['year'] is None and q['session'] is None
    assert q['verificationStatus'] == 'reviewed'
counts = Counter(q['subject'] for q in bank)
assert len(counts) == 5 and set(counts.values()) == {200}
families = {}
for q in bank:
    if q.get('family'):
        families.setdefault(q['family'], []).append(q)
assert len(families) == 96 and all(len(group) == 10 for group in families.values())
audit = {
    'scope': 'AI internal template/text review and separate automated numeric checks; not official or external expert verification',
    'reviewDate': '2026-10-21', 'target': 1000, 'registered': len(bank),
    'reviewedInternal': len(bank), 'pending': 0, 'shortfall': 0,
    'duplicateIds': 0, 'duplicateNormalizedQuestionsAndChoices': 0,
    'typeCounts': dict(past=0, reconstructed=0, original=len(bank)),
    'subjectCounts': dict(counts), 'calculationCount': 960, 'numericFamilyCount': len(families),
    'conditionsPerFamily': 10, 'additionalNumericVariants': 864, 'conceptualCount': 40,
    'baselineCommit': '1eade5a03b8f1d0186d4df4dd98364ca9ec64323',
    'retainedBaselineCount': 200, 'newCount': 800,
    'baselinePreservationCheck': 'tests/bank.test.ts using tests/fixtures/baseline-200.json',
    'externalExpertReviewed': 0, 'officialSyllabusCompared': False,
    'deterministicRegeneration': True, 'sha256': before,
    'numericVerification': 'npm test; tests/bank.test.ts and tests/expanded-equations.ts',
}
(ROOT/'docs/bank-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n')
lines = ['# 계산 유형 내부 검토 목록', '',
         '96개 계산 템플릿 × 10조건 = 960문항. 아래는 각 템플릿의 첫 조건과 풀이이며, 숫자 조건 전체는 기본 JSON에 있다.',
         'AI 내부 조건·단위·문장 검토와 별도 TypeScript 재계산 범위다. 외부 문헌 대조·전문가 검수를 뜻하지 않는다.', '',
         '## 800문항 보완 시 검토 사항', '',
         '- 기존 16유형의 조건 수를 늘리지 않고 새 템플릿 80개를 추가했다. 유형은 작성 템플릿 단위이며 서로 관련된 개념이 있다.',
         '- 선간/상 전압, 실효값/파고, 극수/극쌍, 주파수/각주파수, 공극/발생/축 출력, 슬립 pu/%를 구별했다.',
         '- 분포권은 임의 슬롯각을 표준 3상 슬롯 설계로 가장하지 않도록 같은 크기 기전력 3개의 벡터합 조건으로 작성했다.',
         '- 대칭분 문제는 순간값과 페이저를 섞지 않도록 동일 주파수의 주어진 페이저 조건으로 작성했다.',
         '- 정착시간은 명시한 근사식, 조명 수량은 올림, 나머지 수치는 지정한 소수 둘째 자리 반올림이다.',
         '- 접지·전선·조명·UPS·태양광 계산의 설계 목표와 재료계수는 가정값이며 법정값이라고 표시하지 않았다.', '',
         '## 템플릿별 조건·단위·풀이', '']
for family, group in sorted(families.items()):
    q = group[0]
    lines.extend([f"### {family} — {q['subject']} / {q['topic']}", '',
                  f"- 조건 수: {len(group)}; 결과 단위: {q['calculation']['unit']}",
                  f"- 첫 문항: {q['question']}", f"- 풀이: {q['explanation']}", ''])
(ROOT/'docs/family-review.md').write_text('\n'.join(lines).rstrip()+'\n')
print('Audited: 1,000; per subject: 200; exact duplicate IDs/bodies: 0; shortfall: 0')
