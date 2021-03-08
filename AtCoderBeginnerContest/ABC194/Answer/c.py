if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    
    dic = {}

    for i in range(len(a)):
        if a[i] in dic.keys():
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1
    
    key = list(dic.keys())

    ans = 0

    for i in range(len(key)):
        for j in range(i+1, len(key)):
            ans += (key[j] - key[i])**2 * (dic[key[i]] * dic[key[j]])
    
    print(ans)