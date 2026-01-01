def heap_sort(arr):
    steps = []
    comparisons = swaps = 0
    a = arr.copy()

    def heapify(n, i):
        nonlocal comparisons, swaps
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n:
            comparisons += 1
            if a[l] > a[largest]:
                largest = l

        if r < n:
            comparisons += 1
            if a[r] > a[largest]:
                largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            swaps += 1
            steps.append({"array": a.copy(), "compare": [i, largest], "swap": True})
            heapify(n, largest)

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        swaps += 1
        steps.append({"array": a.copy(), "compare": [0, i], "swap": True})
        heapify(i, 0)

    return {"steps": steps, "stats": {"comparisons": comparisons, "swaps": swaps}}
