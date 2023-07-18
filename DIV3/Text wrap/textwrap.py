import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    s = wrapper.fill(string)
    # s=''
    # for i in range(len(string)):
    #     s+=string[i]
    #     if (i+1)%max_width==0:
    #         s+='\n'
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
