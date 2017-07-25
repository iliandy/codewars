# https://www.codewars.com/kata/525f039017c7cd0e1a000a26/train/python
def palindrome_chain_length(n):
    count = 0
    while(str(n) != str(n)[::-1]):
        n = n + int(str(n)[::-1])
        count += 1

    return count


print palindrome_chain_length(87)
