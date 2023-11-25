def merge_sort(A, p, q, r):
  if len(A) <= 1:
    return A
  n1 = q - p
  n2 = r - q
  L = [0] * n1
  R = [0] * n2
  for a in range(n1):
    L[a] = A[p+a]
  for b in range(n2):
    R[b] = A[q+b]
  L = merge_sort(L, 0, len(L)//2, len(L))
  R = merge_sort(R, 0, len(R)//2, len(R))
  i = 0
  j = 0
  k = p
  while i < n1 and j < n2:
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
    k += 1
  while i < n1:
    A[k] = L[i]
    i+=1
    k+=1
  while j < n2:
    A[k] = R[j]
    j += 1
    k+=1
  return A

systemIn = [int(l) for l in input().split(' ')]
print(merge_sort(systemIn, 0, len(systemIn)//2, len(systemIn)))