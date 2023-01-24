import requests

# TO GET THE PUBLISH TITLE AND PUBLISH DATE USE THIS URL WITH BOOKS BEFORE THE 
# OPEN LIBRARY CODE: 
    # Example URL: ("https://openlibrary.org/books/{OL27773225M}.json")

# Make a list of all of the open library IDs. Iterate through the list and update
# each URL accordingly to get the data for each book: 

book_request = requests.get("https://openlibrary.org/books/{open_lib_id}.json")
book_data = book_request.json()
book_title = book_data["title"]
publish_date = book_data["publish_date"]
cover_id = book_data["covers"][0]
print(book_title)
print(publish_date)

# TO GET THE COVER...
    # get the value of the key 'covers' --> 'covers': [9181132] from above ^
    # store that as a variable called cover_id or something and...
    # input that into the following url like so: 
        # f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"

cover_path = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
print(cover_path)




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