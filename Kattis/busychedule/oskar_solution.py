def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        l = arr[:mid]
        r = arr[mid:]

        # Recursive cases for both sides
        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        # Merge part
        while i < len(l) and j < len(r):
            left_time = l[i].split(' ')
            right_time = r[j].split(' ')

            if left_time[1] == 'a.m.' and right_time[1] == 'p.m.':
                arr[k] = l[i]
                i += 1
            elif left_time[1] == 'p.m.' and right_time[1] == 'a.m.':
                arr[k] = r[j]
                j += 1
            else:
                left_hours, left_minutes = left_time[0].split(':')
                right_hours, right_minutes = right_time[0].split(':')

                if int(left_hours) == 12 and int(right_hours) != 12:
                    arr[k] = l[i]
                    i += 1
                elif int(left_hours) != 12 and int(right_hours) == 12:
                    arr[k] = r[j]
                    j += 1
                elif int(left_hours) < int(right_hours):
                    arr[k] = l[i]
                    i += 1
                elif int(right_hours) < int(left_hours):
                    arr[k] = r[j]
                    j += 1
                else:
                    if int(left_minutes) < int(right_minutes):
                        arr[k] = l[i]
                        i += 1
                    else:
                        arr[k] = r[j]
                        j += 1

            k += 1

        # Checking if any element was left
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


def solution():
    n = int(input())
    schedules = []
    while n != 0:
        schedule = []
        for i in range(n):
            schedule.append(input())

        schedules.append(schedule)

        n = int(input())

    for schedule in schedules:
        mergeSort(schedule)
        print('\n'.join(schedule))
        print('')


solution()
