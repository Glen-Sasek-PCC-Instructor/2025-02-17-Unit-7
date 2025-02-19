# https://chatgpt.com/share/67b6428b-5cd8-8013-9716-a588cd5ce422

def quicksort(arr, depth=0):
    indent = "  " * depth  # Indentation for better visualization
    print(f"{indent}Quicksort called on: {arr}")

    if len(arr) <= 1:
        print(f"{indent}Base case reached: {arr}")
        return arr

    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    print(f"{indent}Pivot: {pivot}")
    print(f"{indent}Left: {left}")
    print(f"{indent}Middle: {middle}")
    print(f"{indent}Right: {right}")

    sorted_left = quicksort(left, depth + 1)
    sorted_right = quicksort(right, depth + 1)

    result = sorted_left + middle + sorted_right
    print(f"{indent}Merged: {result}")
    return result

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(f"Final sorted array: {sorted_arr}")
