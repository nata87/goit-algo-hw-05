def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return iterations, upper_bound


if __name__ == "__main__":
    arr = [0.1, 1.9, 4.3, 7.7, 14.0, 105.6, 166.8]
    target = float(input("Введіть число для пошуку: "))
    iters, upper = binary_search(arr, target)
    print(f"Ітерацій: {iters}")
    if upper is not None:
        print(f"Верхня межа: {upper}")
    else:
        print("Немає елемента, більшого або рівного заданому значенню.")

