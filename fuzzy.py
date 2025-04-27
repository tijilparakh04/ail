A = dict()
B = dict()

n = int(input("enter the number of entries: "))
print("For A: ")
A = {input("Enter key: "): float(input("Enter value: ")) for _ in range(n)}
print("\nFor A: ")
B = {input("Enter key: "): float(input("Enter value: ")) for _ in range(n)}

print("\nFuzzy set A: ", A)
print("\nFuzzy Set B: ", B)

def union(A,B):
  Y = dict()
  for A_key, B_key in zip(A,B):
    A_value = A[A_key]
    B_value = B[B_key]

    if A_value > B_value:
      Y[A_key] = A_value
    else:
      Y[B_key] = B_value
  return Y

print("\nUnion of A and B: ", union(A,B))

def intersection(A,B):
  X = dict()
  for ak, bk in zip(A,B):
    av = A[ak]
    bv = B[bk]

    if av<bv:
      X[ak] = av
    else:
      X[bk] = bv
  
  return X

print("\nIntersection of A and B: ", intersection(A,B))

def complement(A):
  Z = dict()

  for ak in A:
    av = A[ak]
    Z[ak] = 1- av
  
  return Z

print("\nComplement of A: ", complement(A))

def is_subset(A, B):
  return all(A.get(k,0) <= B.get(k,0) for k in A)

print("\nIs A a subset of B? ", is_subset(A,B))

def de_morgan_law_check(A,B):
  union_complement = complement(union(A,B))
  intersection_complement = intersection(complement(A), complement(B))

  return union_complement == intersection_complement

print("\nDoes De Morgan's Law hold for A and B? ", de_morgan_law_check(A,B))