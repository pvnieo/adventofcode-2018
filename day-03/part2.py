def get_path(wire):
    path = [(0, 0)]
    for x in wire:
        for _ in range(x[1]):
            if x[0] == 'D':
                path.append((path[-1][0], path[-1][1]-1))
            elif x[0] == 'U':
                path.append((path[-1][0], path[-1][1]+1))
            elif x[0] == 'R':
                path.append((path[-1][0]+1, path[-1][1]))
            elif x[0] == 'L':
                path.append((path[-1][0]-1, path[-1][1]))
    return path[1:]


def main(input_):
    wire1, wire2 = list(map(lambda w: [(x[0], int(x[1:])) for x in w.split(",")], input_.strip().split("\n")))
    path1, path2 = get_path(wire1), get_path(wire2)
    for inter in set(path1).intersection(set(path2)):
        continue
    return min([path1.index(x) + path2.index(x) for x in set(path1).intersection(set(path2))]) + 2


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_ = f.read()
        print(main(input_))
