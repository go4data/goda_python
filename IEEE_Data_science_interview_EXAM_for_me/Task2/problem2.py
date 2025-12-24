def num_unit_energy():
    units_list = list()
    t = int(input("Enter the number of test cases you want: "))
    print(f"Enter the {t} cases you want\n")
    for i in range(t):
        coordinates =input("\n")
        n, x1, y1, x2, y2 = map(int, coordinates.split())
        layer1 = min(n-x1, n-y1,x1-1, y1-1)
        layer2 = min(n-x2, n-y2, x2-1, y2-1)
        num_energy_unit = abs(layer1-layer2)
        units_list.append(num_energy_unit)
    print("\n the energy units for each case \n")
    for x in range (t):
    
        print(units_list[x],"\n")

num_unit_energy()