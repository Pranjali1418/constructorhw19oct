# Create constructor and objects of MovieTheater class

class MovieTheater:
    def __init__(self, movie_name, ticket_price , seat_no):
        print(f"MovieTheater constructor is running for {movie_name}")
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.seat_no =seat_no

movie1 = MovieTheater("Mirzapur", 250 , "A5")
movie2 = MovieTheater("Dharmveer", 300 ,"E6")

movie1.ticket_price = 350
movie2.seat_no = "E7"
movie2.ticket_price = 330

print(movie1.ticket_price)
print(movie2.seat_no)