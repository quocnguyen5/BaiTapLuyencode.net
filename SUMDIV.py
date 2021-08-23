T = int(input())
So = []

for i in range(T):
    n = int(input())
    n = abs(n)
    So.append(n)

for i in So:
    TongUoc = 0
    for j in range(1, i + 1):
            if i % j == 0:
                TongUoc += j
    print(TongUoc)
        
         
   

