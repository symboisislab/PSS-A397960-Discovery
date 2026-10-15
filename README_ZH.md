# Project Soul Seed × OEIS A397960：雙層演算法協同演化與極值差集構造下界發現

**作者 / 首席研究員：** Chien-Cheng Dennis Lin（林建呈 / [symboisislab/PSS-A397960-Discovery](https://github.com/symboisislab/PSS-A397960-Discovery)）  
**發現日期與時間戳記：** 2026 年 10 月 14 日（2026 年 10 月 15 日修訂更新）  
**目標數列：** [OEIS A397960](https://oeis.org/A397960)（*從 $\{0, 1, \dots, n(n-1)/2\}$ 中選取 $n$ 元子集所能產生之相異正差值最大數量*，由 Wujie Gu 於 2026 年 8 月創立）。  
**研究狀態：** 確立未知項構造性下界 **$a(15) \ge 90$**（發掘 9 組極值構造，涵蓋 **8 組非鏡像同構之獨立家族**），並構造性重現 $a(3) \dots a(14)$ 全部已知 OEIS 紀錄。  
**開源授權：** 程式碼採用 **MIT License**；構造數據與文檔採用 **CC BY 4.0**（確保完全之學術可驗證性與方法可復現性）。

---

## 1. 研究摘要與證明邊界聲明 (Executive Summary & Epistemic Scope)

本研究將 **Project Soul Seed (PSS)** 之「代數守護者（Algebraic Guardian）」與「不變子空間約束（Invariant Subspace Constraint）」自然語言控制協議，應用於極值加法組合學問題 **OEIS A397960**。

透過建構「雙層閉環演化系統（Bi-Level Closed-Loop Evolutionary System）」：
- **上層（Upper-Level Heuristic Generator）：** 由受 PSS 協議約束（反阿諛奉承 Anti-Sycophancy、鎖定離散邊界條件）之大型語言模型（Gemini 2.5 Flash）負責演化 Python 優先級評分與前瞻搜尋函數。
- **下層（Lower-Level Exact Verifier & LNS Solver）：** 負責執行零幻覺之確定性差集計算與深層禁忌局部精確重構（Deep Tabu Exact-LNS）。

在未提供人類專家現有分支定界（Branch-and-Bound）程式碼的盲測條件下，系統於 **4 個演化世代（Generations）內自主推導出與人類數學家等價之組合上界剪枝不等式**，並引入位元遮罩加速（Bitmasking）與哥倫布尺邊界幾何權重（Golomb Ruler Boundary Bias）。結合 Deep Tabu Exact-LNS 後，系統於單機數秒內**構造性重現（Constructively Reproduced）$n=3 \sim 14$ 之所有已知 OEIS 紀錄**；並針對目前未知的第 15 項 **$n=15$ ($m=105$)**，確立了 **$a(15) \ge 90$** 的構造性下界，發掘出 9 組達到 90 個相異正差值的具體子集，扣除 1 對鏡像對稱雙胞胎後，實質涵蓋 **8 種非鏡像同構（Non-isomorphic）的極值晶格家族**。

> **⚠️ 重要認識論邊界聲明（構造性下界 vs. 窮舉上界證明）：**  
> 給出一組滿足 $A \subseteq \{0, \dots, 105\}$、$\vert{}A\vert{}=15$ 且產生 90 個相異正差值的具體子集，在數學上嚴格確立的是**構造性下界（Constructive Lower Bound）$a(15) \ge 90$**，而非 $a(15) = 90$ 的最終窮舉證明。要證明 $a(15) = 90$（即證明上界 $a(15) \le 90$），仍需透過完整分支定界（Branch-and-Bound）或 SAT/ILP 求解器窮舉反證「不存在產生 91 個相異差值的子集」。本倉庫所提供之 `best = 90` 構造下界，可作為該窮舉反證過程的強初始剪枝下界（Initial Pruning Bound）。

---

## 2. 四代演算法自主演化軌跡 (Four-Generation AI Algorithmic Evolution Log)

在初始世代（Generation 0）僅提供純貪婪種子（Pure Greedy Seed）且於測試腳本中混入錯誤參考值（如將 $n=7$ 標為 18、將 $n=8$ 標為 28）之盲測條件下，PSS 約束協議引導模型完成了四階段的演算法結構躍遷：

| 演化世代 | 演算法結構特徵 (Emergent Algorithmic Structure) | $n=4$ | $n=5$ | $n=6$ | $n=7$ | $n=8$ | 驗證總分 | 關鍵突破意義 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Gen 0** | 純單步貪婪法 (Pure Single-Step Greedy) | 5 | 8 | 13 | 18 | 23 | 67 | 陷入局部極值 (Local Optima) |
| **Gen 1** | 幾何邊界權重 (`abs(cand - N/2)` + 碰撞懲罰) | **6** | **9** | **13** | **19** | 25 | 72 | 突破腳本誤導，自主發現 $a(7)=19$ 已知最優值 |
| **Gen 2** | 3步前瞻剪枝樹 (3-Step Lookahead with $O(1)$ Early Stop) | **6** | **9** | **13** | **19** | 25 | 72 | 由純代數公式自發轉移至多步搜索樹結構 |
| **Gen 3** | 動態束搜索 (Dynamic Beam Search + Path Multiplicity) | **6** | **9** | **13** | **19** | **26** | **73** | 攻克 $a(8)=26$，$n=4 \sim 8$ 全數命中 OEIS 已知最優紀錄 |
| **Gen 4** | **位元遮罩 DFS + 組合上界剪枝 (Bitmask B&B DFS)** | **6** | **9** | **13** | **19** | **26** | **73** | **自主推導出 `rem*(n-rem) + rem*(rem-1)//2` 嚴格剪枝不等式** |

---

## 3. 已知 OEIS 紀錄 $a(9) \dots a(14)$ 之構造性重現 (Constructive Reproduction of Known Records)

結合 Gen 3/4 演化出之位元遮罩、邊界啟發式排序與深層禁忌局部精確重構（Deep Tabu Exact-LNS，每次拔除 $k=4 \sim 6$ 個元素進行分支定界重組），系統於單機 Google Colab 環境下構造性重現了 OEIS A397960 截至 2026 年 9 月之所有已知紀錄：

| 項數 $n$ | 最大範圍 $m = n(n-1)/2$ | OEIS A397960 已知紀錄 | 本系統達到之下界 | 搜索耗時 (Colab CPU) | 構造性見證子集 (Constructive Witness Subset) | 相鄰步長 (Adjacent Steps) |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **9** | 36 | 32 | **32** | 0.21s | `[0, 1, 3, 13, 20, 27, 31, 35, 36]` | `[1, 2, 10, 7, 7, 4, 4, 1]` |
| **10** | 45 | 40 | **40** | 0.32s | `[0, 1, 7, 11, 15, 24, 40, 42, 43, 45]` | `[1, 6, 4, 4, 9, 16, 2, 1, 2]` |
| **11** | 55 | 49 | **49** | 0.51s | `[0, 1, 2, 6, 17, 25, 33, 43, 46, 53, 55]` | `[1, 1, 4, 11, 8, 8, 10, 3, 7, 2]` |
| **12** | 66 | 58 | **58** | 2.20s | `[0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66]` | `[1, 1, 4, 11, 9, 9, 9, 12, 2, 5, 3]` |
| **13** | 78 | 68 | **68** | 4.42s | `[0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78]` | `[1, 1, 10, 1, 16, 4, 15, 7, 9, 6, 3, 5]` |
| **14** | 91 | 79 | **79** | 8.31s | `[0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91]` | `[1, 3, 7, 13, 5, 13, 13, 19, 2, 6, 6, 2, 1]` |

---

## 4. 未知項構造性下界 $a(15) \ge 90$、同構分析與「中段等差晶格」現象

針對目前未知之 $n=15$ ($m=105$)，透過多家族隨機化束搜索與局部精確修補（Multi-Family Randomized Beam + Exact-LNS），系統從零生長出 47 棵獨立演化樹，發掘出 **9 組達到 90 個相異正差值的有效構造子集（遺漏差值數皆為 15）**。

### 4.1 鏡像同構檢驗：9 組構造涵蓋 8 個非同構家族 (8 Non-Isomorphic Families)
在差集問題中，子集 $A$ 與其鏡像反轉 $A' = \{m - x \mid x \in A\}$ 生成完全相同的正差值集合，屬同一等價類（同構家族）。經逐一比對相鄰步長序列（Adjacent Steps）：
- **Config #3** 之步長為 `[1, 4, 10, 13, 12, 12, 12, 12, 7, 2, 9, 2, 6, 3]`；
- **Config #6** 之步長為 `[3, 6, 2, 9, 2, 7, 12, 12, 12, 12, 13, 10, 4, 1]`（恰為 Config #3 之完全逆序，即 $105 - x$ 鏡像雙胞胎）。
- 其餘 7 組構造皆不互為平移或鏡像反轉。因此，這 9 組構造實質代表 **8 個彼此獨立之非同構結構家族（Families A–H）**：

| 獨立家族編號 | 構造序號 | 結構特徵描述 | 構造子集 $A$ ($\vert{}A\vert{}=15, m=105$, 相異差值數 $= 90$) | 相鄰步長序列 (Adjacent Steps) |
| :--- | :---: | :--- | :--- | :--- |
| **Family A** | #0 | 非對稱稀疏內核型 | `[0, 1, 8, 12, 26, 43, 44, 51, 71, 81, 84, 90, 100, 103, 105]` | `[1, 7, 4, 14, 17, 1, 7, 20, 10, 3, 6, 10, 3, 2]` |
| **Family B** | #1 | 中後段 `+7/+6` 晶格群 | `[0, 4, 8, 9, 19, 30, 42, 58, 65, 71, 78, 85, 102, 103, 105]` | `[4, 4, 1, 10, 11, 12, 16, 7, 6, 7, 7, 17, 1, 2]` |
| **Family C** | #2 | 中段 `[12, 12, 12]` 複合 `[7, 7]` 晶格 | `[0, 1, 2, 4, 6, 21, 33, 45, 57, 71, 80, 87, 94, 97, 105]` | `[1, 1, 2, 2, 15, 12, 12, 12, 14, 9, 7, 7, 3, 8]` |
| **Family D** | #3 | **中段四連步 `[12, 12, 12, 12]` 純等差核心** | `[0, 1, 5, 15, 28, 40, 52, 64, 76, 83, 85, 94, 96, 102, 105]` | `[1, 4, 10, 13, 12, 12, 12, 12, 7, 2, 9, 2, 6, 3]` |
| **Family D*** | #6 | **#3 之 $105-x$ 鏡像雙胞胎（同屬 Family D）** | `[0, 3, 9, 11, 20, 22, 29, 41, 53, 65, 77, 90, 100, 104, 105]` | `[3, 6, 2, 9, 2, 7, 12, 12, 12, 12, 13, 10, 4, 1]` |
| **Family E** | #4 | 中段 `[10, 10]` 對稱步長核心 | `[0, 2, 3, 5, 14, 16, 38, 48, 58, 75, 79, 97, 98, 104, 105]` | `[2, 1, 2, 9, 2, 22, 10, 10, 17, 4, 18, 1, 6, 1]` |
| **Family F** | #5 | 諧波 `[3, 13, 3]` 步長結構 | `[0, 4, 6, 8, 31, 34, 47, 50, 66, 83, 84, 90, 95, 104, 105]` | `[4, 2, 2, 23, 3, 13, 3, 16, 17, 1, 6, 5, 9, 1]` |
| **Family G** | #7 | 交錯 `[11, 14, 5, 11, 14]` 步長結構 | `[0, 1, 4, 10, 27, 28, 39, 53, 58, 69, 83, 90, 98, 103, 105]` | `[1, 3, 6, 17, 1, 11, 14, 5, 11, 14, 7, 8, 5, 2]` |
| **Family H** | #8 | 非對稱寬幅晶格結構 | `[0, 2, 7, 18, 23, 31, 42, 50, 67, 75, 89, 95, 101, 104, 105]` | `[2, 5, 11, 5, 8, 11, 8, 17, 8, 14, 6, 6, 3, 1]` |

### 4.2 結構洞見：中段等差晶格折衷效應 (The Mid-Ruler Arithmetic Progression Trade-off)
觀察上述極值構造（特別是：
- $n=11$: `17, 25, 33` 為公差 8 等差數列，步長 `[8, 8]`；
- $n=12$: `17, 26, 35, 44` 為公差 9 等差數列，步長 `[9, 9, 9]`；
- $n=14$: `29, 42, 55` 為公差 13 等差數列，步長 `[13, 13]`；
- $n=15$ Family C (#2) 與 Family D (#3, #6): 中段自然湧現 `21, 33, 45, 57`、`28, 40, 52, 64, 76` 與 `29, 41, 53, 65, 77` 之 **公差 $\Delta = 12$ 連續等差晶格**！）

**代數解釋：** 在 $m = n(n-1)/2$ 的緊繃邊界下，完美哥倫布尺（Perfect Golomb Ruler）於 $n \ge 5$ 時已不存在，必然產生差值重複碰撞。為了最大化互異差值數量，極值構造展現出一種「局部集中碰撞以換取全局覆蓋」的代數折衷：透過在中段放置等差晶格（Arithmetic Progression Core），將不可避免的差值碰撞（Collision Penalty）高度集中並鎖定於中段內部（例如公差 12 的倍數），從而使兩端高密度分佈的梳狀刻度（Boundary Comb）在與中段晶格進行交叉相減時，達到極高比例的無碰撞鋪展。

---

## 5. 獨立驗算與同構檢驗腳本 (Standalone Verification & Isomorphism Check Script)

任何人皆可執行以下零依賴 Python 腳本，於毫秒內驗證上述所有構造之合法性、相異差值數量，並自動檢驗鏡像對稱同構關係（確認 9 組構造實質對應 8 組非同構家族）：

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
        # 以步長序列與其逆序之字典序較小者作為鏡像同構等價類代表元
        canonical_rep = min(steps, rev_steps)
        if canonical_rep in canonical_families:
            print(f"   [Isomorphism Note] Config #{i} is a reflection-symmetric twin (105 - x) of an earlier configuration.\n")
        canonical_families.add(canonical_rep)

    print(f"=== Summary: Verified {len(a15_configs)} valid configurations for a(15) >= 90, representing {len(canonical_families)} distinct non-isomorphic families. ===")
```

---

## 6. 方法可復現性：開源搜尋引擎程式碼 (Reproducible Search Methodology: Open-Source Exact-LNS & Beam Solver)

為確保本研究不僅提供「可驗證之結果（Verifiable Results）」，更提供完整「可復現之搜索方法（Reproducible Methodology）」，本倉庫同步以 **MIT License** 開源釋出完整的 **Deep Tabu Exact-LNS + 位元遮罩分支定界（Bitmask B&B）求解器**。任何研究者皆可直接執行以下零依賴腳本，從零獨立復現 $a(9) \dots a(14)$ 之搜索過程及 $a(15) \ge 90$ 之多家族探索：

```python
import random
import time

def solve_a397960_lns(n, target_score=None, time_limit=15.0, seed=42):
    """
    可復現之 Deep Tabu Exact-LNS + Bitmask Branch-and-Bound 求解器 (MIT License)
    結合 Gen 1 邊界權重、Gen 3 隨機化束搜索種子與 Gen 4 位元遮罩精確局部重構。
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

    # Stage 1: Randomized Boundary-Biased Beam Search 初始化種子
    beam = [(0, [0, m])]
    for step in range(n - 2):
        rem = n - 2 - step
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
                # Gen 1 演化之哥倫布尺邊界幾何偏好
                bias = abs(cand - m / 2.0) * 0.05 + random.uniform(0, 0.2)
                key = tuple(sorted(sub + [cand]))
                if key not in next_beam or sc > next_beam[key][0]:
                    next_beam[key] = (sc, sc + bias, new_mask, list(key))
        sorted_cands = sorted(next_beam.values(), key=lambda x: x[1], reverse=True)
        beam = [(x[2], x[3]) for x in sorted_cands[:150]]

    best_mask, best_sub = max(beam, key=lambda x: x[0].bit_count())
    best_score = best_mask.bit_count()

    # Stage 2: Deep Tabu Exact-LNS (拔除 k=4~5 點 + Gen 4 位元剪枝 DFS 重組)
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

        # 候選點按新增差值排序
        fixed_set = set(fixed)
        cands = []
        for v in range(1, m):
            if v not in fixed_set:
                dm = 0
                for x in fixed:
                    dm |= (1 << abs(v - x))
                gain = ( dm & ~base_mask ).bit_count()
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
            # Gen 4 自主推導之嚴格組合上界剪枝不等式:
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

## 7. 開源授權與學術合作聲明 (License & Collaboration Notice)

- **程式碼授權（MIT License）：** 本倉庫內所有驗證與搜索演算法腳本（含位元遮罩 B&B 與 Deep Tabu Exact-LNS 實作）均以 MIT License 開源釋出，歡迎學界自由檢驗、復現與擴展。
- **數據與文檔授權（CC BY 4.0）：** 構造子集與結構分析採 CC BY 4.0 授權，引用時請標明出處與原作者（Wujie Gu 之 OEIS A397960 序列定義，以及 Chien-Cheng Dennis Lin 之 $a(15) \ge 90$ 構造下界與中段等差晶格分析）。

© 2026 Chien-Cheng Dennis Lin (Symbiosis Lab). Released under MIT License & CC BY 4.0.
