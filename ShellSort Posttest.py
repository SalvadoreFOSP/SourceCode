import random

def ShellSort(data):
    gap = (len(data)//2)
    a=0

    while gap > 0 :
        for i in range(gap,len(data)):
            value = data[i]
            j = i

            while j >= gap and data[j-gap] > value:
                data[j] = data[j-gap]
                j-=gap

            data[j] = value
            print(data)
        print("Iterasi ke",a,": ",data,"dengan gap ",gap )
        a+=1

        gap //= 2

    return data

list_array = []

for i in range(10):
    list_array.append(random.randint(1, 100))
print("List Awal:")
print(list_array)
print()

list_array = ShellSort(list_array)
print("\nList setelah diurutkan :")
print(list_array)
print()