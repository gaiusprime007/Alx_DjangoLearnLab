# Create a Book instance

# Import
- >>> from bookshelf.models import Book

# Create book instance
- >>> book = Book.objects.create(title="1948", author="George Orwell", publication_year = 1949)
- >>> print(book.title, book.author, book.publication_year)

# Output: 
# 1984 George Orwell 1949
