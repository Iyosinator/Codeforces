t = int(input())

for i in range(t):
    n = int(input())
    st= input()
    one = st.count("1")
    #print(one)
    zero  = st.count("0")
    #print(zero)
    ans = one * (n - 1) + zero
    print(ans)
