# Library Management System

![Menu Screen](https://i.ibb.co/S6Q812G/Menu.png) 

A simple Library Management System implemented in Python using the Tkinter library for the graphical user interface. This system allows users to list books, add new books, and remove existing books from a database file (`books.txt`). If this text file does not exist, it will be created after running python file.

## How to Run

1. Ensure you have Python installed on your system.
2. Run the script `project.py`.
3. The main menu will appear, allowing you to navigate through different functionalities.

## Code Structure

### 1. Library Class

- **Constructor (`__init__`):** Initializes the library by opening the `books.txt` file in append mode.
  
- **Destructor (`__del__`):** Closes the file when the Library instance is destroyed.

- **`lib` Method:** Creates the main menu using Tkinter, allowing users to interact with the library.

### 2. Add Book

- **`add_book_window` Method:** Displays a window for adding a new book with input fields for title, author, release year, and number of pages.

### 3. Remove Book

- **`remove_book_window` Method:** Displays a window for removing a book. Users can select or enter the book title, and the system removes the selected book from the file.

### 4. List Books

- **`show_books_window` Method:** Displays a window listing all available books with their titles and authors.

### 5. Execute Functionality

- **`execute` Function:** Executes the selected functionality based on user input from the main menu.

## Getting Started

### Prerequisites

- Python (>=3.6)
- Tkinter library (usually included with Python installations)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mertkont/library-management-system.git
   cd library-management-system

### Screenshots

![List Screen](https://i.ibb.co/fXTYQHj/List.png)


![Add Screen](https://i.ibb.co/zXh9x77/Add.png)


![Delete Screen](https://i.ibb.co/2ZmY45k/Remove.png)

### Usage

1. Choose an option from the main menu:

    - 1 to list books
    - 2 to add a new book
    - 3 to remove a book
    - Q or q to quit the application

2. Follow the on-screen prompts for each option.


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

### Acknowledgments

[Tkinter Documentation](https://docs.python.org/3/library/tkinter.html) - Official documentation for Tkinter.


### Contribution

Feel free to contribute to this project!
