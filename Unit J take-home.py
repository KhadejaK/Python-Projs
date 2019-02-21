''' 
Khadeja Khalid 
CIS 41A   Spring 2018 
Unit J take-home assignment
'''

class LibraryPatron():
    def __init__(self, name):
        self.name = name
        self.booksCheckedOut = list()
        
    def checkOutBook(self, checkOutLimit, bookTitle):
        if len(self.booksCheckedOut) == checkOutLimit:
            print("Sorry", self.name, "you are at your limit of", checkOutLimit, "books")
        else:
            self.booksCheckedOut.append(bookTitle)
            print(self.name, "has checked out", bookTitle[0])
        
    def returnBook(self, book):
        self.booksCheckedOut.remove(book)
        print(self.name, "has returned", book[0])
        
    def printCheckedOutBooks(self):
        print(self.name, "has the following books checked out:")
        for elm in self.booksCheckedOut:
            print (elm[0])
            
class AdultPatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 4
        
    def checkOutBook(self, book):
        super().checkOutBook(self.checkOutLimit, book)
        
class JuvenilePatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 2
        
    def checkOutBook(self, book):
        if "Juvenile" not in book:
            print("Sorry", self.name, book[0], "is an adult book")
        else:
            super().checkOutBook(self.checkOutLimit, book)
        
#Test Code
book1 = ["Alice in Wonderland", "Juvenile"]
book2 = ["The Cat in the Hat", "Juvenile"]
book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
book4 = ["The Hobbit", "Juvenile"]
book5 = ["The Da Vinci Code", "Adult"]
book6 = ["The Girl with the Dragon Tattoo", "Adult"]s

patron1 = JuvenilePatron("Jimmy")
patron2 = AdultPatron("Sophia")

patron1.checkOutBook(book6)
patron1.checkOutBook(book1)
patron1.checkOutBook(book2)
patron1.printCheckedOutBooks()
patron1.checkOutBook(book3)
patron1.returnBook(book1)
patron1.checkOutBook(book3)
patron1.printCheckedOutBooks()
patron2.checkOutBook(book5)
patron2.checkOutBook(book4)
patron2.printCheckedOutBooks()
        
''' 
Execution results: 

Sorry Jimmy The Girl with the Dragon Tattoo is an adult book
Jimmy has checked out Alice in Wonderland
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out:
Alice in Wonderland
The Cat in the Hat
Sorry Jimmy you are at your limit of 2 books
Jimmy has returned Alice in Wonderland
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out:
The Cat in the Hat
Harry Potter and the Sorcerer's Stone
Sophia has checked out The Da Vinci Code
Sophia has checked out The Hobbit
Sophia has the following books checked out:
The Da Vinci Code
The Hobbit
''' 
