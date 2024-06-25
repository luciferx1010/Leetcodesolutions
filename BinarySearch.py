arr = [1, 2, 3, 4, 8, 6, 7, 5, 9]
arr2 = sorted(arr)
print("sorted array:",arr2)
target = int(input("Enter number to find: "))

first = 0
last = len(arr2)-1
found=False

for _ in range(len(arr2)):
    mid = (first + last) // 2
    if arr[mid] == target:
        found = True
        break
    elif arr2[mid] < target:
        first = mid + 1
    else:
        last = mid - 1
    
if found:
    print(f"{target} is present in array")
else:
    print(f"{target} is not present in array")
    
