"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


def single_number(arr):
    for a in range(len(arr)):
        count = 0
        for b in range(len(arr)):
            if arr[a] is arr[b]:
                count += 1
        if count is 1:
            return arr[a]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
