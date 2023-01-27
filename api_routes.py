import requests

# Everything I want for each book: 
    # book_id --> will pass in 
    # book_ISBN 
    # *author 
    # *title 
    # year_published 
    # cover_path 
    # overview 
    # *author_img_path 



# OPEN LIBRARY API CALL: 

# EXAMPLE OUTPUT FROM CALLING THE FOLLOWING ROUTE: 
# book_request = requests.get(f"https://openlibrary.org/works/OL20531661W.json")

# {"title": "The King of Kindergarten", 
# "key": "/works/OL20531661W", 
# "type": {"key": "/type/work"}, 
# "subjects": ["Children's fiction", "First day of school, fiction", "Kindergarten, fiction", "Schools, fiction"], 
# "authors": [{"author": {"key": "/authors/OL1388283A"}, "type": {"key": "/type/author_role"}}, {"author": {"key": "/authors/OL7324153A"}, "type": {"key": "/type/author_role"}}], 
# "covers": [11222771], 
# "description": {"type": "/type/text", "value": "Starting kindergarten is a big milestone..."}, 


# TEST CODES: 
# King of Kindergarten code for testing is: OL20531661W
# Black is a Rainbow Color code is:"OL27901434M"
# Besos for Baby code is: "OL19987787W"

open_lib_W = "OL20128080W"

# Initial book request from the Open Library Works API: 
book_request = requests.get(f"https://openlibrary.org/works/{open_lib_W}.json")
book_data = book_request.json()


# Get Overview: 
if "description" in book_data:
    overview = book_data["description"]["value"]
else:
    overview = "No overview for this book"


# Get Title 
book_title = book_data["title"]


# Get author(s):
author_path_list = []
# Author data from original JSON dict: 
if "authors" in book_data:
    authors_to_parse = book_data["authors"]
    # Getting list containing author's paths: 
    # if there is more than one author...
    if len(authors_to_parse) > 1:
        for item in authors_to_parse:
            if "author" in item:
                author_path_list.append(item["author"]["key"])
            if "key" in item:
                author_path_list.append(item["key"])
    # if there is one author...
    if len(authors_to_parse) == 1:
        # if "author" in authors_to_parse:
        author_path_list.append(authors_to_parse[0]["author"]["key"])
        # else: 
        #     author_path_list.append(authors_to_parse[0]["key"])
    # if the API JSON dict does not have an author listed...
else:
    author_name = "No author found."

author_names_list = []

if len(author_path_list) >= 1: 
    for path in author_path_list:
        author_request = requests.get(f"https://openlibrary.org{path}.json")
        author_dict = author_request.json()

        if "name" in author_dict:
            author_names_list.append(author_dict["name"])

        elif "personal_name" in author_dict:
            author_names_list.append(author_dict["personal_name"])


# Get Cover Path
cover_id = book_data["covers"][0]
cover_path = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"

# Get ISBN_13: 
isbn_request = requests.get(f"https://openlibrary.org/works/{open_lib_W}/editions.json")
isbn_data = isbn_request.json()

if "entries" in isbn_data:
    book_isbn_13 = int(isbn_data["entries"][-1]["isbn_13"])
else: 
    book_isbn_13 = 0






print(f"Book ISBN: {book_isbn_13}")