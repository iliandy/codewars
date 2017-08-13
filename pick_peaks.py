# https://www.codewars.com/kata/pick-peaks/
def pick_peaks(arr):
    pos = []
    peaks = []

    for i in range(1, len(arr)-1):
        # absolute peak
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            pos.append(i)
            peaks.append(arr[i])
        # start of plateau
        elif arr[i] > arr[i-1] and arr[i] == arr[i+1]:
            for j in range(i+1, len(arr)):
                # values increase above plateau or remain flat until end
                if arr[j] > arr[i] or (arr[j] == arr[i] and j == len(arr)-1):
                    break
                elif arr[j] < arr[i]:
                    pos.append(i)
                    peaks.append(arr[i])
                    break

    return {"pos": pos, "peaks": peaks}

arr1 = [1,2,3,6,4,1,2,3,2,1]
arr2 = [3,2,3,6,4,1,2,3,2,1,2,3]
arr3 = [3,2,3,6,4,1,2,3,2,1,2,2,2,1]
arr4 = [2,1,3,1,2,2,2,2,1]
arr5 = [2,1,3,1,2,2,2,2]
print pick_peaks(arr1)
print pick_peaks(arr2)
print pick_peaks(arr3)
print pick_peaks(arr4)
print pick_peaks(arr5)
