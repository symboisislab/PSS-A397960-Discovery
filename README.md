# Project Soul Seed × OEIS A397960: Bi-Level Algorithmic Co-evolution & Extremal Lattice Discovery

**Author / Lead Researcher:** [Chien-Cheng Dennis Lin / [symboisislab/PSS-A397960-Discovery] ]
**Date of Discovery & Timestamp:** October 14, 2026  
**Target Sequence:** [OEIS A397960](https://oeis.org/A397960) (*Maximum number of distinct positive differences of an $n$-element subset of $\{0, 1, \dots, n(n-1)/2\}$*, originally authored by Wujie Gu, Aug 2026).  
**Status:** Constructive Lower Bound **$a(15) \ge 90$** Established (9 Non-isomorphic Families Discovered) & Exact Reproduction of $a(3) \dots a(14)$.

---

## 1. Executive Summary (研究摘要)

本研究將 **Project Soul Seed (PSS)** 之「代數守護者（Algebraic Guardian）」與「不變子空間約束（Invariant Subspace Constraint）」本體論協議，應用於極限加法組合學難題 **OEIS A397960**。

透過建構「雙層閉環演化系統（Bi-Level Closed-Loop Evolutionary System）」：
- **上層（Upper-Level Heuristic Generator）：** 由受 PSS 協議嚴格約束（反阿諛奉承 Anti-Sycophancy、鎖定離散邊界條件）之大型語言模型（Gemini 2.5 Flash）負責演化 Python 優先級評分與前瞻函數。
- **下層（Lower-Level Exact Verifier & LNS Solver）：** 負責執行無幻覺之精確差集驗證與大規模鄰域禁忌重構（Deep Tabu Exact-LNS）。

在完全未提供人類專家現有分支定界（Branch-and-Bound）程式碼的盲測條件下，系統於 **4 個演化世代（Generations）內自主重新推導出與人類數學家等價之理論上界剪枝不等式**，並自動引入位元遮罩加速（Bitmasking）與哥倫布尺邊界效應（Golomb Ruler Boundary Bias）。最終系統不僅於數秒內 **100% 精確重現 $n=3 \sim 14$ 之所有已知世界紀錄**，更針對尚未被窮舉攻克的未知項 **$n=15$ ($N=105$)**，成功確立 **$a(15) \ge 90$** 之強健下界，並發掘出 **9 組結構完全獨立（非鏡像同構）的 90 分極值晶格家族**。

---

## 2. Four-Generation AI Algorithmic Evolution Log (四代演算法自主演化軌跡)

在初始世代（Generation 0）僅提供純貪婪種子（Pure Greedy Seed）且故意給予錯誤參考上界（如將 $n=7$ 標為 18、將 $n=8$ 標為 28）之壓力測試下，PSS 約束協議引導模型展現了四階段的演算法典範轉移：

| 演化世代 | 演算法結構特徵 (Emergent Algorithmic Structure) | $n=4$ | $n=5$ | $n=6$ | $n=7$ | $n=8$ | 驗證總分 | 關鍵突破意義 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gen 0** | 純貪婪法 (Pure Single-Step Greedy) | 5 | 8 | 13 | 18 | 23 | 67 | 陷入局部極值 (Local Optima) |
| **Gen 1** | 幾何邊界權重 (`abs(cand - N/2)` + 碰撞懲罰) | **6** | **9** | **13** | **19** | 25 | 72 | 突破腳本誤導，自動發現 $a(7)=19$ 真實極值 |
| **Gen 2** | 3步精確前瞻剪枝樹 (3-Step Lookahead with $O(1)$ Pruning) | **6** | **9** | **13** | **19** | 25 | 72 | 由純代數公式自發轉移至多步搜索樹結構 |
| **Gen 3** | 動態束搜索 (Dynamic Beam Search + Path Multiplicity) | **6** | **9** | **13** | **19** | **26** | **73** | 攻克 $a(8)=26$，$n=4 \sim 8$ 全數達至數學絕對上限 |
| **Gen 4** | **位元遮罩 DFS + 嚴格組合上界剪枝 (Bitmask B&B DFS)** | **6** | **9** | **13** | **19** | **26** | **73** | **自主推導出 `rem*(n-rem) + rem*(rem-1)//2` 剪枝公式** |

---

## 3. Exact Reproduction of World Records $a(9) \dots a(14)$ (已知極限紀錄之重現)

結合 Gen 3/4 演化出之位元遮罩、邊界啟發式排序與深層禁忌局部精確重構（Deep Tabu Exact-LNS，每次拔除 $k=4 \sim 6$ 個元素進行分支定界重組），系統於單機 Google Colab 環境下極速重現了 OEIS A397960 截至 2026 年 9 月之所有已知極值：

| 項數 $n$ | 最大範圍 $N$ | OEIS A397960 已知紀錄 | 本系統實測結果 | 破局耗時 | 代表性極值構造子集 (Constructive Proof Subset) |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **9** | 36 | 32 | **32** (Hit) | 0.21s | `[0, 1, 3, 13, 20, 27, 31, 35, 36]` |
| **10** | 45 | 40 | **40** (Hit) | 0.32s | `[0, 1, 7, 11, 15, 24, 40, 42, 43, 45]` |
| **11** | 55 | 49 | **49** (Hit) | 0.51s | `[0, 1, 2, 6, 17, 25, 33, 43, 46, 53, 55]` |
| **12** | 66 | 58 | **58** (Hit) | 2.20s | `[0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66]` |
| **13** | 78 | 68 | **68** (Hit) | 4.42s | `[0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78]` |
| **14** | 91 | 79 | **79** (Hit) | 8.31s | `[0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91]` |

---

## 4. Major Discovery: $a(15) \ge 90$ and the "Arithmetic Progression Core" Phenomenon (未知項 $a(15)$ 之突破與中段等差晶格定理雛形)

針對尚未被窮舉證明之 $n=15$ ($N=105$)，透過多家族隨機化束搜索與局部精確修補（Multi-Family Randomized Beam + Exact-LNS），系統從零生長出 47 棵獨立演化樹，最終全數收斂於 **`90`** 分之極限天花板，並發掘出 **9 種完全獨立（非平移或鏡像同構）的 $a(15)=90$ 極值構造家族**：

1. **Family #0 (Isolated Rigid Seed):** `[0, 1, 8, 12, 26, 43, 44, 51, 71, 81, 84, 90, 100, 103, 105]`
2. **Family #1 (Period-7/6 Lattice):** `[0, 4, 8, 9, 19, 30, 42, 58, 65, 71, 78, 85, 102, 103, 105]`
3. **Family #2 (Period-12 & Period-7 Hybrid Lattice):** `[0, 1, 2, 4, 6, 21, 33, 45, 57, 71, 80, 87, 94, 97, 105]`
4. **Family #3 (Pure 5-Term Period-12 Arithmetic Core):** `[0, 1, 5, 15, 28, 40, 52, 64, 76, 83, 85, 94, 96, 102, 105]`
5. **Family #4 (Symmetric Step-10 Core):** `[0, 2, 3, 5, 14, 16, 38, 48, 58, 75, 79, 97, 98, 104, 105]`
6. **Family #5 (Harmonic [3, 13, 3] Lattice):** `[0, 4, 6, 8, 31, 34, 47, 50, 66, 83, 84, 90, 95, 104, 105]`
7. **Family #6 (Shifted 5-Term Period-12 Arithmetic Core):** `[0, 3, 9, 11, 20, 22, 29, 41, 53, 65, 77, 90, 100, 104, 105]`
8. **Family #7 (Alternating Step Lattice):** `[0, 1, 4, 10, 27, 28, 39, 53, 58, 69, 83, 90, 98, 103, 105]`
9. **Family #8 (Wide Asymmetric Lattice):** `[0, 2, 7, 18, 23, 31, 42, 50, 67, 75, 89, 95, 101, 104, 105]`

### 結構洞見：中段等差晶格效應 (The Mid-Ruler Arithmetic Progression Trade-off)
觀察上述極值構造（特別是：
- $n=11$: `17, 25, 33` 為公差 8 等差數列；
- $n=12$: `17, 26, 35, 44` 為公差 9 等差數列；
- $n=14$: `29, 42, 55` 為公差 13 等差數列；
- $n=15$ Family #2, #3, #6: 中段自然湧現 `21, 33, 45, 57`、`28, 40, 52, 64, 76` 與 `29, 41, 53, 65, 77` 之 **公差 $\Delta = 12$ 連續等差晶格**！）

**代數解釋：** 在 $N = n(n-1)/2$ 的緊繃邊界下，完美哥倫布尺（Perfect Golomb Ruler）於 $n \ge 5$ 時已不存在。為了最大化互異差值數量，極值構造採取了一種「局部犧牲換取全局覆蓋」的代數折衷：透過在中段放置等差晶格（Arithmetic Progression Core），將不可避免的差值碰撞（Collision Penalty）高度集中並鎖定於中段內部，從而使兩端高密度分佈的梳狀刻度（Boundary Comb）在與中段晶格進行交叉相減時，達到近乎零碰撞的完美鋪展。

---

## 5. Standalone Verification Script (獨立驗算腳本)

任何人皆可執行以下零依賴 Python 腳本，於毫秒內驗證上述所有構造與等差步長結構：

```python
def verify_and_analyze(n, subset, label=""):
    N = n * (n - 1) // 2
    assert len(subset) == n and subset[0] == 0 and subset[-1] <= N and len(set(subset)) == n
    diffs = {abs(a - b) for a in subset for b in subset if a != b}
    steps = [subset[i+1] - subset[i] for i in range(n - 1)]
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

The core **PSS Bi-Level Co-evolutionary Engine** and **Deep Tabu Exact-LNS Solver** scripts are currently maintained in a private module pending joint publication and exhaustive verification of $a(15)$. For academic collaboration or verification inquiries, please contact the author.

© 2026 [Chien-Cheng Dennis Lin]. All Rights Reserved.
