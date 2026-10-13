# ANSWER KEY - Bubble Sort and Insertion Sort
# Do not put this file in the students' repository.


# Exercise 1 -----------------------------------------------------------------

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                swapped = True
        if swapped == False:
            break
    return data


# Exercise 2 -----------------------------------------------------------------

def bubble_sort_trace(data):
    trace = []
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                swapped = True
        if swapped == False:
            break
        trace.append(data.copy())       # a COPY, not the list itself
    return trace


# Exercise 3 -----------------------------------------------------------------

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:     # j >= 0 stops at the start of the list
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key
    return data


# Exercise 4 -----------------------------------------------------------------

def insertion_sort_trace(data):
    trace = []
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key
        trace.append(data.copy())
    return trace


# Exercise 5 -----------------------------------------------------------------
# Insertion sort on the score (record[1]), biggest first.
# Using < (not <=) means equal scores are never moved past each other,
# so students with the same score stay in their original order.

def rank_students(records):
    for i in range(1, len(records)):
        key = records[i]
        j = i - 1
        while j >= 0 and records[j][1] < key[1]:
            records[j + 1] = records[j]
            j = j - 1
        records[j + 1] = key
    return records
