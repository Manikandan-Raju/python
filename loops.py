for i in range(5):
    print(f"Outer loop iteration {i}")
    for j in range(3):
        print(f"  Inner loop iteration {j}")
        if i == 2 and j == 1:
            print("    Breaking out of the inner loop")
            break
    else:
        continue
    break

print("Loop execution completed")