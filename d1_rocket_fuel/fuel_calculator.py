import sys

# mass divided by 3, round down, substract 2
def calcfuel(mass):
    return max((mass // 3) - 2, 0)


def calcmodulefuel(mass):
    total_fuel = 0
    mass_remaining = mass
    while mass_remaining > 0:
        mass_remaining = calcfuel(mass_remaining)
        total_fuel += mass_remaining

    return total_fuel


def runtests():
    assert calcfuel(14) == 2, "CalcFuel Test 1 (14,2) failed"
    assert calcfuel(1969) == 654, "CalcFuel Test 2 (1969,654) failed"
    assert calcmodulefuel(1969) == 966, "CalcModuleFuel Test 1 (1969,966) failed"
    assert calcmodulefuel(100756) == 50346, "CalcModuleFuel Test 2 (100756, 50346) failed"
    print("All tests passed")


if __name__ == '__main__':
    test = False
    rocket_modules = sys.argv[1]

    if test:
        runtests()
    else:
        requirements = 0
        with open(rocket_modules) as modules:
            for module in modules:
                requirements += calcmodulefuel(int(module))
    
        print(f"Fuel Requirements: {requirements}")
