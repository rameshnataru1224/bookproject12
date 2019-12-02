"""
Author: Ramesh
Task: Book rental system
"""

from tkinter import Label, Entry, W, E, Button, END, Tk


class BookSystem(object):
    """Renting the books"""
    def __init__(self, book):
        self.book_charges = {"regular": 1.5, "fiction": 3, "novels": 1.5}
        self.min_book_charges = {"regular": 2, "fiction": 0, "novels": 4.5}
        self.min_rent_days = {"regular": 2, "fiction": 0, "novels": 3}

        book.title("Bill for the Books")
        # Defines the width and height of the window
        book.geometry("500x200")

        # Define the Rent attributes
        Label(book, text="books type", fg="white", bg='black').\
            grid(row=0, column=0, sticky=W, padx=4)
        Label(book, text="Number of books rented", fg="white", bg='black').\
            grid(row=0, column=1, sticky=W, padx=4)
        Label(book, text="time period", fg="white", bg='black').\
            grid(row=0, column=2, sticky=W, padx=50)

        # fields for regular book
        Label(book, text="Regular:", fg="blue", bg='green').\
            grid(row=1, sticky=W, padx=4)
        self.num_regbooksrented = Entry(book)
        self.num_regbooksrented.insert(0, "0")
        self.num_regbooksrented.grid(row=1, column=1, sticky=E, pady=4)
        self.reg_booksystemduration = Entry(book)
        self.reg_booksystemduration.insert(0, "0")
        self.reg_booksystemduration.grid(row=1, column=2, sticky=E, pady=4)

        # fields for fiction book
        Label(book, text="Fiction:", fg="blue", bg='green').grid(row=2, sticky=W, padx=4)
        self.num_ficbooksrented = Entry(book)
        self.num_ficbooksrented.insert(0, "0")
        self.num_ficbooksrented.grid(row=2, column=1, sticky=E, pady=10)
        self.fic_booksystemduration = Entry(book)
        self.fic_booksystemduration.insert(0, "0")
        self.fic_booksystemduration.grid(row=2, column=2, sticky=E, pady=4)

        # fields for novels book
        Label(book, text="Novels:", fg="blue", bg='green').grid(row=3, sticky=W, padx=4)
        self.num_novbooksrented = Entry(book)
        self.num_novbooksrented.insert(0, "0")
        self.num_novbooksrented.grid(row=3, column=1, sticky=E, pady=4)
        self.nov_booksystemduration = Entry(book)
        self.nov_booksystemduration.insert(0, "0")
        self.nov_booksystemduration.grid(row=3, column=2, sticky=E, pady=4)

        # fields for total rent
        Label(book, text="Total Rent").grid(row=4, column=1, sticky=W, padx=40)
        self.total_rent_field = Entry(book)
        self.total_rent_field.grid(row=4, column=2, sticky=E, pady=4)

        # fields for submit, quit and clear buttons
        self.submit_button = Button(
            book,
            text="Submit",
            command=(lambda: self.calculating_rent()),
            bg='dark green').\
            grid(row=5, column=1, sticky=E, pady=10, padx=0)

        self.quit_button = Button(book, text="Quit", command=book.quit, bg='red').\
            grid(row=5, column=2, pady=10)

    def fetch_data(self):
        """
        :return: gives the cost assigned for the person
        """
        rented_books_data = []

        try:
            rented_books_data.append(
                ("regular", int(self.num_regbooksrented.get()),
                 int(self.reg_booksystemduration.get())))
            rented_books_data.append(
                ("fiction", int(self.num_ficbooksrented.get()),
                 int(self.fic_booksystemduration.get())))
            rented_books_data.append(
                ("novels", int(self.num_novbooksrented.get()),
                 int(self.nov_booksystemduration.get())))
        except ValueError:
            print("Please enter Valid data")

        # print(rented_books_data)
        return rented_books_data

    def calculating_rent(self):
        """
        :return: calculates the rent for the books of the person
        """
        rented_books_data = self.fetch_data()
        total_rent = 0
        for row in rented_books_data:
            if row[0] in self.book_charges:
                if row[2] < self.min_rent_days[row[0]]:
                    partial_rent = row[1] * self.min_book_charges[row[0]]
                    total_rent = total_rent + partial_rent
                else:
                    if row[0] == "regular":
                        partial_rent = row[1] * 2 + row[1] * (row[2] - 2) \
                                       * self.book_charges[row[0]]
                        total_rent = total_rent + partial_rent
                    else:
                        partial_rent = row[1] * row[2] \
                                       * self.book_charges[row[0]]
                        total_rent = total_rent + partial_rent
            # print(total_rent)
        self.total_rent_field.delete(0, END)
        self.total_rent_field.insert(0, total_rent)


def main():
    """
    :return: initialize the data
    """
    # Get the book window object
    book = Tk()
    # Create the BookSystem
    # calc = BookSystem(book)
    BookSystem(book)
    # Run the app until exited
    book.mainloop()


main()
