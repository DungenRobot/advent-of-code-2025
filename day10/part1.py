
#https://docs.python.org/3/library/itertools.html#itertools-recipes
from itertools import chain, combinations

def powerset(iterable): # type: ignore
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable) # type: ignore
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1)) # type: ignore




t_lights = int
t_button_masks = list[int]

def get_input(path: str) -> list[tuple[t_lights, t_button_masks]]:

    out: list[tuple[t_lights, t_button_masks]] = []

    with open(path) as f:
        for line in f:
            line = line.strip()

            lights, line = line.split('] ', 1)

            lights = lights[1:]

            light_layout = 0

            for char in lights:

                light_layout *= 2

                if char == '#':
                    light_layout += 1


            button_groups, _ = line.split(' {', 1)

            button_groups = [[int(x) for x in group.strip('()').split(',')] for group in button_groups.split(' ')]

            button_masks: t_button_masks = []

            for group in button_groups:

                mask = 0

                for i in range(len(lights)):
                    mask *= 2
                    if i in group:
                        mask += 1

                button_masks.append(mask)
            
            out.append((light_layout, button_masks))

    return out



def solve_buttons(lights: t_lights, button_groups: t_button_masks) -> int:

    lowest = 1_000_000

    for groups in powerset(button_groups):

        if len(groups) >= lowest:
            continue

        attempt = 0

        for group in groups:
            attempt ^= group

        if attempt == lights:
            lowest = len(groups)

    return lowest


def main():
    input = get_input("day10/input.txt")

    button_presses: int = 0

    for box in input:
        button_presses += solve_buttons(box[0], box[1])

    print(button_presses)

    

    



if __name__ == "__main__":
    main()