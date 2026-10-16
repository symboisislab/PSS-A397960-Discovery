# reference_lns.py — REFERENCE RE-IMPLEMENTATION, for reading.
# This is NOT the code that produced the reported results (those are solvers A-F,
# to be released with the paper). Measured with seed=42: n=9 -> 32 in 0.07 s,
# n=10 -> 40 in 0.37 s, n=11 -> 49 in 11.8 s, n=12 -> 57 (not 58) within 20 s.
# License: MIT. (c) 2026 Chien-Cheng Dennis Lin and Wujie Gu.

import random
import time

def solve_a397960_lns(n, target_score=None, time_limit=15.0, seed=42):
    """
    Reproducible Deep Tabu Exact-LNS + Bitmask Branch-and-Bound Solver (MIT License).
    Includes independent from-scratch set difference verification (bad = 0 audit).
    """
    random.seed(seed)
    m = n * (n - 1) // 2
    start_time = time.time()
    bad = 0

    def get_mask(sub):
        mask = 0
        for i in range(len(sub)):
            si = sub[i]
            for j in range(i + 1, len(sub)):
                mask |= (1 << abs(si - sub[j]))
        return mask

    def exact_rescore(sub):
        return len({abs(a - b) for a in sub for b in sub if a != b})

    # Stage 1: Randomized Boundary-Biased Beam Search Initialization
    beam = [(0, [0, m])]
    for step in range(n - 2):
        next_beam = {}
        for mask, sub in beam:
            sub_set = set(sub)
            for cand in range(1, m):
                if cand in sub_set:
                    continue
                new_mask = mask
                for x in sub:
                    new_mask |= (1 << abs(cand - x))
                sc = new_mask.bit_count()
                bias = abs(cand - m / 2.0) * 0.05 + random.uniform(0, 0.2)
                key = tuple(sorted(sub + [cand]))
                if key not in next_beam or sc > next_beam[key][0]:
                    next_beam[key] = (sc, sc + bias, new_mask, list(key))
        sorted_cands = sorted(next_beam.values(), key=lambda x: x[1], reverse=True)
        beam = [(x[2], x[3]) for x in sorted_cands[:150]]

    best_mask, best_sub = max(beam, key=lambda x: x[0].bit_count())
    best_score = best_mask.bit_count()

    # Stage 2: Deep Tabu Exact-LNS (Destroy k=4~5 elements + Gen 4 Bitmask B&B DFS Repair)
    curr_sub = list(best_sub)
    tabu_set = {tuple(curr_sub)}

    while time.time() - start_time < time_limit:
        if target_score and best_score >= target_score:
            break
        k = 4 if n <= 13 else 5
        interior_indices = list(range(1, n - 1))
        removed_idx = set(random.sample(interior_indices, k))
        fixed = [curr_sub[i] for i in range(n) if i not in removed_idx]
        base_mask = get_mask(fixed)
        base_score = base_mask.bit_count()

        fixed_set = set(fixed)
        cands = []
        for v in range(1, m):
            if v not in fixed_set:
                dm = 0
                for x in fixed:
                    dm |= (1 << abs(v - x))
                gain = (dm & ~base_mask).bit_count()
                cands.append((gain, v, dm))
        cands.sort(reverse=True)
        cand_vals = [x[1] for x in cands[:45]]
        cand_masks = [x[2] for x in cands[:45]]

        local_best_sc = best_score - 1
        local_best_sub = None

        def dfs(idx, picked, cur_mask, cur_sc):
            nonlocal local_best_sc, local_best_sub
            rem_k = k - len(picked)
            if rem_k == 0:
                full_sub = tuple(sorted(fixed + picked))
                if cur_sc > local_best_sc and full_sub not in tabu_set:
                    local_best_sc = cur_sc
                    local_best_sub = list(full_sub)
                return
            if idx >= len(cand_vals):
                return
            cur_size = len(fixed) + len(picked)
            max_add = rem_k * cur_size + rem_k * (rem_k - 1) // 2
            if cur_sc + min(max_add, m - cur_sc) <= local_best_sc:
                return

            for i in range(idx, len(cand_vals) - rem_k + 1):
                v = cand_vals[i]
                new_m = cur_mask | cand_masks[i]
                for p in picked:
                    new_m |= (1 << abs(v - p))
                dfs(i + 1, picked + [v], new_m, new_m.bit_count())

        dfs(0, [], base_mask, base_score)

        if local_best_sub is not None:
            if exact_rescore(local_best_sub) != local_best_sc:
                bad += 1
                continue
            curr_sub = local_best_sub
            tabu_set.add(tuple(curr_sub))
            if local_best_sc > best_score:
                best_score = local_best_sc
                best_sub = list(curr_sub)

    elapsed = time.time() - start_time
    print(f"[LNS Search Complete] n={n} (m={m}) | Reached Score: {best_score} in {elapsed:.2f}s | bad={bad} | Subset: {best_sub}")
    return best_score, best_sub

if __name__ == "__main__":
    # Measured with seed=42 (see README): n=9..11 reach the OEIS values; n=12 reached 57 (not 58) within 20 s.
    for n_test, target in [(9, 32), (10, 40), (11, 49)]:
        solve_a397960_lns(n_test, target_score=target, time_limit=20.0)
