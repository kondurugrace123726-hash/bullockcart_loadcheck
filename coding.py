
capacity = int(input().strip())
loads = list(map(int, input().strip().split()))

for load in loads:
    if load > capacity:
        print(f"Rejected Load: {load}")
    else:
        print(f"Accepted Load: {load}")