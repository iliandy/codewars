# https://www.codewars.com/kata/520446778469526ec0000001
def same_structure_as(lst1, lst2):
    for val1, val2 in zip(lst1, lst2):
        if isinstance(val1, list) is not isinstance(val2, list):
            return False
        elif isinstance(val1, list) and isinstance(val2, list):
            # for val
            #     if isinstance(val1, list) is not isinstance(val2, list):
            #         return False
            pass
    return True

print same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
print same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

print same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
print same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

print same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

print same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )


print sum(map(len, [ [ [ ], [ ] ] ]))
