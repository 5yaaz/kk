def main():
   a=input("")
   n=0
   for i in range(2,a//2+1):
     if(a%i==0):
        n=n+1
   if(n<=0):
    print("Yes")
   else:
    print("No")
if __name__ == '__main__':
    main()
