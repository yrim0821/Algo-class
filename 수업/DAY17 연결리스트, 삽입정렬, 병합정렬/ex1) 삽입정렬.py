a = [9, 7, 6, 4, 3, 1 ,0]

for next in range(1,len(a)):  # index=0 은 정렬되어 있다고 보고, index=1부터 시작한다
    key = a[next]  # 정렬시켜야 하는 애
    i = next-1  # 정렬시켜야 하는 애  앞부터, 비교한다
    while i >= 0 and a[i] > key:  # 인덱스가 유효하고, 비교값>들어오고 싶은 애(=자리 바꿔야하는 동안)
        a[i+1] = a[i]  # 비교값보다 한 칸 뒤 자리에, 비교값 넣어줌
        i = i-1  # 반복하다가
    a[i+1] = key  # 비교값 < 들어오고 싶은애 되면, 자리를 찾았으니 넣어줌

print(a)






