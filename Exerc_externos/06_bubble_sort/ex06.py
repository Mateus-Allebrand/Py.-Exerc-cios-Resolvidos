
lista = [10,1,5,3,4,7,2,6,8,9]

print(lista)

# lista.sort()

# print(lista)


lista2 = [[10,1,5],[3,4,7],[2,6,8,9]]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        print(f"i {i}")
        for j in range(0, n-i-1):
            print(f" j {j}")
            if arr[j] > arr[j+1]:
               arr[j] , arr[j+1] = arr[j+1], arr[j]
      
    return arr


        
print(bubble_sort(lista))

