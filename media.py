import webbrowser

class Movie():
    '''I have defined the class Movie. You could do this
    directly in entertainment_center.py but many developers keep their
    class definitions separate from the rest of their code. This also
    gives you practice importing Python files. This class provides a way to
    store movie related information'''


    ''' initialize instance of class Movie
    it's not necessary to take self we can also use any other word also'''
    
    def __init__(self , movie_title , poster_image , 
    	trailer_youtube , rating , actors):
        
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rate = rating
        self.stars = actors
