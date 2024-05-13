class Artwork:
    def __init__(self, artwork_id, title, description, creation_date, medium, image_url):
        self.__artwork_id = artwork_id
        self.__title = title
        self.__description = description
        self.__creation_date = creation_date
        self.__medium = medium
        self.__image_url = image_url

    @property
    def artwork_id(self):
        return self.__artwork_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def creation_date(self):
        return self.__creation_date

    @property
    def medium(self):
        return self.__medium

    @property
    def image_url(self):
        return self.__image_url

    @artwork_id.setter
    def artwork_id(self, new_artwork_id):
        self.__artwork_id = new_artwork_id

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @creation_date.setter
    def creation_date(self, new_creation_date):
        self.__creation_date = new_creation_date

    @medium.setter
    def medium(self, new_medium):
        self.__medium = new_medium

    @image_url.setter
    def image_url(self, new_image_url):
        self.__image_url = new_image_url
