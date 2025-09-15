## CREATE
# Import
- >>> from bookshelf.models import Book

# Create book instance
- >>> book = Book.objects.create(title="1948", author="George Orwell", publication_year = 1949)
- >>> print(book.title, book.author, book.publication_year)

# Output: 
# 1984 George Orwell 1949



## RETRIEVE
 >>> book = Book.objects.get(title="1984")
- >>> print(book.title, book.author, book.publication_year)

# Output
# 1984 George Orwell 1949




## UPDATE
# Update book title
- >>> book.title = "Nineteen Eighty-Four"
- >>> book.save()

# Verify update
- >>> print(book.tile)

## Output: 
# Nineteen Eighty-Four




## DELETE
- >>> book.delete()
# (1, {'bookshelf.Book': 1})

# Confirm Delete
- >>> Book.objects.all()

# Results
# <QuerySet []>