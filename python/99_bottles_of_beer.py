for i in range(99, 0, -1):
    # bottle or bottles
    b1 = "bottle" if i == 1 else "bottles"
    b2 = "bottle" if i - 1 == 1 else "bottles"

    print(f"{i} {b1} of beer on the wall\n{i} {b1} of beer.")

    if i > 1:
        print(f"Take one down and pass it around\n{i-1 if i-1 > 0 else 'no more'} {b2} of beer on the wall!\n")
    else:
        print("Take one down and pass it around, no more bottles of beer on the wall!\n")
