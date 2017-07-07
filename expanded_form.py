# https://www.codewars.com/kata/write-number-in-expanded-form/train/python
def expanded_form(num):
    num_str = str(num)
    num_lst = [str(int(num_str[i]) * 10**(len(num_str) - 1 - i)) for i in range(len(num_str)) if num_str[i] != "0"]

    # num_lst = []
    # for i in range(len(num_str)):
    #     if num_str[i] != "0":
    #         num_lst.append(str(int(num_str[i]) * 10**(len(num_str) - 1 - i)))

    return " + ".join(num_lst)

print expanded_form(70304)
