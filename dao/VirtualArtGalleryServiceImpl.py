import psycopg2
from util.DBConnUtil import DBConnector
from entity.Artwork import Artwork
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from exception.UserNotFoundException import UserNotFoundException

class VirtualArtGalleryServiceImpl:
    def __init__(self, connection):
        self.connection = connection

    def __enter__(self):
        self.connection = self.connection.get_connection()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

    def addArtwork(self):
        # Get artwork details from the user
        title = input("Enter artwork title: ")
        description = input("Enter artwork description: ")
        creation_date = input("Enter creation date (YYYY-MM-DD): ")
        medium = input("Enter artwork medium: ")
        image_url = input("Enter image URL: ")

        # Create an artwork dictionary
        artwork = {
            'title': title,
            'description': description,
            'creation_date': creation_date,
            'medium': medium,
            'image_url': image_url
        }

        # Execute SQL command to insert artwork into database
        cursor = self.connection.cursor()
        insert_query = """
            INSERT INTO artworks (title, description, creation_date, medium, image_url)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
        artwork['title'], artwork['description'], artwork['creation_date'], artwork['medium'], artwork['image_url']))
        self.connection.commit()
        return True

    def updateArtwork(self, artwork):
        cursor = self.connection.cursor()
        update_query = """
            UPDATE artworks SET title = %s, description = %s, creation_date = %s, medium = %s, image_url = %s
            WHERE artwork_id = %s
        """
        cursor.execute(update_query, (artwork.title, artwork.description, artwork.creation_date, artwork.medium, artwork.image_url, artwork.artwork_id))
        self.connection.commit()
        return True

    def removeArtwork(self, artwork_id):
        cursor = self.connection.cursor()
        delete_query = "DELETE FROM artworks WHERE artwork_id = %s"
        cursor.execute(delete_query, (artwork_id,))
        self.connection.commit()
        return True

    def getArtworkById(self, artwork_id):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM artworks WHERE artwork_id = %s"
        cursor.execute(select_query, (artwork_id,))
        artwork_data = cursor.fetchone()
        if artwork_data:
            artwork = Artwork(*artwork_data)
            return artwork
        else:
            return None

    def searchArtworks(self, keyword):
        cursor = self.connection.cursor()
        search_query = "SELECT * FROM artworks WHERE title LIKE %s OR description LIKE %s"
        cursor.execute(search_query, (f"%{keyword}%", f"%{keyword}%"))
        artworks_data = cursor.fetchall()
        artworks = [Artwork(*artwork_data) for artwork_data in artworks_data]
        return artworks

    def addArtworkToFavorite(self, user_id, artwork_id):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO user_favorite_artwork (user_id, artwork_id) VALUES (%s, %s)"
        cursor.execute(insert_query, (user_id, artwork_id))
        self.connection.commit()
        return True

    def removeArtworkFromFavorite(self, user_id, artwork_id):
        cursor = self.connection.cursor()
        delete_query = "DELETE FROM user_favorite_artwork WHERE user_id = %s AND artwork_id = %s"
        cursor.execute(delete_query, (user_id, artwork_id))
        self.connection.commit()
        return True

    def getUserFavoriteArtworks(self, user_id):
        cursor = self.connection.cursor()
        select_query = """
            SELECT a.* FROM artworks a
            JOIN user_favorite_artwork ufa ON a.artwork_id = ufa.artwork_id
            WHERE ufa.user_id = %s
        """
        cursor.execute(select_query, (user_id,))
        favorite_artworks_data = cursor.fetchall()
        favorite_artworks = [Artwork(*artwork_data) for artwork_data in favorite_artworks_data]
        return favorite_artworks
