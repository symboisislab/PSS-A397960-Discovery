# Project Soul Seed × OEIS A397960: A Constructive Lower Bound a(15) ≥ 91 from LLM-Evolved Heuristics and Human–AI Solver Design

**Authors:** Chien-Cheng Dennis Lin (Symbiosis Lab) and Wujie (Gavin) Gu (author of [OEIS A397960](https://oeis.org/A397960))
**Repository:** [symboisislab/PSS-A397960-Discovery](https://github.com/symboisislab/PSS-A397960-Discovery)
**Target sequence:** [OEIS A397960](https://oeis.org/A397960): a(n) is the maximum number of distinct positive differences of an n-element subset of {0, 1, …, n(n−1)/2} (offset 3; Wujie Gu, Aug 13 2026; approved).
**Dates:** Colab experiments 2026-10-14; independent verification and a(15) ≥ 91 on 2026-10-16.
**README version:** V1.4 (2026-10-16). See the revision log at the end.
**License:** code under the MIT License; data and documentation under CC BY 4.0.

> **Status in one line.** We give two explicit 15-element subsets of {0, …, 105} with 91 distinct positive differences each, so **a(15) ≥ 91** (a constructive lower bound, not a proof of optimality). Both witnesses were independently rescored from scratch by W. Gu in an isolated container.

> **AI use disclosure.** All search code in this repository was written by Google Gemini models, either inside an automated evolution loop (`gemini-3.1-pro-preview`) or in conversations between the first author and Gemini 4 Argon through the Gemini web app (October 2026), with the resulting code run by the first author in Google Colab. The authors ran the code, inspected the results and directed revisions. All reported subsets were verified by independent code. This README was revised with the assistance of Claude (Anthropic) under the authors' Project Soul Seed / Symbiosis Protocol, and was reviewed by the authors before publication.

---

## 1. Summary

The work proceeded in three stages of different character. We report them separately because they support different claims.

| Stage | What happened | Who produced the code | Uses known answers? |
|:--|:--|:--|:--|
| I. Program evolution | An LLM rewrote a scoring heuristic for 4 generations, evaluated on n = 4–8 | Automated loop (`gemini-3.1-pro-preview`) | **Yes**: the feedback to the model included the known optimum for each n |
| II. Solver co-design | Beam search, local search and large-neighbourhood search solvers were written and revised over several rounds | The first author in conversation with Gemini 4 Argon | n = 12–14: known values used as stopping targets. n = 15: no known value exists |
| III. Verification | Every reported subset was rescored by independent code; the a(15) ≥ 91 run was performed by W. Gu in an isolated container | W. Gu, authors | No |

**Main results**
- **a(15) ≥ 91**, with 2 non-isomorphic witnesses (found by the multi-family explorer, Section 7.1, in a 600-second run of 1,052 trials; every emitted configuration was rescored from scratch with zero discrepancies, `bad = 0`).
- 9 configurations with 90 distinct differences at n = 15, forming **8 non-isomorphic families** (one pair are mirror images under x ↦ 105 − x).
- Constructive reproduction of the known values for **n = 4–14**: n = 4–8 by the evolved heuristic, n = 9–11 from scratch, and n = 12–14 by local search started from 1-point-short seeds.
- The Generation-4 program contains a pruning bound that is algebraically equivalent to the bound in the OEIS reference program (confirmed by W. Gu).

---

## 2. Scope and Caveats

1. **Known answers guided Stage I.** The evolution loop reported each candidate's score together with the known optimum (for example, "n=4: 6 points (optimum 6)"), and the generation-0 history included an example optimal subset {0, 1, 4, 6}. The selection pressure was therefore guided by known values. The prompts contained no branch-and-bound code, but they did suggest directions (collision penalties, distance to the boundary, adapting to the number of remaining steps). The Stage I system prompt and user-prompt template are part of the evolution-loop code and will be released in full with the accompanying paper. Selected excerpts of the Stage II conversations will be released as well, and the full transcripts are available from the authors on reasonable request.
2. **Stage I was run once.** We have no distribution over repeated runs, and no ablation of the system prompt.
3. **n = 12–14 were warm starts.** These values were reached from seeds scoring 57, 67 and 78 (one below each record), with the record used as the stopping target, by three different solvers. In an independent test by W. Gu, the vault version of the solver that reached a(14) = 79 was run four times for 30 seconds each, starting from its own built-in multi-family seed pool (not from the 78-point seed); 1 of 4 runs reached 79 (median 78). Success rates depend on the seeds supplied.
4. **A lower bound, not an optimality proof.** a(15) ≤ 91 has not been established. As a heuristic only: the density ratio φ(n) = a(n)/m decreases for n = 11–14 (0.8909, 0.8788, 0.8718, 0.8681), with differences shrinking roughly by half each step, and extrapolating gives φ(15) ≈ 0.866, i.e. about 90.9. This is consistent with 91, but φ is not monotone over all n (it increases from n = 6 to n = 8), so this is not evidence of optimality.

---

## 3. Stage I: Program Evolution

| Setting | Value |
|:--|:--|
| Model | `gemini-3.1-pro-preview`, temperature 0.7 |
| Task | Write `priority_score(candidate, current_subset, n, N)`; the evaluator builds a subset greedily from 0 using this score |
| Training instances | n = 4, 5, 6, 7, 8; fitness = sum of distinct-difference counts |
| Feedback to model | Each n's score and the known optimum |
| Acceptance | A new program replaces the incumbent if its total is ≥ the best so far (ties replace) |
| Known-value table in the script | `{2:1, 3:3, 4:6, 5:9, 6:13, 7:18}` (a(7) was mistyped as 18; the correct value is 19; n = 8 was missing) |
| Evaluator | Python `exec`; this is an evaluator, not a security sandbox |

| Gen | n=4 | n=5 | n=6 | n=7 | n=8 | Total | Structure of the program |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 0 (seed) | 5 | 8 | 13 | 18 | 23 | 67 | Pure greedy: count new differences |
| 1 | 6 | 9 | 13 | 19 | 25 | 72 | Gain, collision penalty, distance from N/2 weighted by remaining steps, minimum distance |
| 2 | 6 | 9 | 13 | 19 | 25 | 72 | Exact 2-step and 3-step lookahead with sorted early termination |
| 3 | 6 | 9 | 13 | 19 | 26 | 73 | Beam-search lookahead with adaptive width |
| 4 | 6 | 9 | 13 | 19 | 26 | 73 | Bitmask representation; budgeted branch-and-bound DFS with an upper-bound prune |

The OEIS values are 6, 9, 13, 19, 26 (total 73). Generation 1 scored 19 at n = 7, exceeding the mistyped reference value of 18. Generation 4 kept the same total as Generation 3 and replaced it under the tie rule.

**Equivalence of the pruning bound.** Generation 4 prunes with `max_poss = curr_score + rem * len(curr_list) + rem * (rem - 1) // 2`. Since `len(curr_list) = n − rem`, this equals rem(n − rem) + rem(rem − 1)/2. With d = n − rem elements placed, this is (n−d)(n−d−1)/2 + d(n−d), the bound in the OEIS PROG. The DFS has a node budget, so it is a truncated branch-and-bound, not an exhaustive search.

---

## 4. Stage II: Solver Co-Design

The solvers below were written by Gemini 4 Argon (Gemini web app) in conversation with the first author, who ran each one in Colab, reported the results, and asked for revisions. They are not outputs of the Stage I loop. The local-search solvers combine the Generation-4 bound with the OEIS bound.

| Step | Solver | Start | Result |
|:--|:--|:--|:--|
| A | Fixed-endpoint beam search + 1-opt hill climbing | From scratch | n = 9, 10, 11 reach 32, 40, 49; n = 12–14 reach 57, 67, 78 (one short); **n = 15 reaches 90 (first occurrence, 5.93 s)** |
| B | Simulated annealing with 1-opt / 2-opt moves | Seeds from A | No improvement at n = 12–15 |
| C | Exact LNS, k = 3–4, right endpoint not fixed | Seeds from A | **a(12) = 58 in 2.20 s** |
| D | Tabu LNS, k = 4–5 | Seeds from A | **a(13) = 68 in 4.42 s** |
| E | Deep LNS, k = 5–6, three removal modes, diverse seed pool | Seeds from A | **a(14) = 79 in 8.31 s** |
| F | Multi-family randomized beam search + exact k = 4 repair | From scratch, no seeds | 45 s: 8 literally distinct 90-point configurations |
| G | Explorer F with reflection-canonical deduplication and a rescoring audit (Section 7.1) | From scratch | **600 s run by W. Gu: a(15) ≥ 91, 2 families, `bad = 0`** |

Simulated annealing and 1-opt moves did not get past the 1-point-short plateaus at n = 12–14. Large-neighbourhood moves that removed 3–6 elements at once (and, for n = 12, freed the right endpoint) did.

---

## 5. Results

### 5.1 Known values, n = 9–14

| n | m | OEIS | Reached | Start | Solver, time | Witness | Steps |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 9 | 36 | 32 | 32 | scratch | A, 0.21 s | `[0, 1, 3, 13, 20, 27, 31, 35, 36]` | `[1, 2, 10, 7, 7, 4, 4, 1]` |
| 10 | 45 | 40 | 40 | scratch | A, 0.32 s | `[0, 1, 7, 11, 15, 24, 40, 42, 43, 45]` | `[1, 6, 4, 4, 9, 16, 2, 1, 2]` |
| 11 | 55 | 49 | 49 | scratch | A, 0.51 s | `[0, 1, 2, 6, 17, 25, 33, 43, 46, 53, 55]` | `[1, 1, 4, 11, 8, 8, 10, 3, 7, 2]` |
| 12 | 66 | 58 | 58 | warm (57) | C, 2.20 s | `[0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66]` | `[1, 1, 4, 11, 9, 9, 9, 12, 2, 5, 3]` |
| 13 | 78 | 68 | 68 | warm (67) | D, 4.42 s | `[0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78]` | `[1, 1, 10, 1, 16, 4, 15, 7, 9, 6, 3, 5]` |
| 14 | 91 | 79 | 79 | warm (78) | E, 8.31 s; 1/4 runs in 30 s from its own seed pool (median 78) | `[0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91]` | `[1, 3, 7, 13, 5, 13, 13, 19, 2, 6, 6, 2, 1]` |

Times are single Colab runs and are machine-dependent.

### 5.2 a(15) ≥ 91

| Family | Witness A (\|A\| = 15, max 105, 91 distinct differences) | Steps | Missing differences (14) |
|:--|:--|:--|:--|
| 91-1 | `[0, 3, 4, 13, 29, 40, 51, 62, 73, 85, 90, 97, 103, 104, 105]` | `[3, 1, 9, 16, 11, 11, 11, 11, 12, 5, 7, 6, 1, 1]` | 21, 55, 66, 67, 71, 78, 79, 80, 83, 88, 89, 95, 96, 98 |
| 91-2 | `[0, 2, 6, 15, 17, 29, 39, 49, 59, 69, 79, 97, 100, 104, 105]` | `[2, 4, 9, 2, 12, 10, 10, 10, 10, 10, 18, 3, 4, 1]` | 16, 19, 60, 70, 72, 74, 78, 81, 84, 86, 92, 93, 96, 101 |

The reflection of 91-1 under x ↦ 105 − x is `[0, 1, 2, 8, 15, 20, 32, 43, 54, 65, 76, 92, 101, 102, 105]`, which differs from 91-2, so the two witnesses are non-isomorphic.

### 5.3 Configurations with 90 distinct differences at n = 15

| Family | Config | Subset | Steps |
|:--|:--|:--|:--|
| A | #0 | `[0, 1, 8, 12, 26, 43, 44, 51, 71, 81, 84, 90, 100, 103, 105]` | `[1, 7, 4, 14, 17, 1, 7, 20, 10, 3, 6, 10, 3, 2]` |
| B | #1 | `[0, 4, 8, 9, 19, 30, 42, 58, 65, 71, 78, 85, 102, 103, 105]` | `[4, 4, 1, 10, 11, 12, 16, 7, 6, 7, 7, 17, 1, 2]` |
| C | #2 | `[0, 1, 2, 4, 6, 21, 33, 45, 57, 71, 80, 87, 94, 97, 105]` | `[1, 1, 2, 2, 15, 12, 12, 12, 14, 9, 7, 7, 3, 8]` |
| D | #3 | `[0, 1, 5, 15, 28, 40, 52, 64, 76, 83, 85, 94, 96, 102, 105]` | `[1, 4, 10, 13, 12, 12, 12, 12, 7, 2, 9, 2, 6, 3]` |
| D (mirror) | #6 | `[0, 3, 9, 11, 20, 22, 29, 41, 53, 65, 77, 90, 100, 104, 105]` | `[3, 6, 2, 9, 2, 7, 12, 12, 12, 12, 13, 10, 4, 1]` |
| E | #4 | `[0, 2, 3, 5, 14, 16, 38, 48, 58, 75, 79, 97, 98, 104, 105]` | `[2, 1, 2, 9, 2, 22, 10, 10, 17, 4, 18, 1, 6, 1]` |
| F | #5 | `[0, 4, 6, 8, 31, 34, 47, 50, 66, 83, 84, 90, 95, 104, 105]` | `[4, 2, 2, 23, 3, 13, 3, 16, 17, 1, 6, 5, 9, 1]` |
| G | #7 | `[0, 1, 4, 10, 27, 28, 39, 53, 58, 69, 83, 90, 98, 103, 105]` | `[1, 3, 6, 17, 1, 11, 14, 5, 11, 14, 7, 8, 5, 2]` |
| H | #8 | `[0, 2, 7, 18, 23, 31, 42, 50, 67, 75, 89, 95, 101, 104, 105]` | `[2, 5, 11, 5, 8, 11, 8, 17, 8, 14, 6, 6, 3, 1]` |

Config #0 came from solver A; #1–#8 from solver F. Solver F deduplicated only identical subsets, which is why the mirror pair #3/#6 appears twice; the reflection check was done afterwards.

### 5.4 Observation: arithmetic runs in the middle

Several high-scoring subsets contain a run of equal steps in the middle: 91-2 has five steps of 10 (`29, 39, 49, 59, 69, 79`), 91-1 has four steps of 11, and the 90-point configurations #3/#6 have four steps of 12.

| Subset | Run (k marks) | Step | Excess collisions in the whole set | Of which forced by the run: C(k,2) − (k−1) | Left for all other pairs | Run's differences appear outside the run? |
|:--|:--|:--|:--|:--|:--|:--|
| 91-2 | 29, 39, 49, 59, 69, 79 (k = 6) | 10 | 14 | 10 | 4 (for 90 pairs) | No |
| 91-1 | 29, 40, 51, 62, 73 (k = 5) | 11 | 14 | 6 | 8 (for 95 pairs) | No |
| 90 #3 | 28, 40, 52, 64, 76 (k = 5) | 12 | 15 | 6 | 9 (for 95 pairs) | No |
| 90 #2 | 21, 33, 45, 57 (k = 4) | 12 | 15 | 3 | 12 (for 99 pairs) | No |

("Excess collisions" = 105 pairs minus the number of distinct differences.)

**How to read this table.** The fifth column is arithmetic, not evidence: an arithmetic run of k marks has C(k,2) pairs but only k − 1 distinct differences, so it always produces C(k,2) − (k−1) repeats, whatever the subset or the step. The last column is a real observation, but largely a forced one: with so little collision budget left (only 4 for the remaining 90 pairs in 91-2), any repeat of a run difference outside the run would lower the score. So the run does not "absorb" collisions; it creates them.

**What is actually surprising is the cost.** In 91-2, 6 of the 15 marks (40%) use up 10 of the 14 allowed collisions (71%), and the set still ties the best known value. Intuitively, high-scoring sets should avoid arithmetic progressions, since they waste differences. That such a run appears in the best sets we found suggests the end marks compensate for this cost. How they do so is an open question, and it can be tested: fix a run of step Δ and length k, search only the ends, and compare against unconstrained search under the same time budget (sweeping Δ = 10–12 and k = 4–6). If the constrained search finds equal or better scores faster, the run is usable structure; if not, it is a by-product of high scores. **This is a hypothesis, not a result.** Only two 91-point witnesses are known. Frequency baselines for such runs in random and high-scoring sets will be reported only after they are recomputed under a rule fixed in advance (e.g. a run of at least 4 marks with three equal steps).

---

## 6. Standalone Verification Script

Run with `python3 -I verify.py`. It checks every subset above, prints steps and missing differences, and counts non-isomorphic families.

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

    print("=== PART 3: 90-Point Configurations for n = 15 (9 Configs, 8 Non-Isomorphic Families) ===")
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
        steps = verify_and_analyze(15, cfg, f"n=15 90-pt Config #{i}")
        canonical_rep = min(steps, tuple(reversed(steps)))
        if canonical_rep in fams_90:
            print(f"   [Isomorphism Note] Config #{i} is a reflection-symmetric twin (105 - x) of an earlier configuration.\n")
        fams_90.add(canonical_rep)

    print(f"=== Summary: Verified {len(fams_91)} non-isomorphic families for a(15) >= 91, and {len(fams_90)} non-isomorphic families at 90 points. ===")
```

---

## 7. Search Code

### 7.1 Multi-family explorer (the code that produced a(15) ≥ 91)

This is the explorer W. Gu ran for 600 seconds (1,052 trials) to obtain the two 91-point witnesses (he added the rescoring counter to the earlier version; it is merged here). It includes reflection-canonical deduplication and a from-scratch rescoring audit (`bad`). Results are random; a single run may or may not reach 91.

```python
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
```

### 7.2 Simplified reference LNS solver

A compact reimplementation of the beam-plus-LNS approach, provided for readers who want a short, self-contained example. **It is not the code that produced the results in Section 5.** Measured with `seed=42`: n = 9 reached 32 in 0.07 s, n = 10 reached 40 in 0.37 s, n = 11 reached 49 in 11.8 s, and n = 12 reached 57 (not 58) within 20 s.

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
    # Measured with seed=42 (see README): n=9..11 reach the OEIS values; n=12 reached 57 (not 58) within 20 s.
    for n_test, target in [(9, 32), (10, 40), (11, 49)]:
        solve_a397960_lns(n_test, target_score=target, time_limit=20.0)
```

---

## 8. Provenance of Each Result

| Result | Produced by | Run by |
|:--|:--|:--|
| Generations 0–4 | Stage I loop, `gemini-3.1-pro-preview` | D. Lin (Colab) |
| n = 9–11, first a(15) = 90 | Solver A | D. Lin (Colab) |
| n = 12 / 13 / 14 | Solvers C / D / E | D. Lin (Colab) |
| 8 non-isomorphic 90-point families | Solvers A and F | D. Lin (Colab) |
| a(15) ≥ 91 (2 families) | Solver G (Section 7.1) | W. Gu (isolated container, `python3 -I`) |
| Equivalence of the pruning bound | Comparison with OEIS PROG | W. Gu |

---

## 9. Citation and License

- Code: MIT License. Data and documentation: CC BY 4.0.
- Please cite the sequence as: Wujie Gu, Sequence A397960, The On-Line Encyclopedia of Integer Sequences, https://oeis.org/A397960.
- When citing this repository, please credit both W. Gu (sequence author; independent verification and the 600 s run establishing a(15) ≥ 91) and C.-C. D. Lin (evolution experiments, solver development and structural analysis).

© 2026 Chien-Cheng Dennis Lin (Symbiosis Lab) and Wujie Gu.

---

## Revision Log

| Version | Date | Changes |
|:--|:--|:--|
| V1.3 | 2026-10-16 | Added a(15) ≥ 91 (2 families) and the four peer-review revisions. |
| V1.4 | 2026-10-16 | Corrected the description to match the original Colab records: (1) the evolution model was `gemini-3.1-pro-preview`, not Gemini 2.5 Flash; (2) removed the claim that failed instances received a 0-point penalty, which was not part of the run; (3) stated that the feedback included known optima and that prompts suggested directions, replacing "blind test" and "autonomously derived"; (4) separated Stage I (evolution) from Stage II (human–AI solver co-design) and attributed each result to the solver that produced it; (5) split the reproduction table into from-scratch (n = 9–11) and warm-start (n = 12–14), and changed "n = 3–14" to "n = 4–14"; (6) replaced the claim that the mid-ruler runs were "confirmed" with a descriptive observation plus a collision table; (7) added the non-monotonicity caveat to the φ extrapolation; (8) relabelled the 90-point tier, since a(15) = 90 is no longer a candidate value; (9) added the exact multi-family explorer that produced a(15) ≥ 91 and labelled the short LNS solver as a reference reimplementation with measured performance; (10) added an AI-use disclosure and a provenance table. |
| V1.4 r2 | 2026-10-16 | Named the model used in the Stage II conversations (Gemini 4 Argon) in the AI-use disclosure, Section 1 and Section 4. |
| V1.4 r3 | 2026-10-16 | Corrected the Stage II setting: the conversations took place in the Gemini web app, not in Colab (Colab was used only to run the code). Specified that the Stage I prompts will be released in full and the Stage II conversations as labelled excerpts, with full transcripts available on request. |
| V1.4 r4 | 2026-10-16 | Following W. Gu's addendum (V1.1): (1) Section 5.4 rewritten. The "collisions inside the run" column is shown as C(k,2) − (k−1), which is determined by the run length, and a "left for all other pairs" column is added. The earlier wording that high-scoring sets "concentrate collisions inside the run" reversed the causality and is replaced by the cost question and a testable experiment. The 0.48% / 5% baselines are removed until they are recomputed under a fixed rule. (2) Section 2 and Table 5.1: the 1-in-4 result for n = 14 was obtained from the solver's own seed pool, not from the 78-point seed. |
