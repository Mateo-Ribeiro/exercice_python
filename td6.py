#exercice 1
def say_nb_one_to_three():
    nb=0
    while nb not in [1,2,3]:
        nb=int(input("say a number between 1 and 3. "))

#exercice 2
def ten_to_twenty():
    nb=int(input("choose a number between 10 adn 20: "))
    while not(10<=nb<=20):
        if nb<10:
            print("Higher")
        else:
            print("Lower")
        nb=int(input("choose a number between 10 adn 20: "))

#exercice 3
def ten_next_nb_v1(nb):
    for i in range(nb+1,nb+11):
        print(i)

def ten_next_nb_v2(nb):
    nb_lim=nb+10
    while nb_lim>nb:
        nb+=1
        print(nb)

#exercice 4
def sum_whole_nb_v1():
    nb=-1
    sum=0
    while nb!=0:
        nb=int(input("choose a whole number: "))
        sum+=nb
    return sum

#exercice 5
def sum_whole_nb_v2():
    nb=-1
    l_nb=[]
    while nb!=0:
        nb=int(input("choose a whole number: "))
        l_nb.append(nb)
    sum=0
    for i in l_nb:
        sum+=i
    return sum

#exercice 6
def simple_list_v1():
    for i in ["Python","Javascript","Java","PHP","C++","Cobol"]:
        print(i)

def simple_list_v2():
    list = ["Python", "Javascript", "Java", "PHP", "C++", "Cobol"]
    while list != []:
        print(list.pop(0))

#exercice 7
def max_v1():
    mn=int(input("entrez nombre 1"))
    for i in range(2,21):
        nb=int(input(f"entrez nombre {i}"))
        if mn<nb:
            mn=nb
    print(f"le plus grand nombre est {mn}")

#exercice 8
def max_v2():
    mn=int(input("entrez nombre 1: "))
    pos=1
    for i in range(2,21):
        nb=int(input(f"entrez nombre {i}: "))
        if mn<nb:
            mn=nb
            pos=i
    print(f"le plus grand nombre est {mn} en position {pos}")