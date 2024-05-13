from dao.VirtualArtGalleryServiceImpl import VirtualArtGalleryServiceImpl
from dao.IVirtualArtGallery import IVirtualArtGallery
from util.DBConnUtil import DBConnector

def main():
        dbconn =DBConnector('vartgallery','root','MentalNaKodukka!','localhost')

        connection = DBConnector.get_connection(dbconn)

        service = VirtualArtGalleryServiceImpl(dbconn)
        while True:
            print("\nVAGMS Menu:")
            print("1. Add Artwork (addArtwork)")
            print("2. Search Artworks (searchArtworks)")
            print("3. Update Artwork (updateArtwork)")
            print("4. Delete Artwork (removeArtwork)")
            print("5. Add Artwork to Favorites (addArtworkToFavorite)")
            print("6. Remove Artwork from Favorites (removeArtworkFromFavorite)")
            print("7. View Favorite Artworks (getUserFavoriteArtworks)")
            print("0. Exit")

            choice = input("Enter your choice: ")
            user_id = int(input("Enter user id:"))
            if choice == '1':
                service.addArtwork()
            elif choice == '2':
                service.searchArtworks(user_id)
            elif choice == '3':
                service.updateArtwork(user_id)
            elif choice == '4':
                service.removeArtwork(user_id)
            elif choice == '5':
                service.addArtworkToFavorite(user_id)
            elif choice == '6':
                service.removeArtworkFromFavorite(user_id)
            elif choice == '7':
                service.getUserFavoriteArtworks(user_id)
            elif choice == '0':
                break
            else:
                print("Invalid choice!")


if __name__ == "__main__":
    main()
