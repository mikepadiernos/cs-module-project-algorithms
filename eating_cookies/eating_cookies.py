"""
Input: an integer
Returns: an integer
"""


def eating_cookies(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

# def eating_cookies(n, memo):
#     if n == 0 or n == 1:
#         return 1
#     if n < 0:
#         return 0
#     if n in memo:
#         return memo[n]
#     memo[n] = eating_cookies(n-3, memo) + eating_cookies(n-2, memo) + eating_cookies(n-1, memo)
#     return memo[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
