"""请实现一个函数，把字符串 s 中的每个空格替换成"%20"。"""

s = "We are happy."

list_s = list(s)


def replaceSpace( s: str) -> str:
    for i in range(len(list_s)):
        if list_s[i] == ' ':
            list_s[i] = "%20"
    print("".join(list_s))
replaceSpace(s)