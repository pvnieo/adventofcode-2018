from collections import defaultdict


class OrbitNavigator:
    def count_children(self, obj):
        return len(self.orbits[obj]) + sum([self.count_children(obj_) for obj_ in self.orbits[obj]])

    def main(self, input_):
        map_data = [[y for y in x.split(')')] for x in input_.strip().split("\n")]
        self.orbits = defaultdict(list)
        for relation in map_data:
            self.orbits[relation[0]].append(relation[1])

        return sum([self.count_children(obj) for obj in list(self.orbits)])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_ = f.read()
        print(OrbitNavigator().main(input_))
