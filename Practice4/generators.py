#1
def count(max):
    cnt=0
    while cnt<=max:
        yield cnt**2
        cnt=cnt+1
a=int(input())
res1=count(a)
print("Result of the first task: ")
print(*res1,sep=" ")

#2
def even(max):
    cnt=0
    while cnt<=max:
        if cnt%2==0:
            yield cnt
        cnt=cnt+1
n=int(input())
res2=even(n)
print("Result of the second task: ")
print(*res2,sep=" ")


#3
class MyIterator:
    def __init__(self,end):
        self.end=end
        self.start=0
    def __iter__(self):
        self.current=0
        return self
    def __next__(self):
        while(self.current<= self.end):
            num = self.current
            self.current += 1
            if num % 3 == 0 and num % 4 == 0:
                return num
        raise StopIteration
n=int(input())
res3=MyIterator(n)
print("Result of the third task: ")
print(*res3,sep=" ")

        
#4
def new_generator(a,b):
    while a<=b:
        yield a**2
        a+=1
n1,n2=map(int,input().split())
res4=new_generator(n1,n2)
print("Result of the fourth task: ")
print(*res4, sep=" ")

#5
def myreverse(num):
    while num>=0:
        yield num
        num-=1
n5=int(input())
res5=myreverse(n5)
print("Result of the fourth task: ")
print(*res5, sep=" ")