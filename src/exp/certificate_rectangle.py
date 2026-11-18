"""Exact rational verification of the eight-atom, four-corner k=2 certificate.

No random seeds, solver, or floating-point arithmetic are used in this check.
"""
from fractions import Fraction as F
import json
from pathlib import Path

# At each A, B, C, D, record which of the three replica domains is omitted.
pattern_mass = {
    (2, 1, 1, 1): F(1, 22),
    (2, 1, 2, 1): F(9, 44),
    (2, 1, 2, 2): F(5, 132),
    (2, 3, 2, 3): F(7, 33),
    (3, 1, 1, 1): F(1, 22),
    (3, 3, 1, 1): F(9, 44),
    (3, 3, 1, 3): F(5, 132),
    (3, 3, 2, 2): F(7, 33),
}
w = ((F(1), F(1, 2), F(1, 2)),
     (F(1), F(3, 2), F(1, 2)),
     (F(1), F(1, 2), F(3, 2)),
     (F(1), F(3, 2), F(3, 2)))
edges = ((0, 1, 2), (0, 2, 3), (1, 3, 3), (2, 3, 2))  # one-indexed raised node
assert sum(pattern_mass.values()) == 1
p_excl = [[sum(m for pat, m in pattern_mass.items() if pat[s] == i)
           for i in (1, 2, 3)] for s in range(4)]
for a, weights in enumerate(w):
    total = sum(weights)
    assert p_excl[a] == [1 - 2 * wi / total for wi in weights]
records = []
for old, new, j in edges:
    actual = sum(m for pat, m in pattern_mass.items() if pat[old] != pat[new])
    opt = 2 * w[new][j-1] / sum(w[new]) - 2 * w[old][j-1] / sum(w[old])
    assert opt > 0 and actual / opt == F(12, 11)
    records.append(dict(edge=f'{"ABCD"[old]}->{"ABCD"[new]}', moved=str(actual),
                        opt=str(opt), ratio=str(actual / opt)))
result = dict(certificate='exact rational', sum_prob='1',
              fair_excluded_marginals=[[str(x) for x in p] for p in p_excl],
              edges=records, ratio='12/11', atoms=8)
out = Path(__file__).resolve().parents[2] / 'out' / 'certificate_rectangle.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print('PASS exact rational coupling; all four ratios = 12/11')
