#code
t=int(input())
while t>0:
    st=input();
    strings=list();
    strings=st.split();
    ans=0
    prev=0
    for i in range(0,len(strings)):
        if(i==0):
            for c in strings[0]:
                n=ord(c)-ord("0")
                ans=ans+n
        else:
            for c in strings[i]:
                n=ord(c)-ord("0")
                ans=ans-n
        
    if(ans==0 and len(strings[1])==len(strings[0])):
        print("YES")
    else:
        print("NO")
    t=t-1
