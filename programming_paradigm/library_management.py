class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.__is_checked_out = False
    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
    def check_out_book(self):
        if self.__is_checked_out:
            return False
        self.__is_checked_out = True
        return True
    
    def is_checked_out(self):
        return self.__is_checked_out
    
    
class Library:
    def __init__(self):
        self.__books = []
    
    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self,title):
        for book in self.__books:
            if book.title == title:
               return book.check_out_book()
        return False
        
    def return_book(self,title):
        for book in self.__books:
            if book.title == title:
                return book.return_book()
        return False    

    def list_available_books(self):
        available_books = []
        for book in self.__books:
            if not book.is_checked_out():
                available_books.append(book.title)
        print(*available_books,sep=',')       
