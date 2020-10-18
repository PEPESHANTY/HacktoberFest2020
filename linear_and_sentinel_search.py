def linear_search(arr, num, a):
    i = 0
    for i in range(0, num):
        if (arr[i] == a) & (i < num):
            print("The student with roll no. ", a, "was present for program.")
            break
    else:
        print("The student with roll no. ", a, "was NOT present for program.")
        
def sentinel_search(arr, num, a):
    last = arr[num - 1]
    arr[num - 1] = a
    i = 0

    while (arr[i] != a):
        i += 1
    arr[num - 1] = last

    if ((i < num - 1) or (a == arr[num - 1])):
        print("The student with roll no. ", a, "was present for program.")
    else:
        print("The student with roll no. ", a, "was NOT present for program.")

arr=list(map(int,input("enter array :").rstrip().split()))
num=len(arr)
print(arr)
print("1.linear search")
print("2.sentinel search")

choice = int(input("Enter your choice  :"))
if (choice == 1 or choice == 2):
    a = int(input("Enter Roll No. to be searched  :"))

if choice == 1:
    linear_search(arr, num, a)
elif choice == 2:
    sentinel_search(arr, num, a)
else:
    print("Invalid Choice,please choose\n 1.sentinel search or\n 2.linear search")