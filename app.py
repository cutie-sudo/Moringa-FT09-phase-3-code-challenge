import sqlite3
from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    try:
        # Connect to the database
        conn = get_db_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Create an author
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
        author_id = cursor.lastrowid  # Get the ID of the newly created author
        print(f"Author created with ID: {author_id}")

        # Create a magazine
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
        magazine_id = cursor.lastrowid  # Get the ID of the newly created magazine
        print(f"Magazine created with ID: {magazine_id}")

        # Create an article
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (article_title, article_content, author_id, magazine_id))
        print("Article created successfully.")

        # Commit changes to the database
        conn.commit()

        # Query the database for inserted records
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()

        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()

        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()

    except sqlite3.Error as e:
        # Handle SQLite errors specifically
        print(f"An error occurred while querying the database: {e}")
        conn.rollback()  # Rollback the transaction if something went wrong

    finally:
        # Ensure the connection and cursor are closed properly
        cursor.close()
        conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

if __name__ == "__main__":
    main()
