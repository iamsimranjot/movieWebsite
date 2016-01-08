''' In this file, I have defined several of my favourite instances
 of the class Movie defined in media.py. After you run this code,
 the file fresh_tomatoes.html is launched dynamically created from 
 a python data structure! '''

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story" , 
"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg" , 
"https://www.youtube.com/watch?v=KYz2wyBy3kc" , "8.3" , 
"Tom Hanks, Tim Allen")

avatar = media.Movie("Avatar" , 
"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg" , 
"https://www.youtube.com/watch?v=5PSNL1qE6VY" , "7.9" , 
"Sam Worthington, Zoe Saldana")

dumb_dumber = media.Movie("Dumb & Dumber" , 
"https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg" , 
"https://www.youtube.com/watch?v=l13yPhimE3o" , "7.3" , 
"Jim Carrey, Jeff Daniels")

beautiful_mind = media.Movie("A Beautiful Mind" , 
"https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg" , 
"https://www.youtube.com/watch?v=WFJgUm7iOKw" , "8.2" , 
"Russell Crowe, Ed Harris")

imitation_game = media.Movie("The Imitation Game" , 
"https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg" , 
"https://www.youtube.com/watch?v=S5CjKEFb-sM" , "8.1" , 
"Benedict Cumberbatch, Keira Knightley")

kings_speech = media.Movie("The King's Speech" , 
"https://upload.wikimedia.org/wikipedia/en/a/a0/Kings_speech_ver3.jpg" , 
"https://www.youtube.com/watch?v=pzI4D6dyp_o" , "8.1" , 
"Colin Firth, Geoffrey Rush")

movies = [toy_story, avatar , dumb_dumber , beautiful_mind , imitation_game , kings_speech]

if __name__ == "__main__":
	
	'''
	This function call is made to 'open_movies_page' which is defined
	in the fresh_tomatoes module. It places the the movie tiles placeholder
	generated content to the output file and then opens the output file
	which is an HTML file in the browser. It creates the output file dynamically
	acoording to the given input which in this case are movies. '''
	
	fresh_tomatoes.open_movies_page(movies)
