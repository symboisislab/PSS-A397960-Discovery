def _check(cond, msg):
    """Like assert, but cannot be switched off by `python -O`."""
    if not cond:
        raise SystemExit(f"VERIFICATION FAILED: {msg}")

def verify_and_analyze(n, subset, label="", expected=None):
    """expected: the number of distinct differences this subset is CLAIMED to
    attain. Passing it turns this function from a reporter into a verifier --
    without it, a corrupted subset prints a lower count and the script still
    exits 0, which is the opposite of what a verification script is for."""
    m = n * (n - 1) // 2
    _check(len(subset) == n, f"Length mismatch: expected {n}, got {len(subset)}")
    _check(subset[0] == 0 and subset[-1] <= m, f"Out of range [0, {m}]")
    _check(sorted(subset) == subset and len(set(subset)) == n, "Subset must be strictly increasing")
    
    diffs = {abs(a - b) for a in subset for b in subset if a != b}
    steps = [subset[i+1] - subset[i] for i in range(n - 1)]
    missing = sorted(list(set(range(1, m + 1)) - diffs))
    print(f"[{label:<22}] n={n:<2} (m={m:<3}) | Distinct Diffs: {len(diffs)} | Subset: {subset}")
    print(f"   -> Adjacent Steps : {steps}")
    print(f"   -> Missing ({len(missing):<2})   : {missing}\n")
    _check(expected is None or len(diffs) == expected,
        f"{label}: claimed {expected} distinct differences, computed "
        f"{len(diffs)} -- this subset does NOT support the stated bound")
    return tuple(steps)

if __name__ == "__main__":
    print("=== PART 1: Known OEIS Records (n = 9..14) ===")
    records = [
        (9,  [0, 1, 3, 13, 20, 27, 31, 35, 36], "a(9)=32 Witness", 32),
        (10, [0, 1, 7, 11, 15, 24, 40, 42, 43, 45], "a(10)=40 Witness", 40),
        (11, [0, 1, 2, 6, 17, 25, 33, 43, 46, 53, 55], "a(11)=49 Witness", 49),
        (12, [0, 1, 2, 6, 17, 26, 35, 44, 56, 58, 63, 66], "a(12)=58 Witness", 58),
        (13, [0, 1, 2, 12, 13, 29, 33, 48, 55, 64, 70, 73, 78], "a(13)=68 Witness", 68),
        (14, [0, 1, 4, 11, 24, 29, 42, 55, 74, 76, 82, 88, 90, 91], "a(14)=79 Witness", 79),
    ]
    for n, sub, lbl, exp in records:
        verify_and_analyze(n, sub, lbl, exp)

    print("=== PART 2: New Constructive Lower Bound a(15) >= 91 (2 Non-Isomorphic Families) ===")
    a15_91_configs = [
        [0, 3, 4, 13, 29, 40, 51, 62, 73, 85, 90, 97, 103, 104, 105], # Family 91-1 (Delta=11x4)
        [0, 2, 6, 15, 17, 29, 39, 49, 59, 69, 79, 97, 100, 104, 105], # Family 91-2 (Delta=10x5)
    ]
    fams_91 = set()
    for i, cfg in enumerate(a15_91_configs, 1):
        steps = verify_and_analyze(15, cfg, f"a(15)>=91 Family 91-{i}", 91)
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
        steps = verify_and_analyze(15, cfg, f"n=15 90-pt Config #{i}", 90)
        canonical_rep = min(steps, tuple(reversed(steps)))
        if canonical_rep in fams_90:
            print(f"   [Isomorphism Note] Config #{i} is a reflection-symmetric twin (105 - x) of an earlier configuration.\n")
        fams_90.add(canonical_rep)

    print(f"=== Summary: Verified {len(fams_91)} non-isomorphic families for a(15) >= 91, and {len(fams_90)} non-isomorphic families at 90 points. ===")
