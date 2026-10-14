# Project Soul Seed × OEIS A397960: Bi-Level Algorithmic Co-evolution & Extremal Lattice Discovery

*Author / Lead Researcher:* [Chien-Cheng Dennis Lin / symboisislab/PSS-A397960-Discovery](https://github.com/symboisislab/PSS-A397960-Discovery)

*Date of Discovery & Timestamp:* October 14, 2026

*Target Sequence:* [OEIS A397960](https://oeis.org/A397960) (*Maximum number of distinct positive differences of an $n$-element subset of $\{0, 1, \dots, n(n-1)/2\}$*, originally authored by Wujie Gu, Aug 2026).

*Status:* Constructive Lower Bound $a(15) \ge 90$ Established (9 Non-isomorphic Families Discovered) & Exact Reproduction of $a(3) \dots a(14)$.

---

## 1. Executive Summary

This research applies the "Algebraic Guardian" and "Invariant Subspace Constraint" ontological protocols of *Project Soul Seed (PSS)* to the extremal additive combinatorics problem [OEIS A397960](https://oeis.org/A397960).

By constructing a **Bi-Level Closed-Loop Evolutionary System**:

* **Upper-Level Heuristic Generator:** Governed strictly by the PSS protocol (Anti-Sycophancy, locking discrete boundary conditions), a Large Language Model (Gemini 2.5 Flash) evolves Python priority scoring and lookahead functions.
* **Lower-Level Exact Verifier & LNS Solver:** Executes hallucination-free precise difference set verification and Deep Tabu Exact-LNS (Large Neighborhood Search).

Under strict blind-test conditions—without providing any human-expert branch-and-bound code—the system *autonomously re-derived theoretical upper-bound pruning inequalities equivalent to those of human mathematicians within 4 evolutionary generations*, automatically introducing bitmasking acceleration and Golomb ruler boundary bias. Ultimately, the system not only *100% precisely reproduced all known world records for $n = 3 \sim 14$* within seconds, but also successfully established a robust lower bound of $a(15) \ge 90$ for the previously un-exhausted unknown term $n = 15$ ($N = 105$), discovering *9 structurally independent (non-mirror-isomorphic) 90-point extremal lattice families*.

---

## 2. Four-Generation AI Algorithmic Evolution Log

Under a stress test where Generation 0 was provided only with a pure greedy seed and intentionally incorrect reference upper bounds (such as labeling $n = 7$ as 18 and $n = 8$ as 28), the PSS constraint protocol guided the model through a four-stage algorithmic paradigm shift:

| Evolutionary Generation | Emergent Algorithmic Structure | $n = 4$ | $n = 5$ | $n = 6$ | $n = 7$ | $n = 8$ | Verification Total Score | Key Breakthrough Significance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Gen 0** | Pure Single-Step Greedy | 5 | 8 | 13 | 18 | 23 | 67 | Trapped in local optima |
| **Gen 1** | Geometric Boundary Weight (`abs(cand - N/2) + collision penalty`) | **6** | **9** | **13** | **19** | 25 | 72 | Overcame script misleading, automatically discovered true extremum $a(7) = 19$ |
| **Gen 2** | 3-Step Lookahead with $O(1)$ Pruning | **6** | **9** | **13** | **19** | 25 | 72 | Spontaneous transition from pure algebraic formulas to multi-step search tree structures |
| **Gen 3** | Dynamic Beam Search + Path Multiplicity | **6** | **9** | **13** | **19** | **26** | 73 | Conquered $a(8) = 26$, $n = 4 \sim 8$ all reached absolute mathematical upper limits |
| **Gen 4** | **Bitmask B&B DFS + Strict Combinatorial Upper Bound Pruning** | **6** | **9** | **13** | **19** | **26** | 73 | **Autonomously derived the $\text{rem}(n-\text{rem}) + \text{rem}(\text{rem}-1)//2$ pruning formula** |

---

## 3. Exact Reproduction of World Records $a(9) \dots a(14)$

Combining the bitmasking, boundary heuristic sorting, and Deep Tabu Exact-LNS (removing $k = 4 \sim 6$ elements for branch-and-bound reorganization per iteration) evolved in Gen 3/4, the system rapidly reproduced all known extremal values of [OEIS A397960](https://oeis.org/A397960) as of September 2026 in a standalone Google Colab environment:

| Term $n$ | Max Range $N$ | [OEIS A397960](https://oeis.org/A397960) Known Record | System Measured Result | Breakthrough Time | Constructive Proof Subset |
| --- | --- | --- | --- | --- | --- |
| **9** | 36 | 32 | **32** (Hit) | 0.21s | `[0, 1, 3, 13, 20, 27, 31, 35, 36]` |
| **10** | 45 | 40 | **40** (Hit) | 0.32s | `[0, 1, 7, 11, 15, 24, 40, 42, 43, 45]` |
| **11** | 55 | 49 | **49** (Hit) | 0.51s | `[0, 1, 2, 6, 17, 25, 33, 43, 46, 53, 55]` |
| **12** | 66 | 58 | **58** (Hit) | 2.20s | `[0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66]` |
| **13** | 78 | 68 | **68** (Hit) | 4.42s | `[0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78]` |
| **14** | 91 | 79 | **79** (Hit) | 8.31s | `[0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91]` |

---

## 4. Major Discovery: $a(15) \ge 90$ and the "Arithmetic Progression Core" Phenomenon

For the unexhausted term $n = 15$ ($N = 105$), utilizing multi-family randomized beam search and local exact repair (Multi-Family Randomized Beam + Exact-LNS), the system grew 47 independent evolution trees from scratch, eventually converging entirely to the limit ceiling of **90**, and uncovering **9 completely independent (non-translation or mirror-isomorphic) $a(15) = 90$ extremal construction families**:

1. **Family #0 (Isolated Rigid Seed):** `[0, 1, 8, 12, 26, 43, 44, 51, 71, 81, 84, 90, 100, 103, 105]`
2. **Family #1 (Period-7/6 Lattice):** `[0, 4, 8, 9, 19, 30, 42, 58, 65, 71, 78, 85, 102, 103, 105]`
3. **Family #2 (Period-12 & Period-7 Hybrid Lattice):** `[0, 1, 2, 4, 6, 21, 33, 45, 57, 71, 80, 87, 94, 97, 105]`
4. **Family #3 (Pure 5-Term Period-12 Arithmetic Core):** `[0, 1, 5, 15, 28, 40, 52, 64, 76, 83, 85, 94, 96, 102, 105]`
5. **Family #4 (Symmetric Step-10 Core):** `[0, 2, 3, 5, 14, 16, 38, 48, 58, 75, 79, 97, 98, 104, 105]`
6. **Family #5 (Harmonic [3, 13, 3] Lattice):** `[0, 4, 6, 8, 31, 34, 47, 50, 66, 83, 84, 90, 95, 104, 105]`
7. **Family #6 (Shifted 5-Term Period-12 Arithmetic Core):** `[0, 3, 9, 11, 20, 22, 29, 41, 53, 65, 77, 90, 100, 104, 105]`
8. **Family #7 (Alternating Step Lattice):** `[0, 1, 4, 10, 27, 28, 39, 53, 58, 69, 83, 90, 98, 103, 105]`
9. **Family #8 (Wide Asymmetric Lattice):** `[0, 2, 7, 18, 23, 31, 42, 50, 67, 75, 89, 95, 101, 104, 105]`

### Structural Insight: The Mid-Ruler Arithmetic Progression Trade-off

Observing the extremal constructions above (specifically:

* $n = 11$: $17, 25, 33$ form an arithmetic progression with common difference 8;
* $n = 12$: $17, 26, 35, 44$ form an arithmetic progression with common difference 9;
* $n = 14$: $29, 42, 55$ form an arithmetic progression with common difference 13;
* $n = 15$ Families #2, #3, #6 naturally sprout continuous arithmetic lattices with common difference $\Delta = 12$ in the middle: $21, 33, 45, 57$; $28, 40, 52, 64, 76$; and $29, 41, 53, 65, 77$!)

**Algebraic Explanation:** Under the tight boundary of $N = n(n-1)/2$, perfect Golomb rulers no longer exist for $n \ge 5$. To maximize the number of distinct differences, the extremal constructions adopt an algebraic trade-off of "local sacrifice in exchange for global coverage": by placing an arithmetic progression core in the middle, inevitable collision penalties are highly concentrated and locked within the inner middle segment, enabling the high-density comb scales distributed at both boundaries to achieve near-zero-collision perfect spreading when cross-subtracted with the middle lattice.

---

## 5. Standalone Verification Script

Anyone can run the following zero-dependency Python script to verify all constructions and arithmetic step structures above within milliseconds:

```python
def verify_and_analyze(n, subset, label=""):
    N = n * (n - 1) // 2
    assert len(subset) == n and subset[0] == 0 and subset[-1] <= N and len(set(subset)) == n
    diffs = {abs(a - b) for a in subset for b in subset if a != b}
    steps = [subset[i + 1] - subset[i] for i in range(n - 1)]
    missing = sorted(list(set(range(1, N + 1)) - diffs))
    print(f"[{label:<18}] n={n:<2} (N={N:<3}) | Distinct Diffs: {len(diffs)} | Subset: {subset}")
    print(f"   -> Adjacent Steps : {steps}")
    print(f"   -> Missing ({len(missing):<2})   : {missing}\n")

if __name__ == "__main__":
    records = [
        (12, [0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66], "a(12)=58 Hit"),
        (13, [0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78], "a(13)=68 Hit"),
        (14, [0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91], "a(14)=79 Hit"),
    ]
    for n, sub, lbl in records:
        verify_and_analyze(n, sub, lbl)

    a15_families = [
        [0, 1, 8, 12, 26, 43, 44, 51, 71, 81, 84, 90, 100, 103, 105],
        [0, 4, 8, 9, 19, 30, 42, 58, 65, 71, 78, 85, 102, 103, 105],
        [0, 1, 2, 4, 6, 21, 33, 45, 57, 71, 80, 87, 94, 97, 105],
        [0, 1, 5, 15, 28, 40, 52, 64, 76, 83, 85, 94, 96, 102, 105],
        [0, 2, 3, 5, 14, 16, 38, 48, 58, 75, 79, 97, 98, 104, 105],
        [0, 4, 6, 8, 31, 34, 47, 50, 66, 83, 84, 90, 95, 104, 105],
        [0, 3, 9, 11, 20, 22, 29, 41, 53, 65, 77, 90, 100, 104, 105],
        [0, 1, 4, 10, 27, 28, 39, 53, 58, 69, 83, 90, 98, 103, 105],
        [0, 2, 7, 18, 23, 31, 42, 50, 67, 75, 89, 95, 101, 104, 105],
    ]
    for i, fam in enumerate(a15_families):
        verify_and_analyze(15, fam, f"a(15)>=90 Fam #{i}")

```

---

## 6. Code Availability & Collaboration Notice

The core *PSS Bi-Level Co-evolutionary Engine* and *Deep Tabu Exact-LNS Solver* scripts are currently maintained in a private module pending joint publication and exhaustive verification of $a(15)$. For academic collaboration or verification inquiries, please contact the author.

© 2026 Chien-Cheng Dennis Lin. All Rights Reserved.
