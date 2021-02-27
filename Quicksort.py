

def quicksort(a, lo=None, hi=None):
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

