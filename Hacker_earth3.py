'''
solution for a problem .
imp part is to taking the input continously 

'''
n=int(raw_input())
dic={}

for i in range(n):
    line=raw_input().split()
    dic[line[0]]=sum(map(float,line[1:]))/3.0
    
print '%.2f' %  dic[raw_input()]
