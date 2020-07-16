
arr = [0,1,2,3,4,5,6,7,8,9,10]

def binary_search(arr, item):
    min = 0
    hight = len(arr) - 1
    while min <= hight:
        mid = int((min + hight)/2)
        guess = arr[mid]
        print(guess)
        if guess == item:
            return mid
        if guess > item:
            hight = (mid - 1)
        if guess < item:
            min = (mid + 1)

    return None

print(binary_search(arr, 1))