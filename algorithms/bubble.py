def bubble_sort(arr):
    steps = []
    comparisons = swaps = 0
    a = arr.copy()

    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            steps.append({
                "array": a.copy(),
                "compare": [j, j + 1],
                "swap": False
            })

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                steps.append({
                    "array": a.copy(),
                    "compare": [j, j + 1],
                    "swap": True
                })

    return {"steps": steps, "stats": {"comparisons": comparisons, "swaps": swaps}}
