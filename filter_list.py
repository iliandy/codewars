# https://www.codewars.com/kata/list-filtering/train/python
def filter_list(l):
    # lst = []
    # for item in l:
    #     if (type(item) is int):
    #         lst.append(item)
    # return lst

    return [item for item in l if (type(item) is int)]



l = [1,2,'aasf','1','123',123]
print filter_list(l)
