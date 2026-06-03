"""Demonstrate `for ... else` behaviour.

`for` loops can have an `else` block. The `else` runs only if the loop
completes normally (no `break` encountered). This is useful for
search patterns and distinguishing "not found" vs "found".
"""


print("--- Example 1: simple for/else (no break) ---")
for i in range(3):
    print("i=", i)
else:
    # runs because the loop finished without a break
    print("Loop completed without break")


print('\n--- Example 2: simple for/else (with break) ---')
for i in range(3):
    print("i=", i)
    if i == 1:
        print("Breaking at i==1")
        break
else:
    # will NOT run because we broke out of the loop
    print("This won't print when break occurred")


print('\n--- Example 3: nested loops showing else usage ---')
for i in range(5):
    print(f"Outer loop iteration {i}")
    for j in range(5):
        print(f"  Inner loop iteration {j}")
        if i == 2 and j == 1:
            print("    Breaking out of the inner loop")
            # break will skip the inner `else` and continue after it
            break
    else:
        # This else executes only when the inner loop did NOT break
        # `continue` here skips the remaining outer-loop body and
        # proceeds to the next iteration of the outer loop.
        print("  Inner loop completed without break; continuing outer loop")
        continue
    # If we reach here it means the inner loop did break; we break outer too
    print("Breaking outer loop because inner loop broke")
    break

print("Loop execution completed")