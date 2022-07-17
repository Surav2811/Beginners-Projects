# Student can borrow from a list of the books

#Student and Library are different classes

class Library :
    def __init__(self,listOfBooks):
        self.books = listOfBooks
        
    def displayAvaBooks (self):
        print ("Books that are present in library are : ")
        for book in self.books:
            print("* "+book)
        print ("\n")
            
            
    def issueBook (self,bookName):
        self.books.remove(bookName)
        
    def returnBook (self,bookName):
        self.books.append(bookName)
        print ("Thanks for returning the books. Hope you enjoyed reading it.")
    


if __name__=='__main__':
    
    centralLibrary = Library (["algorithms","oops","dld","database","fiction"])
    
    print ("\t\t\tWelcome to the Central Library!")

    while True:
        
        print ('''
1. Show all the books avaliable.
2. Issue a book.
3. Add or return a book.
4. Exit from the library menu.
5. Check the details of the books issued by the Student.\n''')
        choice = input ("Please enter your choice number: ")
            
        if choice == '1':
            centralLibrary.displayAvaBooks()
            
        elif choice == '2':
            issue = input ("Please enter the name of the book you want to be issued: ").lower()
            if issue in centralLibrary.books:
                print ("You have been issued the book {}. Please remember to return it ontime (30 days).".format(issue))
                centralLibrary.issueBook(issue)
                # student1.issuedBooks(issue)
            else:
                print("This book is not available.")
                
        elif choice == '3':
            returned = input ("Please enter the name of the book you want to return or add to the library: ").lower()
            if returned in centralLibrary.books:
                print("The book is already present in the library.")
            elif returned is not str:
                print ("The name you have entered is incorrect. Please enter the correct name.")
                continue
            days = int (input ("Please enter the time in which book has been returned: "))
            if days > 30:
                print (f"Please pay a fine of {(days-30)*10}")
                
            else:
                centralLibrary.returnBook(returned)
                # student1.issuedBooks(returned)
                print ("Your book has been added to the library")
        # elif choice == '4':
        #     student1.display()        
        elif choice == '4':
            print ("Thank you for visiting Central Library")
            quit()
        
        else:
            print ("Please enter a valid choice.")