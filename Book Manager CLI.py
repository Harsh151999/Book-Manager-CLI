# Define the Book class with name, rate, price, author, and genre
class Book:
    def __init__(self, name, rate, price, author, genre):
        self.name = name
        self.rate = rate
        self.price = price
        self.author = author
        self.genre = genre

    def display_info(self):
        return (
            f"Book Name: {self.name}\n"
            f"Author: {self.author}\n"
            f"Genre: {self.genre}\n"
            f"Rate: {self.rate}\n"
            f"Price: ${self.price}\n"
        )

# Welcome message
print("Welcome to BOOK READER\n")

# Function to create a new book (non-interactive version)
def create_book(name, author, genre, rate, price):
    return Book(name, rate, price, author, genre)

# Function to search for books by genre or author
def search_books(books, keyword):
    print(f"\nSearch results for '{keyword}':")
    found = False
    for book in books:
        if keyword.lower() in book.author.lower() or keyword.lower() in book.genre.lower():
            print(book.display_info())
            print("-" * 40)
            found = True
    if not found:
        print("No matching books found.\n")

# Creating initial book objects
book1 = Book("The Great Gatsby", 4.5, 10.99, "F. Scott Fitzgerald", "Classic")
book2 = Book("1984", 4.8, 8.99, "George Orwell", "Dystopian")
book3 = Book("To Kill a Mockingbird", 4.7, 12.99, "Harper Lee", "Historical Fiction")
book4 = Book("The Hobbit", 4.6, 9.99, "J.R.R. Tolkien", "Fantasy")
book5 = Book("Pride and Prejudice", 4.4, 7.99, "Jane Austen", "Romance")

# Store books in a list
books = [book1, book2, book3, book4, book5]

# Simulate adding a new book (non-interactive)
# You can change the parameters here to simulate different inputs
add_more = True
if add_more:
    simulated_book = create_book("Clean Code", "Robert C. Martin", "Programming", 4.9, 29.99)
    books.append(simulated_book)

# Simulate searching for a book
search = True
if search:
    keyword = "Programming"  # You can change this keyword to test different searches
    search_books(books, keyword)

# Displaying book information
print("\nAll Available Books:")
for book in books:
    print(book.display_info())
    print("-" * 40)
