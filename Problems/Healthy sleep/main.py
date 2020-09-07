A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
    print("Normal")
else:
    if A > H and H <= B:
        print("Deficiency")
    else:
        print("Excess")