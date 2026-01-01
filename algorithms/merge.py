def merge_sort(arr):
    steps = []
    comparisons = 0

    def merge(a, l, m, r):
        nonlocal comparisons
        left = a[l:m]
        right = a[m:r]
        i = j = 0
        k = l

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
            steps.append({"array": a.copy(), "compare": [k - 1], "swap": True})

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
            steps.append({"array": a.copy(), "compare": [k - 1], "swap": False})

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
            steps.append({"array": a.copy(), "compare": [k - 1], "swap": False})

    def divide(a, l, r):
        if r - l > 1:
            m = (l + r) // 2
            divide(a, l, m)
            divide(a, m, r)
            merge(a, l, m, r)

    a = arr.copy()
    divide(a, 0, len(a))
    return {"steps": steps, "stats": {"comparisons": comparisons, "swaps": "N/A"}}
