import requests 

open_lib_W = "OL26977532M"
author_name = ""

book_request = requests.get(f"https://openlibrary.org/works/{open_lib_W}.json")
book_data = book_request.json()

# An empty list to store the author(s) route paths: 
author_path_list = []

if "authors" in book_data:
    # Getting list containing author's paths: 
    authors_to_parse = book_data["authors"]
    print(f"authors to parse: {authors_to_parse}")
    # if there is one author...
    if len(authors_to_parse) == 1:
        # if "author" in authors_to_parse:
        #     author_path_list.append(authors_to_parse[0]["author"]["key"])
        if "key" in authors_to_parse[0]: 
            author_path_list.append(authors_to_parse[0]["key"])
            print(f"Now the author_path_list is {author_path_list}")
    # if there is more than one author...
    if len(authors_to_parse) > 1:
        for item in authors_to_parse:
            if "author" in item:
                author_path_list.append(item["author"]["key"])
            if "key" in item:
                author_path_list.append(item["key"])

print(f"Author Path List: {author_path_list}")

    # if the API JSON dict does not have an author listed...
# else:
#     author_name = "No author found."
    


print(author_path_list)


# THIS GETS THE FIRST AUTHOR LISTED... WILL NEED TO DO A LOOP THROUGH THE LIST 
# TO GET ALL OF THE AUTHORS FOR A CERTAIN BOOK IN CRUD FUNCTION: 
# I have if the length of this list is greater than 1 because if no author is 
# found and append to this list, author is already assigned above to "no author found"

author_names_list = []

if len(author_path_list) >= 1: 
    for path in author_path_list:
        author_request = requests.get(f"https://openlibrary.org{path}.json")
        author_dict = author_request.json()

        if "name" in author_dict:
            author_names_list.append(author_dict["name"])

        elif "personal_name" in author_dict:
            author_names_list.append(author_dict["personal_name"])

print(author_names_list)

# How can I store the correct picture with the correct author? 
        # if "photos" in author_dict:
        #     author_img_id = author_dict["photos"]
        #     author_image_path = f"https://covers.openlibrary.org/b/id/{author_img_id}-L.jpg"
        
        # if "photos" not in author_dict:
        #     author_image_path = "/no_photo.jpeg"







#again-- what happens if there is no photo in the database?
# author_img_id = author_dict["photos"][0]

# author_image_path = f"https://covers.openlibrary.org/b/id/{author_img_id}-L.jpg"