import random

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] 

        print(f"Pivot : {pivot}")
        
        less = [x for x in arr[1:] if x <= pivot]

        greater = [x for x in arr[1:] if x > pivot]
    
    return QuickSort(less) + [pivot] + QuickSort(greater)

list_array = []

for i in range(10):
    list_array.append(random.randint(1, 100))
print("List Awal:")
print(list_array)
print()

list_array = QuickSort(list_array)
print("\nList setelah diurutkan :")
print(list_array)
print()