

def quicksort(a, lo=None, hi=None):
  """  Does in-place quicksort of array

  >>> a = [ 7, 3, 4, -1, 8, 0, 5, 9, 2]
  >>> quicksort(a)
  >>> a
  [-1, 0, 2, 3, 4, 5, 7, 8, 9]
  """
  
  lo = 0 if lo is None else lo
  hi = len(a) - 1 if hi is None else hi

  if lo < hi:
    p = partition(a, lo, hi)
    quicksort(a, lo, p - 1)
    quicksort(a, p, hi)

def partition(a, lo, hi):
  # Choose a partition value
  p = a[hi]
  i = lo
  j = lo
  while j <= hi:
    if a[j] < p:
      swap(a, i, j)
      i += 1
    j += 1
  swap(a, i, hi)
  return i

def swap(a, i, j):
  if i != j:
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

if __name__ == "__main__":
    import doctest
    doctest.testmod()

