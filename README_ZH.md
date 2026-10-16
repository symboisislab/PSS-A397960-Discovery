# Project Soul Seed × OEIS A397960：以 LLM 演化啟發式與人機協作求解器取得構造性下界 a(15) ≥ 91

**作者：** 林建誠 Chien-Cheng Dennis Lin（Symbiosis Lab）、Wujie (Gavin) Gu（[OEIS A397960](https://oeis.org/A397960) 數列作者）
**倉庫：** [symboisislab/PSS-A397960-Discovery](https://github.com/symboisislab/PSS-A397960-Discovery)
**目標數列：** [OEIS A397960](https://oeis.org/A397960)：a(n) 為 {0, 1, …, n(n−1)/2} 的 n 元子集所能擁有的相異正差值最大個數（offset 3；Wujie Gu 於 2026-08-13 登錄，已核可）。
**日期：** Colab 實驗 2026-10-14；獨立驗證與 a(15) ≥ 91 於 2026-10-16。
**README 版次：** V1.4（2026-10-16），版次紀錄見文末。
**授權：** 程式碼採 MIT License；數據與文件採 CC BY 4.0。

> **一句話現況：** 我們給出兩個 {0, …, 105} 的 15 元子集，各自有 91 個相異正差值，因此 **a(15) ≥ 91**（構造性下界，不是最佳性證明）。兩組見證都經 W. Gu 在隔離容器中從頭獨立重算。

> **AI 使用聲明：** 本倉庫所有搜尋程式碼皆由 Google Gemini 模型撰寫：一部分出自自動演化迴圈（`gemini-3.1-pro-preview`），一部分出自第一作者在 Google Colab 中與 Gemini 的對話（確切模型版本待確認）。作者負責執行程式、檢查結果並主導修改方向。所有列出的子集都經獨立程式驗證。

---

## 1. 摘要

研究過程分為三個性質不同的階段，因為它們支持的主張不同，所以分開陳述。

| 階段 | 內容 | 程式碼產出者 | 是否使用已知答案 |
|:--|:--|:--|:--|
| 一、程式演化 | LLM 改寫評分啟發式 4 代，在 n = 4–8 評估 | 自動迴圈（`gemini-3.1-pro-preview`） | **是**：回饋給模型的內容包含每個 n 的已知最佳值 |
| 二、求解器協作設計 | 束搜索、局部搜尋與大鄰域搜尋求解器，經多輪撰寫與修改 | 第一作者與 Gemini 對話 | n = 12–14：以已知值作為停止目標；n = 15：沒有已知值 |
| 三、驗證 | 所有子集以獨立程式重算；a(15) ≥ 91 的執行由 W. Gu 在隔離容器完成 | W. Gu、作者 | 否 |

**主要結果**
- **a(15) ≥ 91**，有 2 組非同構見證（由第 7.1 節的多家族探索器在 600 秒、1,052 次 trial 中取得；每組輸出的配置都從頭重算，零差異，`bad = 0`）。
- n = 15 有 9 組達到 90 個相異差值的配置，構成 **8 個非同構家族**（其中一對在 x ↦ 105 − x 下互為鏡像）。
- 構造性重現 **n = 4–14** 的已知值：n = 4–8 由演化出的啟發式達成，n = 9–11 從零達成，n = 12–14 由局部搜尋從差 1 分的種子補足。
- 第 4 代程式中的剪枝上界，與 OEIS 參考程式的剪枝式在代數上等價（W. Gu 確認）。

---

## 2. 範圍與限制

1. **第一階段受已知答案引導。** 演化迴圈回報每個候選程式的得分時，會一併附上已知最佳值（例如「n=4 得 6 分（最佳 6）」），第 0 代的歷史紀錄還附了一個最佳子集範例 {0, 1, 4, 6}。因此選擇壓力受已知值引導。提示詞中沒有任何分支定界程式碼，但有建議方向（碰撞懲罰、與邊界的距離、依剩餘步數調整）。完整提示詞存於私人庫，將隨論文一併公開。
2. **第一階段只執行了一次。** 沒有多次執行的分布，也沒有系統提示的消融實驗。
3. **n = 12–14 是暖啟動。** 這三個值是從 57、67、78 分（各比紀錄少 1 分）的種子出發，以紀錄為停止目標，由三支不同的求解器補足。在獨立測試中，達成 a(14) = 79 的求解器在 30 秒的 4 次執行中有 1 次成功（中位數 78）。
4. **這是下界，不是最佳性證明。** a(15) ≤ 91 尚未證明。僅作為啟發式參考：密度比 φ(n) = a(n)/m 在 n = 11–14 依序為 0.8909、0.8788、0.8718、0.8681，遞減量大約逐步減半，外推得 φ(15) ≈ 0.866，即約 90.9。這與 91 一致；但 φ 並非對所有 n 單調（n = 6 到 8 是上升的），所以不構成最佳性的證據。

---

## 3. 第一階段：程式演化

| 設定 | 值 |
|:--|:--|
| 模型 | `gemini-3.1-pro-preview`，temperature 0.7 |
| 任務 | 撰寫 `priority_score(candidate, current_subset, n, N)`；評估器從 0 開始以此分數貪婪地挑選元素 |
| 訓練實例 | n = 4、5、6、7、8；適應度 = 五個 n 的相異差值數總和 |
| 回饋給模型 | 每個 n 的得分與已知最佳值 |
| 接受規則 | 新程式總分 ≥ 歷史最高即替換（同分也替換） |
| 腳本中的已知值表 | `{2:1, 3:3, 4:6, 5:9, 6:13, 7:18}`（a(7) 誤植為 18，正確為 19；缺 n = 8） |
| 評估器 | Python `exec`；這是評估器，不是安全沙盒 |

| 代 | n=4 | n=5 | n=6 | n=7 | n=8 | 總分 | 程式結構 |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 0（種子） | 5 | 8 | 13 | 18 | 23 | 67 | 純貪婪：只計算新增差值 |
| 1 | 6 | 9 | 13 | 19 | 25 | 72 | 增益、碰撞懲罰、與 N/2 的距離（依剩餘步數加權）、最小距離 |
| 2 | 6 | 9 | 13 | 19 | 25 | 72 | 2 步與 3 步精確前瞻，含排序後的提前終止 |
| 3 | 6 | 9 | 13 | 19 | 26 | 73 | 寬度自適應的束搜索前瞻 |
| 4 | 6 | 9 | 13 | 19 | 26 | 73 | 位元遮罩表示；有節點預算、含上界剪枝的分支定界 DFS |

OEIS 值為 6、9、13、19、26（總和 73）。第 1 代在 n = 7 得到 19，超過了誤植的參照值 18。第 4 代與第 3 代總分相同，依同分替換規則取代第 3 代。

**剪枝上界的等價性：** 第 4 代以 `max_poss = curr_score + rem * len(curr_list) + rem * (rem - 1) // 2` 剪枝。由於 `len(curr_list) = n − rem`，此式等於 rem(n − rem) + rem(rem − 1)/2。令已放置 d = n − rem 個元素，即為 OEIS PROG 中的 (n−d)(n−d−1)/2 + d(n−d)。該 DFS 有節點預算，因此是截斷的分支定界，不是完整窮舉。

---

## 4. 第二階段：求解器協作設計

以下求解器由 Gemini 在與第一作者的對話中撰寫；第一作者在 Colab 執行、回報結果並要求修改。它們不是第一階段迴圈的輸出。局部搜尋求解器同時使用了第 4 代的剪枝界與 OEIS 的剪枝界。

| 步驟 | 求解器 | 起點 | 結果 |
|:--|:--|:--|:--|
| A | 固定端點束搜索 + 1-opt 爬山 | 從零 | n = 9、10、11 達到 32、40、49；n = 12–14 達到 57、67、78（各差 1）；**n = 15 達到 90（首次出現，5.93 秒）** |
| B | 模擬退火，1-opt／2-opt 移動 | A 的種子 | n = 12–15 皆無改善 |
| C | Exact LNS，k = 3–4，不固定右端點 | A 的種子 | **a(12) = 58，2.20 秒** |
| D | 禁忌 LNS，k = 4–5 | A 的種子 | **a(13) = 68，4.42 秒** |
| E | 深層 LNS，k = 5–6，三種拔除模式，多樣化種子池 | A 的種子 | **a(14) = 79，8.31 秒** |
| F | 多家族隨機化束搜索 + k = 4 精確修補 | 從零，不用種子 | 45 秒：8 個字面不同的 90 分配置 |
| G | F 加上鏡像正規化去重與重算稽核（第 7.1 節） | 從零 | **W. Gu 執行 600 秒：a(15) ≥ 91，2 個家族，`bad = 0`** |

模擬退火與 1-opt 移動無法越過 n = 12–14 的「差 1 分」高原；一次拔除 3–6 個元素的大鄰域移動（n = 12 時並解除右端點的固定）才能越過。

---

## 5. 結果

### 5.1 已知值 n = 9–14

| n | m | OEIS | 達成 | 起點 | 求解器、時間 | 見證 | 步長 |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 9 | 36 | 32 | 32 | 從零 | A，0.21 秒 | `[0, 1, 3, 13, 20, 27, 31, 35, 36]` | `[1, 2, 10, 7, 7, 4, 4, 1]` |
| 10 | 45 | 40 | 40 | 從零 | A，0.32 秒 | `[0, 1, 7, 11, 15, 24, 40, 42, 43, 45]` | `[1, 6, 4, 4, 9, 16, 2, 1, 2]` |
| 11 | 55 | 49 | 49 | 從零 | A，0.51 秒 | `[0, 1, 2, 6, 17, 25, 33, 43, 46, 53, 55]` | `[1, 1, 4, 11, 8, 8, 10, 3, 7, 2]` |
| 12 | 66 | 58 | 58 | 暖啟動（57） | C，2.20 秒 | `[0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66]` | `[1, 1, 4, 11, 9, 9, 9, 12, 2, 5, 3]` |
| 13 | 78 | 68 | 68 | 暖啟動（67） | D，4.42 秒 | `[0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78]` | `[1, 1, 10, 1, 16, 4, 15, 7, 9, 6, 3, 5]` |
| 14 | 91 | 79 | 79 | 暖啟動（78） | E，8.31 秒；30 秒 4 次中 1 次成功（中位數 78） | `[0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91]` | `[1, 3, 7, 13, 5, 13, 13, 19, 2, 6, 6, 2, 1]` |

時間為 Colab 單次執行，會因機器而異。

### 5.2 a(15) ≥ 91

| 家族 | 見證 A（\|A\| = 15，最大 105，91 個相異差值） | 步長 | 遺漏差值（14 個） |
|:--|:--|:--|:--|
| 91-1 | `[0, 3, 4, 13, 29, 40, 51, 62, 73, 85, 90, 97, 103, 104, 105]` | `[3, 1, 9, 16, 11, 11, 11, 11, 12, 5, 7, 6, 1, 1]` | 21, 55, 66, 67, 71, 78, 79, 80, 83, 88, 89, 95, 96, 98 |
| 91-2 | `[0, 2, 6, 15, 17, 29, 39, 49, 59, 69, 79, 97, 100, 104, 105]` | `[2, 4, 9, 2, 12, 10, 10, 10, 10, 10, 18, 3, 4, 1]` | 16, 19, 60, 70, 72, 74, 78, 81, 84, 86, 92, 93, 96, 101 |

91-1 在 x ↦ 105 − x 下的反射為 `[0, 1, 2, 8, 15, 20, 32, 43, 54, 65, 76, 92, 101, 102, 105]`，與 91-2 不同，因此兩組見證互非同構。

### 5.3 n = 15 達到 90 個相異差值的配置

| 家族 | 配置 | 子集 | 步長 |
|:--|:--|:--|:--|
| A | #0 | `[0, 1, 8, 12, 26, 43, 44, 51, 71, 81, 84, 90, 100, 103, 105]` | `[1, 7, 4, 14, 17, 1, 7, 20, 10, 3, 6, 10, 3, 2]` |
| B | #1 | `[0, 4, 8, 9, 19, 30, 42, 58, 65, 71, 78, 85, 102, 103, 105]` | `[4, 4, 1, 10, 11, 12, 16, 7, 6, 7, 7, 17, 1, 2]` |
| C | #2 | `[0, 1, 2, 4, 6, 21, 33, 45, 57, 71, 80, 87, 94, 97, 105]` | `[1, 1, 2, 2, 15, 12, 12, 12, 14, 9, 7, 7, 3, 8]` |
| D | #3 | `[0, 1, 5, 15, 28, 40, 52, 64, 76, 83, 85, 94, 96, 102, 105]` | `[1, 4, 10, 13, 12, 12, 12, 12, 7, 2, 9, 2, 6, 3]` |
| D（鏡像） | #6 | `[0, 3, 9, 11, 20, 22, 29, 41, 53, 65, 77, 90, 100, 104, 105]` | `[3, 6, 2, 9, 2, 7, 12, 12, 12, 12, 13, 10, 4, 1]` |
| E | #4 | `[0, 2, 3, 5, 14, 16, 38, 48, 58, 75, 79, 97, 98, 104, 105]` | `[2, 1, 2, 9, 2, 22, 10, 10, 17, 4, 18, 1, 6, 1]` |
| F | #5 | `[0, 4, 6, 8, 31, 34, 47, 50, 66, 83, 84, 90, 95, 104, 105]` | `[4, 2, 2, 23, 3, 13, 3, 16, 17, 1, 6, 5, 9, 1]` |
| G | #7 | `[0, 1, 4, 10, 27, 28, 39, 53, 58, 69, 83, 90, 98, 103, 105]` | `[1, 3, 6, 17, 1, 11, 14, 5, 11, 14, 7, 8, 5, 2]` |
| H | #8 | `[0, 2, 7, 18, 23, 31, 42, 50, 67, 75, 89, 95, 101, 104, 105]` | `[2, 5, 11, 5, 8, 11, 8, 17, 8, 14, 6, 6, 3, 1]` |

#0 來自求解器 A；#1–#8 來自求解器 F。F 只去除完全相同的子集，所以鏡像對 #3／#6 會各出現一次；鏡像檢驗是事後完成的。

### 5.4 觀察：中段的等差段

數個高分子集的中段有一段相同的步長：91-2 有連續 5 步的 10（`29, 39, 49, 59, 69, 79`），91-1 有連續 4 步的 11，90 分配置 #3／#6 有連續 4 步的 12。在這些子集中，等差段產生的重複差值，只由等差段內部的點對產生：

| 子集 | 等差段 | 公差 | 全集合的多餘碰撞 | 等差段內部的碰撞 | 等差段的差值是否出現在段外 |
|:--|:--|:--|:--|:--|:--|
| 91-2 | 29, 39, 49, 59, 69, 79 | 10 | 14 | 10 | 否 |
| 91-1 | 29, 40, 51, 62, 73 | 11 | 14 | 6 | 否 |
| 90 #3 | 28, 40, 52, 64, 76 | 12 | 15 | 6 | 否 |
| 90 #2 | 21, 33, 45, 57 | 12 | 15 | 3 | 否 |

（「多餘碰撞」＝ 105 個點對減去相異差值數。）

這提示一個假說：高分子集可能把一部分不可避免的碰撞集中在中段的等差段內。**這是描述性觀察，不是已確立的結構定律。** 作為比較，W. Gu 估計此類等差段在隨機子集中約佔 0.48%，在高分局部最佳解中約佔 5%；91 分的見證目前只有兩組，因此不做統計主張。

---

## 6. 獨立驗算腳本

以 `python3 -I verify.py` 執行。腳本會檢查上述所有子集，印出步長與遺漏差值，並計算非同構家族數。

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

## 7. 搜尋程式碼

### 7.1 多家族探索器（產生 a(15) ≥ 91 的程式）

這是 W. Gu 執行 600 秒（1,052 次 trial）取得兩組 91 分見證的探索器（重算計數器由他加入前一版，此處已併入），內含鏡像正規化去重與從頭重算的稽核計數器（`bad`）。結果具隨機性，單次執行不一定能達到 91。

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

### 7.2 簡化版參考 LNS 求解器

束搜索加 LNS 方法的精簡重寫版，提供給想看簡短、獨立範例的讀者。**它不是產生第 5 節結果的程式。** 以 `seed=42` 實測：n = 9 於 0.07 秒達到 32，n = 10 於 0.37 秒達到 40，n = 11 於 11.8 秒達到 49，n = 12 在 20 秒內達到 57（未達 58）。

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

## 8. 各結果的出處

| 結果 | 產出者 | 執行者 |
|:--|:--|:--|
| 第 0–4 代 | 第一階段迴圈，`gemini-3.1-pro-preview` | 林建誠（Colab） |
| n = 9–11、首次 a(15) = 90 | 求解器 A | 林建誠（Colab） |
| n = 12／13／14 | 求解器 C／D／E | 林建誠（Colab） |
| 8 個非同構 90 分家族 | 求解器 A 與 F | 林建誠（Colab） |
| a(15) ≥ 91（2 個家族） | 求解器 G（第 7.1 節） | W. Gu（隔離容器，`python3 -I`） |
| 剪枝上界等價 | 與 OEIS PROG 比對 | W. Gu |

---

## 9. 引用與授權

- 程式碼：MIT License。數據與文件：CC BY 4.0。
- 引用數列請用：Wujie Gu, Sequence A397960, The On-Line Encyclopedia of Integer Sequences, https://oeis.org/A397960。
- 引用本倉庫時，請同時標明 W. Gu（數列作者；獨立驗證與確立 a(15) ≥ 91 的 600 秒執行）與林建誠（演化實驗、求解器開發與結構分析）。

© 2026 Chien-Cheng Dennis Lin (Symbiosis Lab) and Wujie Gu.

---

## 版次紀錄

| 版次 | 日期 | 變更 |
|:--|:--|:--|
| V1.3 | 2026-10-16 | 加入 a(15) ≥ 91（2 個家族）與四項同行評審修正。 |
| V1.4 | 2026-10-16 | 依 Colab 原始紀錄更正描述：(1) 演化模型為 `gemini-3.1-pro-preview`，非 Gemini 2.5 Flash；(2) 刪除「失敗實例判 0 分罰分」，該機制不在實際執行中；(3) 說明回饋包含已知最佳值、提示詞含建議方向，取代「盲測」與「自主推導」；(4) 區分第一階段（演化）與第二階段（人機協作設計求解器），並將每項結果歸屬到實際產生它的求解器；(5) 重現表拆分為從零（n = 9–11）與暖啟動（n = 12–14），並將「n = 3–14」改為「n = 4–14」；(6) 將等差段「證實」的說法改為描述性觀察並附碰撞表；(7) φ 外推補上非單調的限制；(8) 90 分層級改名，因 a(15) = 90 已不可能；(9) 加入實際產生 a(15) ≥ 91 的多家族探索器，並將簡短 LNS 求解器標示為參考重寫版且附實測表現；(10) 新增 AI 使用聲明與結果出處表。 |
