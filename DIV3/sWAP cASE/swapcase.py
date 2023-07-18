def swap_case(s):
    return s.swapcase()
    # sn=''
    # alp='abcdefghijklmnopqrstuvwxyz'
    # for c in s:
    #     if c in alp:
    #         sn+=c.upper()
    #     else:
    #         sn+=c.lower()
    # return sn

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
