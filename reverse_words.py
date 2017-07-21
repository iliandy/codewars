# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

def reverse_words(str):
    # str_lst = str.split(" ")
    # rev_str_lst = [wrd[::-1] for wrd in str_lst]
    # return " ".join(rev_str_lst)

    return " ".join([wrd[::-1] for wrd in str.split(" ")])

print reverse_words("This is an example!")
