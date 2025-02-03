import json
#exercice 1
dewey=("Computer science, information and general works","Philosophy and psychology","Religion","Social sciences","Language","Pure science","Technology","Arts and recreation","Literature","History and geography")
def dewey_giver():
    ref=""
    verif="0123456789"
    while True:
        ref=input("enter a reference: ")
        if ref=="stop":
            break
        elif len(ref)!=3 or (ref[0] not in verif or ref[1] not in verif or ref[2] not in verif):
            print("invalid reference")
        else:
            print(f"({ref[0]}, {dewey[int(ref[0])]})")

#exercice 2
def sort_by_sale(to_sort):
    return to_sort["sold_copies"]
def ranking():
    books=[]
    when_stop="N"
    while when_stop!="Y":
        title=input("what is the title of the book? ")
        writer=input("what is the writer of the book? ")
        sold_copies=int(input("how many copies were sold? "))
        genre=input("what is the genre of the book? ")
        books.append({"title":title,"writer":writer,"sold_copies":sold_copies,"genre":genre})
        when_stop=input("Do you wish to stop? (Y/N): ")
    books.sort(key=sort_by_sale,reverse=True)
    i=1
    for book in books:
        book["rank"]=i
        i+=1
    with open("td8_top_books_2021.json","w") as outfile:
        json.dump(books,outfile)
    with open("td8_top_books_2021.json","r") as outfile:
        books_change=json.load(outfile)
    last_name=writer.replace(" ","").split(".")[-1].upper()
    for book in books_change:
        book["classification"]=f"{dewey.index(book["genre"])}00-{last_name[:3]}"
    with open("td8_top_books_2021.json","w") as outfile:
        json.dump(books_change,outfile)
    books_genre={}
    for book in books:
        if book["genre"] not in books_genre:
            books_genre[book["genre"]]=book["sold_copies"]
        else:
            books_genre[book["genre"]]+=book["sold_copies"]
    print(books_change)
    print(books_genre)