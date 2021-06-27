class Room:
    
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    def add_songs_rooms(self, songs):
        self.songs.append(songs)

    def guest_check_in(self, guest):
        self.guest_list.append(guest)

    def guest_check_out(self, guest):
        self.guest_list.remove(guest)


        




    


  
    
