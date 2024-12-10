# WAP to check the given year is leap year or not:-
year=int(input("Enter year: "))
if year%4==0:
    print("It is leap year:")
else:
    print("It is not leap year")

# A program that calculates the factorial of a given no:-
num=int(input("Enter any Number: "))
fact=num
if num==1 or num==0:
        print("Enter another no: ")
else:
    for var in range(num-1,1,-1):
        fact*=var
    print("Factoril of",num,"is: ",fact)
# 2nd way:- by recursion
def fact(n):
    if n==1 or n==0:
        return 1
    return fact(n-1)*n
print(fact(int(input("Enter the no: "))))

# pelendrom or not:
word=(input("Enter: "))
rword=word[::-1]
if word==rword:
    print("The word",word,"is Pelindrome")
else:
    print(word,"is not Pelindrome")

# sort the list in assendn and descending order:-
list=[2,4,6,9,8,3,5]
list.sort()
print("Sorted list in Ascending order",list)
list.reverse()
print("Sorted list in Descending order",list)
