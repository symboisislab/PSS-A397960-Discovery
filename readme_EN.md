# Project Soul Seed × OEIS A397960: Bi-Level Algorithmic Co-evolution & Constructive Lower Bound Discovery

**Author / Lead Researcher:** Chien-Cheng Dennis Lin ([symboisislab/PSS-A397960-Discovery](https://github.com/symboisislab/PSS-A397960-Discovery))  
**Date of Discovery & Timestamp:** October 14, 2026 (Revised October 15, 2026)  
**Target Sequence:** [OEIS A397960](https://oeis.org/A397960) (*Maximum number of distinct positive differences of an $n$-element subset of $\{0, 1, \dots, n(n-1)/2\}$*, originally authored by Wujie Gu, Aug 2026).  
**Status:** Constructive Lower Bound **$a(15) \ge 90$** Established (9 Valid Configurations Spanning **8 Non-isomorphic Families**) & Constructive Reproduction of Known OEIS Records $a(3) \dots a(14)$.  
**Open-Source License:** Code released under the **MIT License**; constructive data and documentation under **CC BY 4.0** (ensuring both verifiable results and fully reproducible search methodology).

---

## 1. Executive Summary & Epistemic Scope

This research applies the "Algebraic Guardian" and "Invariant Subspace Constraint" natural language control protocols of **Project Soul Seed (PSS)** to the extremal additive combinatorics problem [OEIS A397960](https://oeis.org/A397960).

By constructing a **Bi-Level Closed-Loop Evolutionary System**:
- **Upper-Level Heuristic Generator:** Governed by the PSS protocol (Anti-Sycophancy, locking discrete boundary conditions), a Large Language Model (Gemini 2.5 Flash) evolves Python priority scoring and lookahead search functions.
- **Lower-Level Exact Verifier & LNS Solver:** Executes deterministic, hallucination-free difference set evaluation and Deep Tabu Exact-LNS (Large Neighborhood Search).

Under strict blind-test conditions—without providing any human-expert branch-and-bound (B&B) code—the system **autonomously re-derived combinatorial upper-bound pruning inequalities algebraically equivalent to those of human mathematicians within 4 evolutionary generations**, automatically introducing bitmasking acceleration and Golomb ruler boundary geometric bias. Combined with Deep Tabu Exact-LNS, the system **constructively reproduced all known OEIS records for $n = 3 \dots 14$** within seconds on a single commodity instance. Furthermore, for the previously unestablished term **$n = 15$ ($m = 105$)**, the system established a constructive lower bound of **$a(15) \ge 90$**, uncovering 9 valid subsets generating 90 distinct positive differences, which—after accounting for one reflection-symmetric twin pair—span **8 mutually non-isomorphic extremal lattice families**.

> **⚠️ Important Epistemic Scope Statement (Constructive Lower Bound vs. Exhaustive Upper-Bound Proof):**  
> Providing an explicit subset $A \subseteq \{0, \dots, 105\}$ with $\vert{}A\vert{} = 15$ that generates 90 distinct positive differences rigorously establishes the **constructive lower bound $a(15) \ge 90$**; it does **not** constitute an exhaustive proof that $a(15) = 90$. Proving the matching upper bound $a(15) \le 90$ (i.e., refuting the existence of any subset yielding 91 distinct differences) requires an exhaustive Branch-and-Bound or SAT/ILP tree traversal. The `best = 90` constructive lower bound provided herein serves as a strong initial pruning bound to accelerate such exhaustive verification.

---

## 2. Four-Generation AI Algorithmic Evolution Log

Under a blind test where Generation 0 was initialized only with a naive single-step greedy seed—and where the evaluation harness intentionally contained misleading reference targets (such as labeling $n = 7$ as 18 and $n = 8$ as 28)—the PSS constraint protocol guided the model through a four-stage algorithmic transition:

| Evolutionary Generation | Emergent Algorithmic Structure | $n=4$ | $n=5$ | $n=6$ | $n=7$ | $n=8$ | Verification Total Score | Key Breakthrough Significance |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gen 0** | Pure Single-Step Greedy | 5 | 8 | 13 | 18 | 23 | 67 | Trapped in local optima |
| **Gen 1** | Geometric Boundary Weight (`abs(cand - N/2)` + collision penalty) | **6** | **9** | **13** | **19** | 25 | 72 | Overcame misleading script targets, autonomously menemukan known optimum $a(7) = 19$ |
| **Gen 2** | 3-Step Lookahead Tree with $O(1)$ Early Stopping | **6** | **9** | **13** | **19** | 25 | 72 | Spontaneous transition from static algebraic formulas to multi-step search trees |
| **Gen 3** | Dynamic Beam Search + Path Multiplicity | **6** | **9** | **13** | **19** | **26** | **73** | Reached $a(8) = 26$; $n = 4 \dots 8$ all matched known OEIS optimal records |
| **Gen 4** | **Bitmask DFS + Combinatorial Upper-Bound Pruning (Bitmask B&B)** | **6** | **9** | **13** | **19** | **26** | **73** | **Autonomously derived the strict pruning inequality `rem*(n-rem) + rem*(rem-1)//2`** |

---

## 3. Constructive Reproduction of Known OEIS Records $a(9) \dots a(14)$

Combining the bitmasking, boundary heuristic sorting, and Deep Tabu Exact-LNS (destroying $k = 4 \sim 6$ interior elements and reconstructing via B&B DFS per iteration) evolved in Gen 3/4, the system constructively reproduced all known values of [OEIS A397960](https://oeis.org/A397960) as of September 2026 in a standalone Google Colab environment:

| Term $n$ | Max Range $m = n(n-1)/2$ | Known OEIS Record | Reached Lower Bound | Search Runtime (Colab CPU) | Constructive Witness Subset $A$ | Adjacent Step Sizes |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **9** | 36 | 32 | **32** | 0.21s | `[0, 1, 3, 13, 20, 27, 31, 35, 36]` | `[1, 2, 10, 7, 7, 4, 4, 1]` |
| **10** | 45 | 40 | **40** | 0.32s | `[0, 1, 7, 11, 15, 24, 40, 42, 43, 45]` | `[1, 6, 4, 4, 9, 16, 2, 1, 2]` |
| **11** | 55 | 49 | **49** | 0.51s | `[0, 1, 2, 6, 17, 25, 33, 43, 46, 53, 55]` | `[1, 1, 4, 11, 8, 8, 10, 3, 7, 2]` |
| **12** | 66 | 58 | **58** | 2.20s | `[0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66]` | `[1, 1, 4, 11, 9, 9, 9, 12, 2, 5, 3]` |
| **13** | 78 | 68 | **68** | 4.42s | `[0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78]` | `[1, 1, 10, 1, 16, 4, 15, 7, 9, 6, 3, 5]` |
| **14** | 91 | 79 | **79** | 8.31s | `[0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91]` | `[1, 3, 7, 13, 5, 13, 13, 19, 2, 6, 6, 2, 1]` |

---

## 4. Constructive Lower Bound $a(15) \ge 90$, Isomorphism Analysis, and the "Mid-Ruler Arithmetic Progression Core"

For the unknown term $n = 15$ ($m = 105$), utilizing multi-family randomized beam search and local exact repair (Multi-Family Randomized Beam + Exact-LNS), the system grew 47 independent evolution trees from scratch, uncovering **9 valid subsets achieving 90 distinct positive differences (each leaving 15 missing differences)**.

### 4.1 Reflection Isomorphism Check: 9 Configurations Spanning 8 Non-Isomorphic Families
In difference set problems, a subset $A$ and its reflection $A' = \{m - x \mid x \in A\}$ generate the exact same set of positive differences and belong to the same equivalence class (isomorphic family). Comparing the adjacent step sequences:
- **Config #3** has step sequence `[1, 4, 10, 13, 12, 12, 12, 12, 7, 2, 9, 2, 6, 3]`;
- **Config #6** has step sequence `[3, 6, 2, 9, 2, 7, 12, 12, 12, 12, 13, 10, 4, 1]` (the exact reversal of Config #3, i.e., its $105 - x$ reflection twin).
- The remaining 7 configurations are neither translations nor reflections of one another. Consequently, these 9 configurations represent **8 mutually non-isomorphic structural families (Families A–H)**:

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

### 4.2 Structural Insight: The Mid-Ruler Arithmetic Progression Trade-off
Observing the extremal constructions above across multiple scales:
- $n = 11$: `17, 25, 33` form an arithmetic progression with common difference 8 (steps `[8, 8]`);
- $n = 12$: `17, 26, 35, 44` form an arithmetic progression with common difference 9 (steps `[9, 9, 9]`);
- $n = 14$: `29, 42, 55` form an arithmetic progression with common difference 13 (steps `[13, 13]`);
- $n = 15$ Family C (#2) and Family D (#3, #6): The middle segments naturally exhibit continuous arithmetic progressions with **common difference $\Delta = 12$** (`21, 33, 45, 57`, `28, 40, 52, 64, 76`, and `29, 41, 53, 65, 77`).

**Algebraic Explanation:** Under the tight domain bound $m = n(n-1)/2$, perfect Golomb rulers no longer exist for $n \ge 5$, making difference collisions mathematically inevitable. To maximize the number of distinct differences, extremal constructions adopt an algebraic trade-off of "localizing collisions to maximize global cross-coverage": by placing an arithmetic progression core in the middle, inevitable collision penalties are concentrated and locked within multiples of the common difference $\Delta$ in the interior, thereby enabling the high-density boundary combs at both ends to achieve near-collision-free spreading when cross-subtracted against the middle lattice.

---

## 5. Standalone Verification & Isomorphism Check Script

Anyone can run the following zero-dependency Python script to deterministically verify the validity, distinct difference counts, and reflection symmetries of all subsets above within milliseconds (confirming that the 9 configurations for $n=15$ span 8 distinct non-isomorphic families):

```python
def verify_and_analyze(n, subset, label=""):
    m = n * (n - 1) // 2
    assert len(subset) == n, f"Length mismatch: expected {n}, got {len(subset)}"
    assert subset[0] == 0 and subset[-1] <= m, f"Out of range [0, {m}]"
    assert sorted(subset) == subset and len(set(subset)) == n, "Subset must be strictly increasing"
    
    diffs = {abs(a - b) for a in subset for b in subset if a != b}
    steps = [subset[i+1] - subset[i] for i in range(n - 1)]
    missing = sorted(list(set(range(1, m + 1)) - diffs))
    print(f"[{label:<20}] n={n:<2} (m={m:<3}) | Distinct Diffs: {len(diffs)} | Subset: {subset}")
    print(f"   -> Adjacent Steps : {steps}")
    print(f"   -> Missing ({len(missing):<2})   : {missing}\n")
    return tuple(steps)

if __name__ == "__main__":
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

    a15_configs = [
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
    
    canonical_families = set()
    for i, cfg in enumerate(a15_configs):
        steps = verify_and_analyze(15, cfg, f"a(15)>=90 Config #{i}")
        rev_steps = tuple(reversed(steps))
        # Use the lexicographically smaller of step sequence and its reversal as canonical representative
        canonical_rep = min(steps, rev_steps)
        if canonical_rep in canonical_families:
            print(f"   [Isomorphism Note] Config #{i} is a reflection-symmetric twin (105 - x) of an earlier configuration.\n")
        canonical_families.add(canonical_rep)

    print(f"=== Summary: Verified {len(a15_configs)} valid configurations for a(15) >= 90, representing {len(canonical_families)} distinct non-isomorphic families. ===")
```

---

## 6. Reproducible Search Methodology: Open-Source Exact-LNS & Beam Solver

To ensure this repository provides not only **verifiable results** but also a fully **reproducible methodology**, we release the standalone implementation of our **Deep Tabu Exact-LNS + Bitmask Branch-and-Bound Solver** under the **MIT License**. Any researcher can execute the zero-dependency script below to independently reproduce the search trajectories for $a(9) \dots a(14)$ and multi-family exploration for $a(15) \ge 90$ from scratch:

```python
import random
import time

def solve_a397960_lns(n, target_score=None, time_limit=15.0, seed=42):
    """
    Reproducible Deep Tabu Exact-LNS + Bitmask Branch-and-Bound Solver (MIT License).
    Combines Gen 1 boundary geometric bias, Gen 3 randomized beam seeding,
    and Gen 4 bitwise B&B exact neighborhood reconstruction.
    """
    random.seed(seed)
    m = n * (n - 1) // 2
    start_time = time.time()

    def get_mask(sub):
        mask = 0
        for i in range(len(sub)):
            si = sub[i]
            for j in range(i + 1, len(sub)):
                mask |= (1 << abs(si - sub[j]))
        return mask

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
                # Gen 1 evolved Golomb-ruler boundary geometric preference
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

        # Sort candidates by marginal difference gain
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
            # Gen 4 autonomously derived combinatorial upper-bound pruning inequality:
            # max_new_diffs <= rem_k * current_size + rem_k * (rem_k - 1) // 2
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
            curr_sub = local_best_sub
            tabu_set.add(tuple(curr_sub))
            if local_best_sc > best_score:
                best_score = local_best_sc
                best_sub = list(curr_sub)

    elapsed = time.time() - start_time
    print(f"[LNS Search Complete] n={n} (m={m}) | Reached Score: {best_score} in {elapsed:.2f}s | Subset: {best_sub}")
    return best_score, best_sub

if __name__ == "__main__":
    for n_test, target in [(9, 32), (10, 40), (11, 49), (12, 58)]:
        solve_a397960_lns(n_test, target_score=target, time_limit=10.0)
```

---

## 7. Open-Source License & Collaboration Notice

- **Code License (MIT License):** All verification and search algorithm scripts in this repository (including the Bitmask B&B and Deep Tabu Exact-LNS solver) are released under the open-source MIT License for unrestricted academic verification, reproduction, and extension.
- **Data & Documentation License (CC BY 4.0):** Constructive witness subsets and structural analyses are licensed under CC BY 4.0. Please attribute both Wujie Gu (author of OEIS A397960) and Chien-Cheng Dennis Lin ($a(15) \ge 90$ constructive lower-bound witnesses and mid-ruler arithmetic progression analysis) when citing.

© 2026 Chien-Cheng Dennis Lin (Symbiosis Lab). Released under MIT License & CC BY 4.0.
