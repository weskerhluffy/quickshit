'''
Created on 19/05/2018

@author: ernesto
'''
# XXX: https://www.hackerrank.com/contests/learna/challenges/quicksort3/problem

def swap(a,i,j):
    a[i],a[j]=a[j],a[i]

def print_a(a):
    print(" ".join(map(str,a)))
    
def quickshit(a,lo,hi):
    if lo<hi:
        p=a[hi]
        i=lo-1
        for j in range(lo,len(a)-1):
            if a[j]<p:
                i+=1
                swap(a,i,j)
        swap(a,i+1,hi)
        print_a(a)
        quickshit(a,lo,i)
        quickshit(a,i+2,hi)

n=int(input())
a=[int(x) for x in input().strip().split(" ")]
quickshit(a,0,len(a)-1)

