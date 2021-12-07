"""
--- Part Two ---
Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""

from typing import List, Tuple

SAMPLE_INPUT = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2)
]


def read_input(filename: str) -> List[Tuple[str, int]]:
    with open(filename) as file:
        rows = file.readlines()
        return [
            (row.split()[0], int(row.split()[1]))
            for row in rows
        ]


def calculate_position(instructions: List[Tuple[str, int]]) -> dict:
    coordinate_map = {
        "horizontal": 0,
        "aim": 0,
        "depth": 0
    }

    for instruction in instructions:
        direction = instruction[0]
        value = instruction[1]

        if direction == "forward":
            aim = coordinate_map["aim"]
            if aim != 0:
                coordinate_map["depth"] = coordinate_map["depth"] + (aim * value)

            coordinate_map["horizontal"] = coordinate_map["horizontal"] + value
        elif direction == "up":
            coordinate_map["aim"] = coordinate_map["aim"] - value
        elif direction == "down":
            coordinate_map["aim"] = coordinate_map["aim"] + value

    return coordinate_map


if __name__ == "__main__":
    input_filename = "day2-input.txt"
    coordinates = calculate_position(instructions=read_input(input_filename))
    print("coordinates", coordinates)