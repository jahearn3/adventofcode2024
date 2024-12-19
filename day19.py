# Day 19: Linen Layout

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f'example{day}.txt')
data = ld.load_data(f'input{day}.txt')

patterns = data[0].split(', ')
designs = []
for line in data[2:]:
    designs.append(line)


def can_construct(design, patterns):
    # Dynamic Programming
    # Create a DP array to store whether a substring can be constructed
    # dp[i] will be True if design[0:i] can be constructed from patterns
    dp = [False] * (len(design) + 1)
    dp[0] = True  # Base case: empty string can be constructed
    for i in range(1, len(design) + 1):
        for pattern in patterns:
            # Check if the current pattern can be found at the end of the
            # substring and if the preceding part of the string can be
            # constructed
            if design[i - len(pattern):i] == pattern and dp[i - len(pattern)]:
                dp[i] = True
                break
    # Return whether the entire design string can be constructed
    return dp[len(design)]


ans = 0
for design in designs:
    if can_construct(design, patterns):
        ans += 1

print(ans)

# Part 2


def count_ways_to_construct(design, patterns):
    dp = [0] * (len(design) + 1)
    dp[0] = 1
    for i in range(1, len(design) + 1):
        # See if each pattern can fit into the substring ending at i
        for pattern in patterns:
            # Check if the current pattern matches the end of the substring
            if design[i - len(pattern):i] == pattern:
                # If it matches, add the number of ways
                # to construct the preceding part
                dp[i] += dp[i - len(pattern)]

    # Return the number of ways to construct the entire design string
    return dp[len(design)]


ans = 0
for design in designs:
    ans += count_ways_to_construct(design, patterns)

print(ans)
