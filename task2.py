from typing import List
import random

def quick_select(arr: List[int], k: int) -> int:
    if not 1 <= k <= len(arr):
        raise ValueError("k має бути в межах від 1 до довжини масиву")

    def select(left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return arr[left]

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    # Зменшуємо k на 1, бо індексація з нуля
    return select(0, len(arr) - 1, k - 1)

if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"{k}-й найменший елемент: {quick_select(arr, k)}")  # Очікувано: 7
