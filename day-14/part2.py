from math import ceil
from collections import defaultdict


class SpaceStoichiometry:
    def need_orbs(self, fuel):
        need = defaultdict(int)
        need["FUEL"] = fuel
        while True:
            try:
                ele, qt = next(((el, qt) for el, qt in need.items() if qt > 0 and el != "ORE"))
            except Exception:
                break
            ele_coef, ingreds = self.reactions[ele]
            factor = ceil(qt / ele_coef)
            for n_coef, n_name in ingreds:
                need[n_name] += n_coef * factor
            need[ele] -= factor * ele_coef

        return need["ORE"]

    def main(self, reactions):
        rea = reactions.strip().split("\n")
        reactions = [[[(int(e.split()[0]), e.split()[1]) for e in s.split(", ")] for s in l.strip().split(' => ')] for l in rea]
        self.reactions = {r[1][0][1]: (int(r[1][0][0]), r[0]) for r in reactions}

        total_orb = 1e12
        need_orbs_per_fuel = self.need_orbs(1)
        base_fuel, prime = total_orb // need_orbs_per_fuel, 0
        while True:
            need_orb = self.need_orbs(base_fuel + prime)
            if need_orb < total_orb:
                prime += 1000
            else:
                prime -= 1000
                break
        while True:
            need_orb = self.need_orbs(base_fuel + prime)
            if need_orb < total_orb:
                prime += 1
            else:
                return int(base_fuel + prime - 1)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        reactions = f.read()
        print(SpaceStoichiometry().main(reactions))
