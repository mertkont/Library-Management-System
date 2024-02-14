import tkinter as tk
from tkinter import ttk, messagebox

class Library:

    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def lib(self):
        menu_window = tk.Tk()
        menu_window.title("Menu")
        menu_window.geometry("325x240+0+0")

        menu_list = ["1) List Books", "2) Add a Book", "3) Remove a Book", "Q) Quit"]

        for menu_item in menu_list:
            menu_label = tk.Label(menu_window, text=menu_item, font=("Ubuntu", 16, "bold"))
            menu_label.pack()

        value_var = tk.StringVar()
        value_combobox = ttk.Combobox(menu_window, values=['1', '2', '3', 'Q'], font=("Ubuntu", 12),
                                      textvariable=value_var, style="Value.TCombobox")
        style = ttk.Style()
        style.configure('Value.TCombobox', background='white', font=('Ubuntu', 12), fieldbackground='white',
                        arrowsize=17, highlightthickness=0)
        value_combobox.pack(pady=10)

        def execute():
            text = value_combobox.get().lower()
            value_combobox.delete(0, tk.END)
            if text == "1":
                self.show_books_window()
            elif text == "2":
                self.add_book_window()
            elif text == "3":
                self.remove_book_window()
            elif text == "q":
                confirmation = messagebox.askyesno("Quit", "Do you really want to quit?", icon='warning',
                                                   parent=menu_window)
                if confirmation:
                    menu_window.quit()
                    menu_window.destroy()
            else:
                messagebox.showwarning("Wrong Value", "Please use the values in the menu.",
                                       parent=menu_window)

        execute_button = tk.Button(menu_window, text="Execute", command=execute, bg="green", fg="white", font=("Ubuntu",
                                                                                                               14))
        execute_button.pack(pady=1)
        menu_window.bind("<Return>", lambda event: execute())
        value_combobox.focus_set()

        menu_window.mainloop()

    def add_book_window(self):
        add_window = tk.Tk()
        add_window.title("Add a Book")
        add_window.geometry("300x175+100+100")

        fields = ["Book Title:", "Book Author:", "First Release Year:", "Number of Pages:"]

        entries = []

        for field in fields:
            frame = tk.Frame(add_window)
            frame.pack(side=tk.TOP)

            book = tk.Label(frame, text=field, font=("Ubuntu", 12), bg="lightgray")
            book.pack(side=tk.LEFT)

            book_input = tk.Entry(frame, font=("Ubuntu", 12), width=13)
            book_input.pack(side=tk.LEFT)

            entries.append(book_input)

            def add():
                title, author, year, pages = [entry.get().strip() for entry in entries]

                if len(title) != 0 and len(author) != 0 and len(year) != 0 and len(pages) != 0:
                    book_str = f"{title},{author},{year},{pages}"

                    with open("books.txt", "a+") as file:
                        file.write(book_str + "\n")

                    messagebox.showinfo("Book Added", "Book successfully added.", parent=add_window)
                    add_window.destroy()
                else:
                    messagebox.showerror("Error", "Please fill in all fields.", parent=add_window)

        close_add_window_button = tk.Button(add_window, text="Close", command=add_window.destroy, bg="red", fg="white")
        close_add_window_button.pack(side=tk.RIGHT)

        add_button = tk.Button(add_window, text="Add", command=add, bg="green", fg="white")
        add_button.pack(side=tk.RIGHT)

        add_window.bind("<Return>", lambda event: add())

        add_window.mainloop()

    def remove_book_window(self):
        remove_window = tk.Toplevel()
        remove_window.title("Remove a Book")
        remove_window.geometry("325x125+100+100")

        title_label = tk.Label(remove_window, text="Select or Enter Book Title to Remove:", font=("Ubuntu", 12))
        title_label.pack()

        title_var = tk.StringVar()
        title_combobox = ttk.Combobox(remove_window, textvariable=title_var, width=25, style='Remove.TCombobox')
        style = ttk.Style()
        style.configure('Remove.TCombobox', background='white', font=('Ubuntu', 12), fieldbackground='white',
                        arrowsize=17, highlightthickness=0)
        title_combobox.pack()

        books_list = []
        with open("books.txt", "r") as file:
            data = file.read()
            lines = data.splitlines()
            for line in lines:
                book = line.split(",")
                books_list.append(book[0])

        title_combobox["values"] = books_list

        def remove():
            title_to_remove = title_combobox.get().strip()
            if title_to_remove:
                books_list = []
                with open("books.txt", "r") as file:
                    data = file.read()
                    lines = data.splitlines()
                    for line in lines:
                        book = line.split(",")
                        books_list.append(book)

                index_to_remove = None
                for i, book in enumerate(books_list):
                    if book[0] == title_to_remove:
                        index_to_remove = i
                        break

                if index_to_remove is not None:
                    del books_list[index_to_remove]

                    with open("books.txt", "w") as file:
                        file.write("")

                    with open("books.txt", "a+") as file:
                        for book in books_list:
                            book_str = ",".join(book)
                            file.write(book_str + "\n")

                    messagebox.showinfo("Book Removed", f"Book '{title_to_remove}' successfully removed.",
                                        parent=remove_window)
                    remove_window.destroy()
                else:
                    messagebox.showwarning("Book Not Found", f"Book '{title_to_remove}' not found.",
                                           parent=remove_window)
            else:
                messagebox.showwarning("Error", "Please enter a book title.",
                                       parent=remove_window)

        close_remove_window_button = tk.Button(remove_window, text="Close", command=remove_window.destroy, bg="red", fg="white")
        close_remove_window_button.pack(side=tk.RIGHT)

        remove_button = tk.Button(remove_window, text="Remove", command=remove,  bg="green", fg="white")
        remove_button.pack(side=tk.RIGHT)

        remove_window.bind("<Return>", lambda event: remove())
        title_combobox.focus_set()

        remove_window.mainloop()

    def show_books_window(self):
        show_window = tk.Tk()
        show_window.title("List of Books")
        show_window.geometry("400x300+100+100")

        title_label = tk.Label(show_window, text="Book, Author", font=("Helvetica", 14, "bold"))
        title_label.pack(pady=10)

        separator = tk.Frame(show_window, height=2, bd=1, relief="sunken")
        separator.pack(fill="x", padx=10, pady=5)

        books = tk.Listbox(show_window, width=40, height=10, font=("Helvetica", 12))
        books.pack()

        with open("books.txt", "r") as file:
            data = file.read()
            lines = data.splitlines()
            for line in lines:
                book = line.split(",")
                title = book[0]
                author = book[1]
                books.insert("end", f"{title}, by {author}")

        close_show_window_button = tk.Button(show_window, text="Close", command=show_window.destroy, bg="red", fg="white")
        close_show_window_button.pack(side=tk.RIGHT)

        show_window.mainloop()

Library().lib()
