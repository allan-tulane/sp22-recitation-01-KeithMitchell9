"""
CMPS 2200  Recitation 1
"""
### the only imports needed are here
import tabulate
import time

print("WHY DOES NOTHING PRINT")

def linear_search(mylist, key):
    """ done. """
    for i, v in enumerate(mylist):
        if v == key:
            return i
    return -1


def tes_linear_search():
    """ done. """
    assert linear_search([1, 2, 3, 4, 5], 5) == 4
    assert linear_search([1, 2, 3, 4, 5], 1) == 0
    assert linear_search([1, 2, 3, 4, 5], 6) == -1


def binary_search(mylist, key):
    """ done. """
    return _binary_search(mylist, key, 0, len(mylist) - 1)


def _binary_search(mylist, key, left, right):
    if right >= left:
        mid = (right + left) // 2
        if mylist[mid] == key:
            return mid
        elif mylist[mid] > key:
            mid -= 1
            return _binary_search(mylist, key, left, mid)
        else:
            mid += 1
            return _binary_search(mylist, key, mid, right)
    else:
        return -1


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 0) == -1
    assert binary_search([1, 2, 3, 4, 5], 4) == 3


def time_search(search_fn, mylist, key):
    start_time = time.time() * 1000
    search_fn(mylist, key)
    finish_time = time.time() * 1000
    return finish_time - start_time


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
    mylist = []
    for n in sizes:
        tlist = list(range(int(n)))
        linsearch = time_search(linear_search, tlist, -1)
        binsearch = time_search(binary_search, tlist, -1)
        x = (n, linsearch, binsearch)
        mylist.append(x)
    return mylist


def print_results(results):
    print(
        tabulate.tabulate(results,
                          headers=['n', 'linear', 'binary'],
                          floatfmt=".3f",
                          tablefmt="github"))

def test_print_results():
    compare = test_compare_search()
    print_results(compare)

def test_compare_search():
    res = compare_search(sizes=[10, 100])
    print(res)
    assert res[0][0] == 10
    assert res[1][0] == 100
    assert res[0][1] < 1
    assert res[1][1] < 1
