import sqlite3  # This is the SQLite module, which helps us interact with the database.

class Author:
    def __init__(self, id, name):
        """
        This is the constructor method that gets called when you create a new Author object.
        It takes the author's name as an argument, validates it, and then stores it in the database.
        """
        self._id = id  # Initially, the author does not have an ID.
        self.name = name  # This calls the setter to validate and set the name.
        self._create_author()  # This method inserts the author into the database.

    def _create_author(self):
        """
        This method connects to the database and creates a record for the author.
        It inserts the author's name into the 'authors' table.
        """
        try:
            # Connect to the database file 'magazine.db'. If the file doesn't exist, it will be created.
            connection = sqlite3.connect('magazine.db')
            cursor = connection.cursor()  # The cursor lets us run SQL queries.

            # SQL query to insert the author's name into the 'authors' table.
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
            connection.commit()  # Save the changes to the database.

            # Get the ID of the newly added author and store it in self._id.
            self._id = cursor.lastrowid  # This gives the ID assigned by SQLite to the new record.
            print(f"Author created with ID: {self._id}")  # Print the ID for debugging.

        except sqlite3.Error as e:
            # If there is any error with the database, we print it.
            print(f"Database error: {e}")
            connection.rollback()  # Undo any changes in case of an error.

        finally:
            # Ensure the database connection is closed no matter what.
            connection.close()

    @property
    def id(self):
        """
        This property allows us to access the author's ID.
        It is a getter method for the private _id variable.
        """
        return self._id

    @property
    def name(self):
        """
        This property allows us to access the author's name.
        It is a getter method for the private _name variable.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        This is the setter for the 'name' property.
        It validates the name before it's set:
        - The name cannot be empty.
        - The name must be between 2 and 16 characters long.
        - Once set, the name cannot be changed.
        """
        if hasattr(self, '_name'):  # Check if the name has already been set.
            raise AttributeError("Name cannot be changed once set.")  # If it has, raise an error.
        if not value:
            raise ValueError("Name must not be empty.")  # Ensure the name is not empty.
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")  # Validate name length.
        self._name = value  # If the name passes all checks, store it in _name.

    def __repr__(self):
        """
        This method defines how the Author object is represented when we print it.
        It's used to give a clear and readable output.
        """
        return f'<Author id={self.id}, name={self.name}>'

