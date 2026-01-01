def selection_sort(arr):
    steps = []
    comparisons = swaps = 0
    a = arr.copy()

    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            comparisons += 1
            steps.append({
                "array": a.copy(),
                "compare": [min_idx, j],
                "swap": False
            })

            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
            steps.append({
                "array": a.copy(),
                "compare": [i, min_idx],
                "swap": True
            })

    return {"steps": steps, "stats": {"comparisons": comparisons, "swaps": swaps}}

