def compute_mass(input_):
    total_fuel = 0
    for module_mass in input_.strip().split('\n'):
        module_fuel = max(int(module_mass) // 3 - 2, 0)
        total_fuel += module_fuel
        while module_fuel > 0:
            module_fuel = max(int(module_fuel) // 3 - 2, 0)
            total_fuel += module_fuel
    return total_fuel


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_ = f.read()
        print(compute_mass(input_))