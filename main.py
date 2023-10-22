d={}
n=input("Enter a list of words:").split()
for i in n:
    d[i]=d.get(i,0)+1
for i, count in d.items():
    print(f'{i}:{count}')
