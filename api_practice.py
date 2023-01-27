import requests

# TO GET THE PUBLISH TITLE AND PUBLISH DATE USE THIS URL WITH BOOKS BEFORE THE 
# OPEN LIBRARY CODE: 
    # Example URL: ("https://openlibrary.org/books/{OL27773225M}.json")

# Make a list of all of the open library IDs. Iterate through the list and update
# each URL accordingly to get the data for each book: 


# Everything I want for each book: 
    # book_id 
    # book_ISBN 
    # author 
    # title 
    # year_published 
    # cover_path 
    # overview 
    # author_img_path 



open_lib_id_for_works = "OL20531661W"

#OPEN_LIB_ID NEEDS TO END IN A W FOR THIS TO WORK!!! 
book_request = requests.get(f"https://openlibrary.org/works/{open_lib_id_for_works}.json")
book_data = book_request.json()



print(f"Title: {book_title}")
print(f"Author ID Path: {author_id_path}")


open_lib_id_for_book = "OL20531661M"
book_request_from_book_API = requests.get(f"https://openlibrary.org/books/{open_lib_id_for_book}.json")
publish_date = book_data["publish_date"]
print(publish_date)

# TO GET THE COVER...
    # get the value of the key 'covers' --> 'covers': [9181132] from above ^
    # store that as a variable called cover_id or something and...
    # input that into the following url like so: 
        # f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"




author_id_path = book_data["authors"]["author"]["key"]





# # TO GET THE AUTHOR'S NAME AND IMAGE: 

author_request = requests.get(f"https://openlibrary.org{author_id_path}.json")
author_dict = author_request.json()

author_name = author_dict["personal_name"]
author_img_id = author_dict["photos"][0]

author_image_path = f"https://covers.openlibrary.org/b/id/{author_img_id}-L.jpg"
# if there is not an image add a shadowy image instead



# # AUTHOR --> STILL TRYING TO GET THIS TO WORK. HERE'S WHAT I'M THINKING SO FAR 
# # author_request = requests.get("https://openlibrary.org/authors/{open_lib_id}.json")
# author_request = requests.get("https://openlibrary.org/authors/OL27773225M.json")
# author_data = author_request.json()
# print(author_data)





# MISC. NOTES AND TEST CODE: 

# url = "https://openlibrary.org/api/books?bibkeys=ISBN:0201558025&format=json"

# res = requests.get(url)
# print(res)
# # print(res.keys())
# data = res.json()
# print(data)



## the script tag will need to go in the base HTML file:
# <script src="https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&callback=mycallback"></script>



# a list of ISBNs 
# for each ISBN --> format string for URLs 
# get the responses and JSONify them and then pick out what I want--> get the keys I want
# commit things to database with db.sessions.commit()