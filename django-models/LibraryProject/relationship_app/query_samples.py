import os
import django
import sys



sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

#Sample data setup function
def setup_sample_data():
    author = Author.objects.create(name="George Orwell")
    book1 = Book.objects.create(title = "1984", author=author)
    book2 = Book.objects.create(title = "Animal Farm", author=author)

    library = Library.objects.create(name = "City Library")
    library.books.set([book1, book2])

    librarian = Librarian.objects.create(name = "Alice", library=library)



#Query samples
def get_books_by_author(author_name):
    try:
        books = Book.objects.filter(author__name = author_name)
        print(f"Books by {author_name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"No books found for author: {author_name}")


def list_books_in_library(library_name):

    try: 
        library = Library.objects.get(name = library_name)
        for book in library.books.all():
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")

def get_librarians_in_library(library_name):
    try:
        library = Library.objects.get(name =library_name)
        print(f'Librarian for {library.name} is {library.librarian.name}')
    except (Librarian.DoesNotExist, Library.DoesNotExist):
        print(f"No librarian found for library: {library_name}")



if __name__ == "__main__":
    setup_sample_data()
    get_books_by_author("George Orwell")
    list_books_in_library("City Library")
    get_librarians_in_library("City Library")