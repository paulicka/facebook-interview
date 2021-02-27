
def mergesort(a, lo = None, hi = None):
  assert(isinstance(a, list))
  lo = 0 if lo is None else lo
  hi = len(a) if hi is None else hi

  r = a
  if hi - lo > 1:
    mid = (hi + lo) // 2
    # splits = a[lo:mid], a[mid:hi]
    # r = merge(*map(mergesort, splits))
    r = merge(mergesort(a[lo:mid]), mergesort(a[mid:hi]))
    
  return r
  
def merge(a, b):
  la = len(a)
  lb = len(b)
  l = la + lb
  r = [0] * l

  i = 0
  j = 0
  k = 0
  while k < l:
    va = a[i] if i < la else None
    vb = b[j] if j < lb else None

    if va is None or (vb is not None and vb < va):
      r[k] = vb
      j += 1
    elif vb is None or va < vb:
      r[k] = va
      i += 1
    
    k += 1
  
  return r
