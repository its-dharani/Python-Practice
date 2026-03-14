def swap_case(s):
    swapped=[]
    for i in s:
        if i.islower():
            swapped.append(i.upper())
        elif i.isupper():
            swapped.append(i.lower())
        else:
            swapped.append(i)
    r="".join(swapped)
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)