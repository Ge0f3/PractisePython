import sys

def reverse(S,K):
    res = ""
    S=S.replace("-","").upper()[::-1]
    for i in range(0,len(S),K):
        print(S[i:i+K])
        res += S[i:i+K]
        res += "-"
    res = res[::-1]
    return res[1:]


def main():
    print("*****************License Split*****************")
    S="2-4A0r7-4k"
    K=4
    print("The array after License Split {}".format(reverse(S,K)))


if __name__ == '__main__':
    main()