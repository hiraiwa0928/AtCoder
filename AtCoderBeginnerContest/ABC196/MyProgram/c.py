N = input()

if int(N) < 11:
    print(0)
    exit()

keta = len(N)

cnt1 = 0

for i in range(int((keta+1)/2)-1):
    cnt1 += 9*10**i

if keta%2 == 0:
    
    n1 = int(N[:int(len(N)/2)])
    n2 = int(N[int(len(N)/2):])

    num = 10**(int(keta/2)-1)
    cnt2 = 0

    if n1 >= num:
        cnt2 += n1-(num-1)
        if n1 > n2:
            cnt2 -= 1
    
    print(cnt1+cnt2)

else:
    print(cnt1)