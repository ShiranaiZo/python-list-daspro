#3z List Function:
#
# 1. Konso
# 2. Konsi
# 3. is empty
# 4. head
# 5. tail
# 6. NB element
# 7. is one element
# 8. is member
# 9. first element
# 10. last element
# 11. copy list
# 12. inverse
# 13. concat

# 1. Konso
def konso(S, L):
    if L==[]:
        return [S]
    else:
        return [S]+L

# 2. Konsi
def konsi(S, L):
    if L==[]:
        return [S]
    else:
        return L+[S] 
    
# 3. is empty
def is_empty(S):
    return S == []

# 4. head
def head(S):
    return S[:-1]

# 5. tail 
def tail(S):
    return S[1:]

# 6. NB element
def NB_element(S):
    if is_empty(S):
        return 0
    else:
        return NB_element(tail(S)) + 1
    
# 7. is one element 
def is_one_element(L):
    if not(is_empty(L)):
        return NB_element(L)==1
    
# 8. is member
def is_member(L, S):
    if is_empty(L):
        return False
    else:
        if first_element(L) == S:
            return True
        else:
            return is_member(tail(L, S))

# 9. first element
def first_element(L):
    return L[0]

# 10. last element
def last_element(L):
    return L[-1]

# 11. Copy List
def copy_List(L):
    if is_empty(L):
        return []
    else:
        return konso(first_element(L), copy_List(tail(L)))
    
# 12. Inverse
def inverse(L):
    if is_empty(L):
        return []
    else:
        return konsi(first_element(L), inverse(tail(L)))
    
# 13. Concat
def concat(L1, L2):
    if is_empty(L1):
        return L2
    else:
        return konso(first_element(L1), concat(tail(L1), L2))

L1 = [5,6,7,8,1]
L2 = [1,2,4,5,9]
S = 5

print(konso(S, L1))
print(konsi(S, L1))
print(is_empty([]))
print(head(L1))
print(tail(L1))
print(NB_element(L1))
print(is_one_element([S]))
print(is_member(L1, S))
print(first_element(L1))
print(last_element(L1))
print(copy_List(L1))
print(inverse(L1))
print(concat(L1, L2))
    