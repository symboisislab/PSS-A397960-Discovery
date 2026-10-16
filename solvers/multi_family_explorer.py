# multi_family_explorer.py — solver G
# The exact code that produced a(15) >= 91 (two witnesses, 2026-10-16).
# Run by W. Gu for 600 s (1,052 trials) in an isolated container (python3 -I);
# every emitted configuration is rescored from scratch (bad = 0).
# Written by Gemini 4 Argon in conversation with C.-C. D. Lin; mirror-canonical
# deduplication and the rescoring counter added after W. Gu's review.
# License: MIT. (c) 2026 Chien-Cheng Dennis Lin and Wujie Gu.

import time
import random

def get_mask_and_score(sub):
    mask = 0
    L = len(sub)
    for i in range(L):
        si = sub[i]
        for j in range(i + 1, L):
            mask |= (1 << abs(si - sub[j]))
    return mask, mask.bit_count()

def exact_rescore_set(sub):
    """Independent from-scratch set difference evaluator to audit bitmask scores."""
    return len({abs(a - b) for a in sub for b in sub if a != b})

def get_canonical_step_signature(sub):
    """Returns reflection-invariant canonical step tuple under x -> m - x."""
    steps = tuple(sub[i+1] - sub[i] for i in range(len(sub) - 1))
    rev_steps = tuple(reversed(steps))
    return min(steps, rev_steps)

def multi_family_a15_explorer(max_time_sec=600):
    """
    In a 600-second run (1,052 trials), discovers 2 non-isomorphic families achieving
    a(15) >= 91 with bad = 0 (zero discrepancy between bitmask and set rescoring).
    """
    n, N = 15, 105
    start_time = time.time()
    best_score = 0
    all_extremal_configs = []
    non_isomorphic_families = {}
    trials = 0
    bad = 0  # Counter for any scoring discrepancy

    while time.time() - start_time < max_time_sec:
        trials += 1
        edge_weight = random.uniform(0.5, 4.0)
        noise_level = random.uniform(0.1, 1.2)
        beam_width = 350

        beam = [(1, N, 1 << N, (0, N))]
        for step in range(n - 2):
            next_beam = []
            visited = set()
            for sc, _, mask, sub in beam:
                sub_set = set(sub)
                avail = [y for y in range(1, N) if y not in sub_set]
                for y in random.sample(avail, min(len(avail), 65)):
                    new_sub = tuple(sorted(sub + (y,)))
                    if new_sub in visited:
                        continue
                    visited.add(new_sub)
                    add_m = 0
                    for x in sub:
                        add_m |= (1 << abs(y - x))
                    nm = mask | add_m
                    nsc = nm.bit_count()
                    prio = nsc * 100 + abs(y - N / 2.0) * edge_weight + random.uniform(0, noise_level * 100)
                    next_beam.append((prio, nsc, nm, new_sub))
            next_beam.sort(key=lambda x: x[0], reverse=True)
            beam = [(x[1], 0, x[2], x[3]) for x in next_beam[:beam_width]]

        for sc, _, mask, sub_tuple in beam[:5]:
            curr_sub = list(sub_tuple)
            curr_sc = sc
            for _ in range(40):
                kept = sorted(random.sample(range(1, n), n - 5))
                base = [0] + [curr_sub[i] for i in kept]
                base_set = set(base)
                bm, _ = get_mask_and_score(base)
                cands = []
                for y in range(1, N + 1):
                    if y in base_set:
                        continue
                    ym = 0
                    for x in base:
                        ym |= (1 << abs(y - x))
                    cands.append(((ym & ~bm).bit_count(), abs(y - N / 2.0), y, ym))
                cands.sort(reverse=True)
                cands = cands[:28]
                cy = [c[2] for c in cands]; cm = [c[3] for c in cands]; cg = [c[0] for c in cands]
                L_c = len(cy)
                b_sc = curr_sc; b_add = None

                def dfs4(st, m, last_i, add):
                    nonlocal b_sc, b_add
                    cs = m.bit_count()
                    if st == 4:
                        if cs >= b_sc and sorted(base + add) != curr_sub:
                            b_sc = cs; b_add = add.copy()
                        return
                    rem = 4 - st
                    if cs + rem * (11 + st) + rem * (rem - 1) // 2 < b_sc:
                        return
                    for i in range(last_i + 1, L_c - rem + 1):
                        if cs + rem * cg[i] + rem * (rem - 1) // 2 < b_sc:
                            break
                        y = cy[i]; nm = m | cm[i]
                        for py in add:
                            nm |= (1 << abs(y - py))
                        add.append(y); dfs4(st + 1, nm, i, add); add.pop()

                dfs4(0, bm, -1, [])
                if b_add is not None:
                    curr_sub = sorted(base + b_add)
                    curr_sc = b_sc

            # Independent rescoring audit (bad = 0 check)
            true_sc = exact_rescore_set(curr_sub)
            if true_sc != curr_sc or len(curr_sub) != n or curr_sub[0] != 0 or curr_sub[-1] > N:
                bad += 1
                continue

            if curr_sc > best_score:
                best_score = curr_sc
                all_extremal_configs = [curr_sub]
                non_isomorphic_families = {get_canonical_step_signature(curr_sub): curr_sub}
            elif curr_sc == best_score:
                if curr_sub not in all_extremal_configs:
                    all_extremal_configs.append(curr_sub)
                sig = get_canonical_step_signature(curr_sub)
                if sig not in non_isomorphic_families:
                    non_isomorphic_families[sig] = curr_sub

    print(f"[Explorer Finished] Trials={trials} | Best={best_score} | Families={len(non_isomorphic_families)} | bad={bad}")
    return best_score, trials, bad, all_extremal_configs, list(non_isomorphic_families.values())
