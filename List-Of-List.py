def is_empty_LOL(X):
    return X == []

def tail_list(c):
    if not (is_empty_LOL(c)):
        return c[1:]

def head_list(c):
    if not (is_empty_LOL(c)):
        return c[:-1]

def last_list(s):
    if not (is_empty_LOL(s)):
        return s[-1:]

def first_List(a):
    if not(is_empty_LOL(a)):
        return a[0]

def NBelementlist(J):
    if J == []:
        return 0
    else:
        return 1+NBelementlist(tail_list(J)) 
    
def isAtom (a):
    return type(a)!=list

def isList (a):
    return not isAtom(a)

def konso(L,S):
    if is_empty_LOL(S):
        return [L]
    else:
        return [L]+S

def konsi(L,S):
    if is_empty_LOL(S):
        return [L]
    else:
        return [S]+L

def IsEqs(S1,S2):
    if is_empty_LOL(S1) and is_empty_LOL(S2):
        return True
    elif not is_empty_LOL(S1) and is_empty_LOL(S2):
        return False
    elif is_empty_LOL(S1) and not is_empty_LOL(S2):
        return False
    elif not is_empty_LOL(S1) and not is_empty_LOL(S2):
        if isAtom(first_List(S1)) and isAtom (first_List(S2)):
            return first_List(S1)==first_List(S2) and IsEqs (tail_list(S1),tail_list(S2))
        elif isList(first_List(S1)) and isList (first_List(S2)):
            return IsEqs(first_List(S1),first_List(S2)) and IsEqs (tail_list(S1),tail_list(S2))
        else:
            return False


def IsMember(A,M):
    print(M)
    if is_empty_LOL (M):
        return False
    else:
        if isAtom(first_List(M)):
            if A == first_List(M):
                return True
            else:
                return IsMember(A, tail_list(M))
        elif isList (first_List(M)):
            return IsMember(A, first_List(M)) or IsMember(A, tail_list(M))

def IsMemberLS(L,S):
    if is_empty_LOL(L) and is_empty_LOL(S):
        return True
    elif not is_empty_LOL(L) and is_empty_LOL(S):
        return False
    elif is_empty_LOL(L) and not is_empty_LOL(S):
        return False
    elif not is_empty_LOL(L) and not is_empty_LOL(S):
        if (isAtom(first_List(S))) :
            if L == head_list(S):
                return True
            else: 
                return IsMemberLS(L, tail_list(S))
        else:
            if IsEqs(L,first_List(S)): 
                return True
            else:
                return IsMemberLS(L,tail_list(S))

def Rember(a,L):
    print(L)
    if is_empty_LOL(L):
        return L
    else:
        if isList(first_List(L)):
            if first_List(L) == a:
                return tail_list(L)
            else:
                return konso(Rember(a,first_List(L)), Rember(a,tail_list(L)))
        else:
            if first_List(L) == a:
                return tail_list(L)
            else:
                return konso(first_List(L), Rember(a,tail_list(L))) 

def Max2(a,b):
    if a>=b:return a
    else: return b

def Max(S):
    if NBelementlist(S)==1:
        if isAtom(first_List(S)):
            return first_List(S)
        else:
            return Max(first_List(S))
    else:
        if isAtom(first_List(S)):
            return Max2(first_List(S), Max(tail_list(S)))
        else:
            return Max2(Max(first_List(S)),Max(tail_list(S)))
            

