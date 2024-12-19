if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr1 = set(arr)
    arr2 = sorted(arr1)
    print(arr2[-2])
