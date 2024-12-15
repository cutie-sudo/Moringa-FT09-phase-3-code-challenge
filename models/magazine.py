import sqlite3  # This imports the SQLite module, which helps us interact with the database.

class Magazine:
    def __init__(self, id, name, category):
    
        self._id = id

  # This will hold the unique identifier (ID) of the magazine once saved to the database.
        self.name = name  # Calls the setter method to set the name and validate it.
        self.category = category  # Calls the setter method to set the category and validate it.

    def _create_magazine(self):
        """This method adds the magazine to the database."""
        connection = None  # Start by setting the connection to None.

        try:
            # Connect to the database 'magazine.db'. This file will be created if it doesn't exist.
            connection = sqlite3.connect('magazine.db')
            cursor = connection.cursor()  # Cursor allows us to run SQL queries.

            # Run an SQL query to insert the magazine's name and category into the 'magazines' table.
            cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))

            # Commit (save) the changes to the database.
            connection.commit()

            # Get the ID of the newly added magazine and store it in self._id.
            self._id = cursor.lastrowid  # SQLite automatically gives a new ID for each new row.

        except sqlite3.Error as e:
            # If there's any error while interacting with the database, print the error.
            print(f"Error inserting into database: {e}")

            # If there was an error, we roll back (undo) the changes made in the database.
            if connection:
                connection.rollback()

        finally:
            # Always close the connection, whether or not there was an error.
            if connection:
                connection.close()

    @property
    def id(self):
        # This method is a property that returns the magazine's ID.
        return self._id

    @property
    def name(self):
        # This method is a property that returns the magazine's name.
        return self._name

    @name.setter
    def name(self, value):
        """
        This setter method ensures that the magazine's name is:
        - Between 2 and 16 characters long.
        - Cannot be changed after being set (immutable).
        """
        if hasattr(self, '_name'):  # If the name has already been set, it can't be changed.
            raise AttributeError("Name cannot be changed once set.")
        if not value or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value  # If the name is valid, we store it in the _name attribute.

    @property
    def category(self):
        # This method is a property that returns the magazine's category.
        return self._category

    @category.setter
    def category(self, value):
        """
        This setter method ensures that:
        - The category cannot be empty.
        - The category cannot be changed once it is set (immutable).
        """
        if not value:
            raise ValueError("Category cannot be empty.")
        if hasattr(self, '_category'):  # If the category has already been set, it can't be changed.
            raise AttributeError("Category cannot be changed once set.")
        self._category = value  # If the category is valid, we store it in the _category attribute.

    def __repr__(self):
        """
        This method defines how the magazine is represented as a string (for example, when printing it).
        """
        return f'<Magazine {self.name}>'

    def save(self):
        """
        This method saves the magazine's data to the database.
        It calls _create_magazine to insert the data into the database.
        """
        self._create_magazine()

