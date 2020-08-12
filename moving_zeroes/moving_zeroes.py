'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    moved = 0
    for n in range(0, len(arr)):
        if arr[n] is not 0:
            arr[moved], arr[n] = arr[n], arr[moved]
            moved += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
