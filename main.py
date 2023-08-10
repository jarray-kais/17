#1/ Countdown :Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
T=[]
def decompteur(i):
    
    for j in range(i,-1,-1):
        T.append(j)
k=int(input("entrer la valeur :"))
decompteur(k)
print(f"countdown {k} should return {T}")
#2/ Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def Print_and_return(T):
    print(T[0])
    return T[1]
print(Print_and_return([1,2]))
#3/ First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
T=[1,2,3,4,5]
def first_plus_lentgh():
    k=T[0]+len(T)
    return k
print(first_plus_lentgh())
#4/Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(val=int(input("entrer la lentgh de list :"))):
    T=[]
    for s in range(0,val+1):
            i= int(input("entrer les valeurs du tableaux:"))
            T.append(i)
    print(T)
    value_greater=[]
    for k in range(0,len(T)):
            if T[k]>=T[2]:
                value_greater.append(T[k])
#return condition
    if len(value_greater)<2:
            return ("false")
    else:
            return(f"values greater than {T[2]} est{value_greater}")
print(values_greater_than_second())

#5/This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
val=int(input("entrer la lentgh de list :"))
i=int(input("entrer l'element de list :"))
def length_value(val,i):
    T=[]
    for s in range(0,val+1):
                T.append(i)
    return T
print(length_value(val,i))