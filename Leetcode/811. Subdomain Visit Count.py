def subdomainVisits(cpdomains):
    dict = {}
    arr = []
    for i in cpdomains:
        k = i.split(" ")
        print(k)
        s = k[1].split(",")
        arr.append(s)
    print(arr)
subdomainVisits([["9001 discuss.leetcode.com"]])