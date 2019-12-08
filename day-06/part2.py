from collections import defaultdict


class OrbitNavigator:
    def get_distance_children(self, obj, i=0):
        d = {x: i+1 for x in self.orbits[obj]}
        for obj_ in self.orbits[obj]:
            d.update(self.get_distance_children(obj_, i+1))
        return d

    def main(self, input_):
        map_data = [[y for y in x.split(')')] for x in input_.strip().split("\n")]
        self.orbits = defaultdict(list)
        for relation in map_data:
            self.orbits[relation[0]].append(relation[1])

        distances = {obj: self.get_distance_children(obj) for obj in list(self.orbits)}

        return min([x['YOU'] + x['SAN'] - 2 for x in distances.values() if 'YOU' in x and 'SAN' in x])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_ = f.read()
        print(OrbitNavigator().main(input_))
