from part1 import get_boxes, connections


def main():
    boxes = get_boxes("day08/input.txt")

    connection_list = connections(boxes)

    circuits: list[set[tuple[int, int, int]]] = []


    #basically the same code as before but we initialize the circuits list with every box on it's own
    # and then iterate through the connections until we only have a single circuit

    for box in boxes:
        circuits.append(set([box]))

    
    while len(circuits) > 1:

        conn = connection_list.pop(0)[1]

        connected_circuits: list[set[tuple[int, int, int]]] = []

        for circuit in circuits:
            if conn[0] in circuit or conn [1] in circuit:
                connected_circuits.append(circuit)
        
        big_circuit: set[tuple[int, int, int]] = set()
        
        for circuit in connected_circuits:
            big_circuit = big_circuit.union(circuit)
            circuits.remove(circuit)
        
        circuits.append(big_circuit)
    
    #me when I abuse python's lack of scoping rules
    #(this would never fly in Rust)
    print(conn[0][0] * conn[1][0]) # type: ignore


if __name__ == "__main__":
    main()