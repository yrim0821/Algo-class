Data = list(map(int, input().split()))
visited = [0] * 10

def GetSome(k, sum):
    if sum==10 :
        for i in range(10) :
            if visited[i]: print("%d " %Data[i], end = " ")
        print()
        return
    if k >=10 or sum > 10 : return

    visited[k] = 1
    GetSome(k+1, Data[k] + sum)
    visited[k] = 0
    GetSome(k+1,  sum)

GetSome(0,0)