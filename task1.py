from typing import List, Tuple

def find_min_max(arr: List[int]) -> Tuple[int, int]:
    # Базовий випадок: якщо масив містить один елемент
    if len(arr) == 1:
        return arr[0], arr[0]

    # Якщо масив містить два елементи
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    # Рекурсивне розбиття масиву на дві половини
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Об'єднання результатів
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return overall_min, overall_max

if __name__ == '__main__':
    arr = [3, 1, 7, 2, 9, 4, 6]
    min_val, max_val = find_min_max(arr)
    print(f"Min: {min_val}, Max: {max_val}")