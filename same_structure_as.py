# https://www.codewars.com/kata/520446778469526ec0000001
def same_structure_as(lst1, lst2):
    lst1_str = str(lst1)
    lst2_str = str(lst2)

    for ch1, ch2 in zip(lst1_str, lst2_str):
        if ch1.isdigit() and ch2.isdigit():
            continue
        if "'" in lst1_str or "'" in lst2_str:
            break
        if ch1 is not ch2:
            return False
    return True

# solution:
def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2):
                return False
        return True
    else:
        return not isinstance(original, list) and not isinstance(other, list)


print same_structure_as([1,'[',']'], ['[',']',1])   # should be True
