


t_button_groups = list[set[int]]
t_joltages = list[int]

def get_input(path: str) -> list[tuple[t_button_groups, t_joltages]]:

    out: list[tuple[t_button_groups, t_joltages]] = []

    with open(path) as f:
        for line in f:
            line = line.strip()

            _lights, line = line.split('] ', 1)

            groups, joltages = line.split(' {', 1)


            button_groups: t_button_groups = [set([int(x) for x in group.strip('()').split(',')]) for group in groups.split(' ')]

            joltages = [ int(x) for x in joltages[:-1].split(',')]

            out.append((button_groups, joltages))

    return out


def solution_valid(solution: list[float]) -> bool:
    for num in solution:

        if abs(num) < 0.0001:
            continue

        if num < 0.0:
            return False
        if abs(num - int(num)) > 0.0001:
            return False
    return True

def solution_possible(joltages: t_joltages) -> bool:
    for i in joltages:
        if i < 0:
            return False
    return True

def buttons_posible(buttons: t_button_groups, joltages: t_joltages):

    for i, num in enumerate(joltages):

        if num > 0:

            group_has_i = False

            for group in buttons:
                if i in group:
                    group_has_i = True

            if group_has_i == False:
                return False

    return True


import sympy as sp

def solve_joltage(buttons: t_button_groups, joltages: t_joltages, force: bool = False, depth: int = 0) -> int:

    if sum(joltages) == 0:
        return 0


    if len(buttons) > len(joltages) or force:

        joltages = joltages.copy()

        lowest = 100_000

        for i in range(max(joltages)):
            
            if not solution_possible(joltages):
                break

            x = solve_joltage(buttons[1:], joltages)

            lowest = min(lowest, x + i)

            for num in buttons[0]:
                joltages[num] -= 1

        return lowest

    else:

        a_tmp: list[list[int]] = []

        for i in range(len(joltages)):
            row: list[int] = []
            for group in buttons:
                if i in group:
                    row.append(1)
                else:
                    row.append(0)
            a_tmp.append(row)

    
        a = sp.Matrix(a_tmp)
        b = sp.Matrix(joltages)

        solution: sp.FiniteSet = sp.linsolve((a, b)) # type: ignore

        for x in solution:
            pass

        #print(solution)

        if solution == sp.EmptySet:
            return 100_000

        if len(solution.free_symbols) == 0 :

            total = 0

            for x in solution.args[0]:
                if x < 0:
                    return 1000_000

                total += x
            return total
        
        s_cpy = solution.copy()

        t = sp.symbols('tau0')

        lowest = 0

        for x in s_cpy.args[0]:

            x = x.subs(t, 0)

            lowest = min(x, lowest)

            #print(x)
        
        total = 0

        for x in s_cpy.args[0]:

            total += x.subs(t, -lowest)


        return total

def main():
    input = get_input("day10/input.txt")

    button_presses: int = 0

    for box in input:
        x = solve_joltage(box[0], box[1])
        print("solution: ", x)
        button_presses += x

    print(button_presses)

    

    
if __name__ == "__main__":
    main()