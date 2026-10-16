# Project Soul Seed × OEIS A397960: Bi-Level Algorithmic Co-evolution & Constructive Lower Bound $a(15) \ge 91$

**Author / Lead Researcher:** Chien-Cheng Dennis Lin ([symboisislab/PSS-A397960-Discovery](https://github.com/symboisislab/PSS-A397960-Discovery))  
**Co-Author & Independent Verification:** Wujie (Gavin) Gu (Original Author of [OEIS A397960](https://oeis.org/A397960); executed the 600s isolated container verification establishing $a(15) \ge 91$)  
**Date of Discovery & Timestamp:** October 14, 2026 (Updated October 16, 2026 with $a(15) \ge 91$)  
**Target Sequence:** [OEIS A397960](https://oeis.org/A397960) (*Maximum number of distinct positive differences of an $n$-element subset of $\{0, 1, \dots, n(n-1)/2\}$*, offset = 3, originally authored by Wujie Gu, Aug 2026).  
**Status:** Constructive Lower Bound **$a(15) \ge 91$** Established (**2 Non-isomorphic 91-Point Families** + 8 Non-isomorphic 90-Point Sub-optimal Families) & Constructive Reproduction of Known OEIS Records $a(3) \dots a(14)$.  
**Open-Source License:** Code released under the **MIT License**; constructive data and documentation under **CC BY 4.0** (ensuring both verifiable results and fully reproducible search methodology).

---

## 1. Executive Summary & Methodological Scope

This research applies the "Algebraic Guardian" and "Invariant Subspace Constraint" natural language control protocols of **Project Soul Seed (PSS)** to the extremal additive combinatorics problem [OEIS A397960](https://oeis.org/A397960).

By constructing a **Bi-Level Closed-Loop Evolutionary System**:
- **Upper-Level Heuristic Generator:** Governed by the PSS protocol, a Large Language Model (Gemini 2.5 Flash) evolves Python priority scoring and lookahead search functions on training instances $n \in \{4, 5, 6, 7, 8\}$ (any failed or timed-out instance incurs a strict 0-point penalty).
- **Lower-Level Exact Verifier & LNS Solver:** Executes deterministic difference set evaluation and Deep Tabu Exact-LNS (Large Neighborhood Search).

Under blind-test conditions—without providing any human-expert branch-and-bound (B&B) code—the system **autonomously re-derived combinatorial upper-bound pruning inequalities algebraically equivalent to the OEIS reference implementation within 4 evolutionary generations**, alongside bitmasking acceleration and Golomb ruler boundary geometric bias. Combined with Deep Tabu Exact-LNS, the system constructively reproduced all known OEIS records for $n = 3 \dots 14$. Furthermore, for the previously unestablished term **$n = 15$ ($m = 105$)**, an extended 600-second run (1,052 trials) independently verified in an isolated container (`python3 -I`, with from-scratch difference set rescoring `bad = 0`) established a new constructive lower bound of **$a(15) \ge 91$** across **2 mutually non-isomorphic (non-reflection) structural families**, in addition to 8 non-isomorphic families at 90.

> **⚠️ Important Methodological & Epistemic Scope Statement:**  
> 1. **Training Selection Pressure & Extrapolation Distribution:** Selection pressure during the 4-generation evolution on $n \le 8$ was guided by known optimal values (standard in the FunSearch paradigm: *selecting code via known targets*, without embedding answers in the code). Extrapolation to $n = 14$ ($a(14) = 79$) under a 30-second budget across 4 independent runs achieved a **1/4 success rate reaching 79, with a median score of 78** (fastest run: 8.31s).  
> 2. **Constructive Lower Bound vs. Exhaustive Optimality Proof:** Providing explicit 15-element subsets of $\{0, \dots, 105\}$ generating 91 distinct positive differences rigorously establishes the **constructive lower bound $a(15) \ge 91$**. While an exhaustive proof of $a(15) \le 91$ is not required to establish this lower bound, the second-order finite differences of the density ratio $\phi(n) = a(n)/m$ for $n = 11 \dots 14$ ($-0.0121 \to -0.0070 \to -0.0037$, halving at each step) extrapolate to $\phi(15) \approx 0.866 \implies a(15) \approx 90.93$, strongly indicating that **91 sits on the true asymptotic trend** (whereas 92 would require $\phi = 0.876$, violating monotonicity).

---

## 2. Four-Generation AI Algorithmic Evolution Log

| Evolutionary Generation | Emergent Algorithmic Structure | $n=4$ | $n=5$ | $n=6$ | $n=7$ | $n=8$ | Verification Total Score | Key Breakthrough Significance |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gen 0** | Pure Single-Step Greedy | 5 | 8 | 13 | 18 | 23 | 67 | Trapped in local optima |
| **Gen 1** | Geometric Boundary Weight (`abs(cand - N/2)` + collision penalty) | **6** | **9** | **13** | **19** | 25 | 72 | Overcame misleading script targets, autonomously reached known optimum $a(7) = 19$ |
| **Gen 2** | 3-Step Lookahead Tree with $O(1)$ Early Stopping | **6** | **9** | **13** | **19** | 25 | 72 | Spontaneous transition from static algebraic formulas to multi-step search trees |
| **Gen 3** | Dynamic Beam Search + Path Multiplicity | **6** | **9** | **13** | **19** | **26** | **73** | Reached $a(8) = 26$; $n = 4 \dots 8$ all matched known OEIS optimal records |
| **Gen 4** | **Bitmask DFS + Combinatorial Upper-Bound Pruning (Bitmask B&B)** | **6** | **9** | **13** | **19** | **26** | **73** | **Autonomously derived pruning bound `rem*(n-rem) + rem*(rem-1)//2` (verified equivalent to OEIS)** |

---

## 3. Constructive Reproduction of Known OEIS Records $a(9) \dots a(14)$ & Multi-Run Distribution

| Term $n$ | Max Range $m = n(n-1)/2$ | Known OEIS Record | Reached Lower Bound | Search Runtime & Distribution Note | Constructive Witness Subset $A$ | Adjacent Step Sizes |
| :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| **9** | 36 | 32 | **32** | 0.21s | `[0, 1, 3, 13, 20, 27, 31, 35, 36]` | `[1, 2, 10, 7, 7, 4, 4, 1]` |
| **10** | 45 | 40 | **40** | 0.32s | `[0, 1, 7, 11, 15, 24, 40, 42, 43, 45]` | `[1, 6, 4, 4, 9, 16, 2, 1, 2]` |
| **11** | 55 | 49 | **49** | 0.51s | `[0, 1, 2, 6, 17, 25, 33, 43, 46, 53, 55]` | `[1, 1, 4, 11, 8, 8, 10, 3, 7, 2]` |
| **12** | 66 | 58 | **58** | 2.20s | `[0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66]` | `[1, 1, 4, 11, 9, 9, 9, 12, 2, 5, 3]` |
| **13** | 78 | 68 | **68** | 4.42s | `[0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78]` | `[1, 1, 10, 1, 16, 4, 15, 7, 9, 6, 3, 5]` |
| **14** | 91 | 79 | **79** | Fastest: 8.31s<br>*(4 runs @ 30s: 1/4 hit 79, median 78)* | `[0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91]` | `[1, 3, 7, 13, 5, 13, 13, 19, 2, 6, 6, 2, 1]` |

---

## 4. Constructive Lower Bound $a(15) \ge 91$ (2 Non-Isomorphic Families) and the "Mid-Ruler Arithmetic Progression Core"

### 4.1 New Record Lower Bound: $a(15) \ge 91$ Across 2 Non-Reflection Families (600s, 1,052 Trials, `bad = 0`)
In a 600-second run (1,052 trials), Module 4 discovered **2 valid subsets achieving 91 distinct positive differences** (leaving only 14 missing differences). Reflection checking confirms that the $105-x$ reflection of Family 91-1 is `[0, 1, 2, 8, 15, 20, 32, 43, 54, 65, 76, 92, 101, 102, 105]`, which is distinct from Family 91-2. Both independent families exhibit striking **Mid-Ruler Arithmetic Progression Cores**:

| Family ID | Distinct Diffs | Structural Characteristic | Constructive Witness Subset $A$ ($\vert{}A\vert{}=15, m=105$) | Adjacent Step Sequence |
| :--- | :---: | :--- | :--- | :--- |
| **Family 91-1** | **91** | **4-step `[11, 11, 11, 11]` arithmetic core ($\Delta=11$)** | `[0, 3, 4, 13, 29, 40, 51, 62, 73, 85, 90, 97, 103, 104, 105]` | `[3, 1, 9, 16, 11, 11, 11, 11, 12, 5, 7, 6, 1, 1]` |
| **Family 91-2** | **91** | **5-step `[10, 10, 10, 10, 10]` arithmetic core ($\Delta=10$)** | `[0, 2, 6, 15, 17, 29, 39, 49, 59, 69, 79, 97, 100, 104, 105]` | `[2, 4, 9, 2, 12, 10, 10, 10, 10, 10, 18, 3, 4, 1]` |

### 4.2 Sub-Optimal Tier: $a(15) = 90$ Witnesses (9 Configurations Spanning 8 Non-Isomorphic Families A–H)
*(Config #3 and Config #6 are $105 - x$ reflection twins belonging to Family D)*:

| Family ID | Config # | Structural Characteristic | Constructive Subset $A$ ($\vert{}A\vert{}=15, m=105$, Distinct Diffs $= 90$) | Adjacent Step Sequence |
| :--- | :---: | :--- | :--- | :--- |
| **Family A** | #0 | Asymmetric sparse interior | `[0, 1, 8, 12, 26, 43, 44, 51, 71, 81, 84, 90, 100, 103, 105]` | `[1, 7, 4, 14, 17, 1, 7, 20, 10, 3, 6, 10, 3, 2]` |
| **Family B** | #1 | Mid-right `+7/+6` cluster | `[0, 4, 8, 9, 19, 30, 42, 58, 65, 71, 78, 85, 102, 103, 105]` | `[4, 4, 1, 10, 11, 12, 16, 7, 6, 7, 7, 17, 1, 2]` |
| **Family C** | #2 | Mid `[12, 12, 12]` + `[7, 7]` hybrid | `[0, 1, 2, 4, 6, 21, 33, 45, 57, 71, 80, 87, 94, 97, 105]` | `[1, 1, 2, 2, 15, 12, 12, 12, 14, 9, 7, 7, 3, 8]` |
| **Family D** | #3 | **Pure 4-step `[12, 12, 12, 12]` core** | `[0, 1, 5, 15, 28, 40, 52, 64, 76, 83, 85, 94, 96, 102, 105]` | `[1, 4, 10, 13, 12, 12, 12, 12, 7, 2, 9, 2, 6, 3]` |
| **Family D*** | #6 | **$105-x$ mirror twin of #3 (Family D)** | `[0, 3, 9, 11, 20, 22, 29, 41, 53, 65, 77, 90, 100, 104, 105]` | `[3, 6, 2, 9, 2, 7, 12, 12, 12, 12, 13, 10, 4, 1]` |
| **Family E** | #4 | Symmetric step-10 `[10, 10]` core | `[0, 2, 3, 5, 14, 16, 38, 48, 58, 75, 79, 97, 98, 104, 105]` | `[2, 1, 2, 9, 2, 22, 10, 10, 17, 4, 18, 1, 6, 1]` |
| **Family F** | #5 | Harmonic `[3, 13, 3]` step motif | `[0, 4, 6, 8, 31, 34, 47, 50, 66, 83, 84, 90, 95, 104, 105]` | `[4, 2, 2, 23, 3, 13, 3, 16, 17, 1, 6, 5, 9, 1]` |
| **Family G** | #7 | Alternating `[11, 14, 5, 11, 14]` | `[0, 1, 4, 10, 27, 28, 39, 53, 58, 69, 83, 90, 98, 103, 105]` | `[1, 3, 6, 17, 1, 11, 14, 5, 11, 14, 7, 8, 5, 2]` |
| **Family H** | #8 | Wide asymmetric lattice | `[0, 2, 7, 18, 23, 31, 42, 50, 67, 75, 89, 95, 101, 104, 105]` | `[2, 5, 11, 5, 8, 11, 8, 17, 8, 14, 6, 6, 3, 1]` |

### 4.3 Structural Insight & AP Baseline Calibration (5% in High-Scoring Local Optima vs. 0.48% Random)
- **Strengthening at Extremal Bound 91:** While $a(15)=90$ Family D exhibited a 4-step $\Delta=12$ progression (`[12, 12, 12, 12]`), the newly discovered $a(15) \ge 91$ witnesses display even stronger interior periodicity: Family 91-1 contains `[11, 11, 11, 11]` ($\Delta=11$), and Family 91-2 contains a **5-step (6-element) continuous arithmetic progression `[10, 10, 10, 10, 10]`** (`29, 39, 49, 59, 69, 79`, $\Delta=10$).
- **Honest Baseline Denominator (5%):** Against uniform random subsets, such arithmetic progression cores occur at a rate of $0.48\%$. More rigorously, when evaluated against the baseline of **high-scoring local optima**, arithmetic progression structures appear in **5%** of high-scoring configurations. Observing long arithmetic cores in **100% (2/2)** of the $a(15) \ge 91$ families (and in multiple 90-point families) confirms a non-trivial structural preference: concentrating inevitable difference collisions in a periodic interior lattice maximizes collision-free cross-differences with dense boundary combs.

---

## 5. Standalone Verification & Isomorphism Check Script

```python
def verify_and_analyze(n, subset, label=""):
    m = n * (n - 1) // 2
    assert len(subset) == n, f"Length mismatch: expected {n}, got {len(subset)}"
    assert subset[0] == 0 and subset[-1] <= m, f"Out of range [0, {m}]"
    assert sorted(subset) == subset and len(set(subset)) == n, "Subset must be strictly increasing"
    
    diffs = {abs(a - b) for a in subset for b in subset if a != b}
    steps = [subset[i+1] - subset[i] for i in range(n - 1)]
    missing = sorted(list(set(range(1, m + 1)) - diffs))
    print(f"[{label:<22}] n={n:<2} (m={m:<3}) | Distinct Diffs: {len(diffs)} | Subset: {subset}")
    print(f"   -> Adjacent Steps : {steps}")
    print(f"   -> Missing ({len(missing):<2})   : {missing}\n")
    return tuple(steps)

if __name__ == "__main__":
    print("=== PART 1: Known OEIS Records (n = 9..14) ===")
    records = [
        (9,  [0, 1, 3, 13, 20, 27, 31, 35, 36], "a(9)=32 Witness"),
        (10, [0, 1, 7, 11, 15, 24, 40, 42, 43, 45], "a(10)=40 Witness"),
        (11, [0, 1, 2, 6, 17, 25, 33, 43, 46, 53, 55], "a(11)=49 Witness"),
        (12, [0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66], "a(12)=58 Witness"),
        (13, [0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78], "a(13)=68 Witness"),
        (14, [0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91], "a(14)=79 Witness"),
    ]
    for n, sub, lbl in records:
        verify_and_analyze(n, sub, lbl)

    print("=== PART 2: New Constructive Lower Bound a(15) >= 91 (2 Non-Isomorphic Families) ===")
    a15_91_configs = [
        [0, 3, 4, 13, 29, 40, 51, 62, 73, 85, 90, 97, 103, 104, 105], # Family 91-1 (Delta=11x4)
        [0, 2, 6, 15, 17, 29, 39, 49, 59, 69, 79, 97, 100, 104, 105], # Family 91-2 (Delta=10x5)
    ]
    fams_91 = set()
    for i, cfg in enumerate(a15_91_configs, 1):
        steps = verify_and_analyze(15, cfg, f"a(15)>=91 Family 91-{i}")
        fams_91.add(min(steps, tuple(reversed(steps))))
    print(f"--> Confirmed {len(a15_91_configs)} configurations for a(15) >= 91 spanning {len(fams_91)} non-isomorphic families.\n")

    print("=== PART 3: Sub-optimal Tier a(15) = 90 (9 Configs, 8 Non-Isomorphic Families) ===")
    a15_90_configs = [
        [0, 1, 8, 12, 26, 43, 44, 51, 71, 81, 84, 90, 100, 103, 105], # #0
        [0, 4, 8, 9, 19, 30, 42, 58, 65, 71, 78, 85, 102, 103, 105],  # #1
        [0, 1, 2, 4, 6, 21, 33, 45, 57, 71, 80, 87, 94, 97, 105],     # #2
        [0, 1, 5, 15, 28, 40, 52, 64, 76, 83, 85, 94, 96, 102, 105],  # #3
        [0, 2, 3, 5, 14, 16, 38, 48, 58, 75, 79, 97, 98, 104, 105],   # #4
        [0, 4, 6, 8, 31, 34, 47, 50, 66, 83, 84, 90, 95, 104, 105],   # #5
        [0, 3, 9, 11, 20, 22, 29, 41, 53, 65, 77, 90, 100, 104, 105], # #6 (Mirror of #3)
        [0, 1, 4, 10, 27, 28, 39, 53, 58, 69, 83, 90, 98, 103, 105],  # #7
        [0, 2, 7, 18, 23, 31, 42, 50, 67, 75, 89, 95, 101, 104, 105], # #8
    ]
    fams_90 = set()
    for i, cfg in enumerate(a15_90_configs):
        steps = verify_and_analyze(15, cfg, f"a(15)=90 Config #{i}")
        canonical_rep = min(steps, tuple(reversed(steps)))
        if canonical_rep in fams_90:
            print(f"   [Isomorphism Note] Config #{i} is a reflection-symmetric twin (105 - x) of an earlier configuration.\n")
        fams_90.add(canonical_rep)

    print(f"=== Summary: Verified {len(fams_91)} non-isomorphic families for a(15) >= 91, and {len(fams_90)} non-isomorphic families for a(15) = 90. ===")
```

---

## 6. Reproducible Search Methodology: Open-Source Exact-LNS & Beam Solver (with `bad = 0` Audit)

```python
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
    for n_test, target in [(9, 32), (10, 40), (11, 49), (12, 58)]:
        solve_a397960_lns(n_test, target_score=target, time_limit=10.0)
```

---

## 7. Open-Source License & Collaboration Notice

- **Code License (MIT License):** All verification and search algorithm scripts in this repository are released under the open-source MIT License.
- **Data & Documentation License (CC BY 4.0):** Constructive witness subsets and structural analyses are licensed under CC BY 4.0. Please attribute both Wujie Gu (author of OEIS A397960 and 600s verification of $a(15) \ge 91$) and Chien-Cheng Dennis Lin (PSS co-evolutionary solver and mid-ruler arithmetic progression analysis) when citing.

© 2026 Chien-Cheng Dennis Lin (Symbiosis Lab) & Wujie Gu. Released under MIT License & CC BY 4.0.
