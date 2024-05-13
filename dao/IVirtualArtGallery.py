from abc import ABC, abstractmethod
from entity.Artwork import Artwork

class IVirtualArtGallery(ABC):
    @abstractmethod
    def addArtwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def updateArtwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def removeArtwork(self, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def getArtworkById(self, artwork_id: int) -> Artwork:
        pass

    @abstractmethod
    def searchArtworks(self, keyword: str) -> list[Artwork]:
        pass

    @abstractmethod
    def addArtworkToFavorite(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def removeArtworkFromFavorite(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def getUserFavoriteArtworks(self, user_id: int) -> list[Artwork]:
        pass
