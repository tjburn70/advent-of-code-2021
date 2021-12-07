"""
--- Part Two ---
Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A
200  A B
208  A B C
210    B C D
200  E   C D
207  E F   D
240  E F G
269    F G H
260      G H
263        H
Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
"""

from typing import List

sample_input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def read_input(filename: str) -> List[int]:
    with open(filename) as file:
        rows = file.readlines()
        return [int(row.strip()) for row in rows]


def generate_slices(depths: List[int]) -> List[List[int]]:
    window_size = 3
    window_slices = []
    for i in range(len(depths) - (window_size - 1)):
        window_slice = depths[i : i + window_size]
        window_slices.append(window_slice)

    return window_slices


def sum_window_slices(window_slices) -> List[int]:
    return list(map(lambda x: sum(x), window_slices))


def calculate_num_increasing_window_depths(depths: List[int]) -> int:
    num_increasing = 0
    window_slices = generate_slices(depths)
    summed_slices = sum_window_slices(window_slices)
    total_depths = len(summed_slices)
    for i in range(total_depths):
        if i != (total_depths - 1):
            curr_depth = summed_slices[i]
            next_depth = summed_slices[i + 1]
            if next_depth > curr_depth:
                num_increasing += 1
    return num_increasing


if __name__ == "__main__":
    input_filename = "day1-input.txt"
    answer = calculate_num_increasing_window_depths(depths=read_input(input_filename))
    print(f"Number of increasing depths: {answer}")
