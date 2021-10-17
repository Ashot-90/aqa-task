# aqa-task

### Here, please find 4 types of solutions for the provided task.
merge_1 -> Uses built-in 'sorted' function (Works for initially non-sorted inputs as well).\
merge_2 -> Uses built-in 'SortedList' container (Works for initially non-sorted inputs as well).\
merge_3 -> Uses my own version of SortedList implementation (Works for initially non-sorted inputs as well).\
merge_4 -> Uses my own implementation of heap.

### To run these solutions please install all requirements
`pip3 install -r requirements.txt`

### Testing
Use `pytest -s -v test.py` command to run unit tests\
It prints performance measurements as well for all implemented solutions as well as built-in 'heapq.merge'


### Summary
The fastest working solution is built-in 'heapq.merge'
Below are solutions sorted by working speeds (fastest -> slowest)
##### 1. Built-in 'heapq.merge' (~4K ns)
##### 2. Built-in 'sorted' (~100K ns)
##### 3. Built-in 'SortedList' (~100K ns)
##### 4. Own 'SortedList' (4M ns)
##### 5. Own 'heap' (56M ns)

### P.S.
I have not tried to re-invent the wheel, but just tried to show my Python and research skills a little.
To be honest, I've never used heap sort algorithm during last >9 years of my experience as QA automation engineer,
and definitely such kind of algorithmic problem solving skills are not one of my strongest ones.\
In spite of that I have stronger QE specific skills, which I'll be glad to introduce you during the call.

### References
https://medium.com/outco/how-to-merge-k-sorted-arrays-c35d87aa298e \
https://www.tutorialspoint.com/merge-k-sorted-lists-in-python \
https://hg.python.org/cpython/file/default/Lib/heapq.py#l314
