import bisect
import math

connection = tuple[tuple[int, int, int], tuple[int, int, int]]

def get_boxes(input: str) -> set[tuple[int, int, int]]:

    out: set[tuple[int, int, int]] = set()

    with open(input) as f:
        for line in f:
            line = line.strip()

            x, y, z = line.split(',')

            out.add((int(x), int(y), int(z)))
    
    return out

def sort_func(x: tuple[int, connection]) -> int:
    return -x[0]

def connections(boxes: set[tuple[int, int, int]]) -> list[tuple[int, connection]]:

    boxes = boxes.copy()

    out: list[tuple[int, connection]] = []

    while len(boxes) > 0:

        a = boxes.pop()

        for b in boxes:

            dx = a[0] - b[0]
            dy = a[1] - b[1]
            dz = a[2] - b[2]

            dist_sq = dx * dx + dy * dy + dz * dz

            bisect.insort(out, (dist_sq, (a, b))) # type: ignore
        
        # Keep the size of the list small otherwise it takes forever :P
        if len(out) > 10_000:
            out = out[:10_000]

    return out


def main():
    boxes = get_boxes("day08/input.txt")

    target_connections = 1000

    #this gives us a sorted list of the top 10,000 shortest connections
    connection_list = connections(boxes)

    circuits: list[set[tuple[int, int, int]]] = []


    for _ in range(target_connections):

        #grab the shortest connection
        conn = connection_list.pop(0)[1]

        #We now grab every circuit that includes these two boxes

        connected_circuits: list[set[tuple[int, int, int]]] = []

        for circuit in circuits:
            if conn[0] in circuit or conn [1] in circuit:
                connected_circuits.append(circuit)
        
        #then we merge them into a big circuit and add them back into the list of mater circuits

        big_circuit: set[tuple[int, int, int]] = set(conn) # We add both boxes here because we can't be sure they're in any of the circuits we found
        
        for circuit in connected_circuits:
            big_circuit = big_circuit.union(circuit)
            circuits.remove(circuit)
        
        circuits.append(big_circuit)
    
    
    sizes = (len(c) for c in circuits)
    
    print(math.prod(sorted(sizes, reverse=True)[:3]))


if __name__ == "__main__":
    main()