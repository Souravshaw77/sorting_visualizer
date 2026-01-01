def insertion_sort(arr):
    steps = []
    comparisons = swaps = 0
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            comparisons += 1
            a[j + 1] = a[j]
            swaps += 1
            steps.append({
                "array": a.copy(),
                "compare": [j, j + 1],
                "swap": True
            })
            j -= 1

        a[j + 1] = key
        steps.append({
            "array": a.copy(),
            "compare": [j + 1],
            "swap": False
        })

    return {"steps": steps, "stats": {"comparisons": comparisons, "swaps": swaps}}
