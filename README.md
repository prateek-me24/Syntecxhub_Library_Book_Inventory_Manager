# Syntecxhub_Library_Book_Inventory_Manager
This is a Library Book Inventory Manager Project

# WHAT THIS PROJECT WILL DO
Library Book Inventory Manager can - 
    1. Add a book
    2. Sreach book by TITLE OR AUTHOR
    3. Issue a book
    4. Return a book
    5. Show reports:
        Total books
        Issued books
    6. Save data in a JSON file
    7. Reload data when program starts


# DATA STRUCTURE PLNNING
Each details : 
    id
    title
    author
    is_issued (True / False)

We use :
    dict - like hashmap for fast lookup
    list - when displaying all books
    JSON file - permanent storage