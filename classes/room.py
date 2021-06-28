class Room:
    
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    def guest_check_in(self, guest):
        self.guests.append(guest)

    def guest_check_out(self, guest):
        self.guests.remove(guest)

    def add_songs_rooms(self, songs):
        self.songs.append(songs)
        




    


  
    
