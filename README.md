# Python Bubble Sort and Insertion Sort

Python Bubble Sort and Insertion Sort PDF:

https://drive.google.com/file/d/1DpK-S8RL9LZenG2QnSlxk7drOTGo5xVL/view?usp=sharing

**Rules for this assignment**

- Do **not** use `sorted()` or `.sort()`. The tests check for this — write the
  algorithms yourself.


## Exercise 1

**Problem:**

`bubble_sort(data)`

Sort `data` from smallest to largest using **bubble sort**, and return it.
Stop early if a pass makes no swaps.

**Example:**

    Example Input:
        data = [5, 6, 1, 3]

    Program Output:
        [1, 3, 5, 6]

---

## Exercise 2

**Problem:**

`bubble_sort_trace(data)`

Sort `data` using bubble sort, and return a **trace**: a list showing what
`data` looked like after each pass.

- After every pass that made **at least one swap**, add a copy of `data` to the trace.
- A pass with **no swaps** means the list is sorted — stop, and do **not** add it.
- If the list is already sorted (or empty), the trace is `[]`.

**Example:**

    Example Input:
        data = [5, 6, 1, 3]

    Program Output:
        [[5, 1, 3, 6], [1, 3, 5, 6]]

    Pass 1 moves 6 to the end      -> [5, 1, 3, 6]
    Pass 2 moves 5 into place      -> [1, 3, 5, 6]
    Pass 3 makes no swaps          -> stop, not added

    Example Input:
        data = [1, 2, 3]

    Program Output:
        []


---

## Exercise 3

**Problem:**

`insertion_sort(data)`

Sort `data` from smallest to largest using **insertion sort**, and return it.

**Example:**

    Example Input:
        data = [5, 6, 1, 3]

    Program Output:
        [1, 3, 5, 6]

---

## Exercise 4

**Problem:**

`insertion_sort_trace(data)`

Sort `data` using insertion sort, and return a trace of what `data` looked like
after **every step** (`i = 1, 2, 3, ...` up to the end).

- Add a copy after **every** step — even if nothing moved in that step.
- A list with 0 or 1 items has no steps, so its trace is `[]`.

**Example:**

    Example Input:
        data = [5, 6, 1, 3]

    Program Output:
        [[5, 6, 1, 3], [1, 5, 6, 3], [1, 3, 5, 6]]

    Step i = 1: key = 6, nothing moves     -> [5, 6, 1, 3]
    Step i = 2: key = 1, goes to the front -> [1, 5, 6, 3]
    Step i = 3: key = 3, goes after 1      -> [1, 3, 5, 6]

    Example Input:
        data = [1, 2, 3]

    Program Output:
        [[1, 2, 3], [1, 2, 3]]

Notice the difference from Exercise 2: bubble sort can **stop early**,
but insertion sort always does every step.

---

## Exercise 5

**Problem:**

`rank_students(records)`

`records` is a list of students. Each student is a list `[name, score]`.

Sort the students by score, **highest first**, using **insertion sort**,
and return the list.

If two students have the **same score**, they must stay in the same order they
were in originally.

**Example:**

    Example Input:
        records = [["Bat", 78], ["Saraa", 91], ["Anu", 78], ["Dorj", 91], ["Tuya", 85]]

    Program Output:
        [["Saraa", 91], ["Dorj", 91], ["Tuya", 85], ["Bat", 78], ["Anu", 78]]

Saraa was before Dorj, and Bat was before Anu — so they stay that way.


---
