def solution(arr):
    # Create 2 lists to store integers
    new_temp_array = []
    not_used = []
    arr1 = []
    arr2 = []

    # remove the negatives and store them in a list - wont need them
    for i in arr:
        if i < 0:
            not_used.append(i)
        else:
            new_temp_array.append(i)

    # reference % to sort out the index of the even and odd positions
    for i in new_temp_array:
        location = new_temp_array.index(i)
        if location % 2 == 0:
            arr2.append(i)
        else:
            arr1.append(i)
    # since 3 is sorted out to 2nd array we automatically append it to the 1st array
    arr1.append(arr2[0])

    # sum of both arrays
    sum_arr1 = sum(arr1)
    sum_arr2 = sum(arr2)

    # if statement to check which side of the binary tree wins
    if sum_arr1 > sum_arr2:
        print("Left")
    else:
        print("Right")
