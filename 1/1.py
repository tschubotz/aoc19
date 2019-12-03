def calc_fuel(mass):
    fuel = int(mass / 3.0) - 2
    fuel = fuel if fuel > 0 else 0
    return fuel if fuel <= 0 else fuel + calc_fuel(fuel)

def main():

    total = 0
    with open('./input.txt') as f:
        for l in f.readlines():
            mass = int(l.rstrip('\n'))
            print(mass)
            # import pdb;pdb.set_trace()
            fuel = calc_fuel(mass)
            print(fuel)

            total += fuel

    print(total)

if __name__ == '__main__':
    main()