def quick_sort(arr):
    steps = []
    comparisons = swaps = 0
    a = arr.copy()

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1
            steps.append({"array": a.copy(), "compare": [j, high], "swap": False})

            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps += 1
                steps.append({"array": a.copy(), "compare": [i, j], "swap": True})

        a[i + 1], a[high] = a[high], a[i + 1]
        swaps += 1
        steps.append({"array": a.copy(), "compare": [i + 1, high], "swap": True})
        return i + 1

    def qs(low, high):
        if low < high:
            pi = partition(low, high)
            qs(low, pi - 1)
            qs(pi + 1, high)

    qs(0, len(a) - 1)
    return {"steps": steps, "stats": {"comparisons": comparisons, "swaps": swaps}}
