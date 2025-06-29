
arr=[11,22,33,44,55,66,77,88,99]

my_key=99
found=False

for i in arr:
    if i==my_key:
        print("Found")
        break

    else:
        print("Not found")


start_index=0
end_index=len(arr)-1
found=False

while start_index<= end_index:

    mid=(start_index+end_index)//2
    if arr[mid]==my_key:
        print("Found element at position: ", mid)
        found=True
        break
    elif my_key < arr[mid]:
        end_index=mid-1

    elif my_key>arr[mid]:
        start_index = mid + 1

if not found:
    print(f"{my_key} not found in the list!")



def recursive_binarysearch(start_index,end_index):
    #Base case
    if start_index > end_index:
        return -1
    mid=(start_index+end_index)//2

    if arr[mid]==my_key:
        return mid
    elif my_key< arr[mid]:
        return  recursive_binarysearch(start_index,mid-1)
    else:
        return recursive_binarysearch(mid+1,end_index)


result=recursive_binarysearch(0,len(arr)-1)

if result != -1:
    print("The value is found at the index:",result)

else:
    print(f"{my_key} not found in the list!")



