'''
k = 3
n = 17
w = 4

17

3 6 9 12

Sn = n/2(2a+(n-1)d) = 2(k) + (w-1)
'''

k,n,w = map(int,input().split())

summ = w/2 *( 2*k + (w-1)*k)

if summ - n < 0:
    print(0) 
else:
    print(int(summ-n))


