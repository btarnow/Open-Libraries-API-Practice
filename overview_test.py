import requests 
import pprint 

books_database = {}

book_OLIDs_list = ["OL20914137W", "OL25074818W", "OL22020948W", "OL27139917W",
                   "OL26585018W", "OL21183636W", "OL19635091W", "OL20639677W", 
                   "OL27137338W", "OL20531661W", "OL25070735W", "OL39666203M", 
                   "OL24141019W", "OL20660371W", "OL46525616M", "OL24348919W", 
                   "OL46525603M", "OL19406W", "OL19987787W", "OL26886570M", 
                   "OL20055629W", "OL20128080W", "OL20128080W", "OL34975354M", 
                   "OL29531064M", "OL19743931W", "OL46525609M", "OL25873929W", 
                   "OL24327244W", "OL46525611M", "OL46525610M", "OL21874814W", 
                   "OL28716700M", "OL35289538M", "OL19667684W", "OL17072538M", 
                   "OL26977532M"]


for book_OLID in book_OLIDs_list:
    ind_book_dict = {}
    book_request = requests.get(f"https://openlibrary.org/works/{book_OLID}.json")
    book_data = book_request.json()
    print(f"This is the loop for book_OLID: {book_OLID}")

    if "description" in book_data:
        if "value" in book_data["description"]:
            overview = book_data["description"]["value"]
        
        else:
            overview = book_data["description"]
        
    else:
        overview = "No overview for this book"
        print(overview)

    ind_book_dict["Overview"] = overview

    books_database[book_OLID]= ind_book_dict 

pprint.pprint(books_database)
    


#     books_database[book_OLID]= ind_book_dict 

# pprint.pprint(books_database)