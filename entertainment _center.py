import  media

# a single movie object
toyStory = media.Movie("toy story","a good movie","http://aforismi.meglio.it/img/film/Toy_story.jpg"
                       ,"https://www.youtube.com/watch?v=7FQ68Rw25gM")
batman = media.Movie("Batman the Dark Knight", "a great experience for comic fans",
                       "http://geekretreatimages.s3.amazonaws.com/wp-content/uploads/2016/03/The-Dark-Knight.jpg"
                       , "https://www.youtube.com/watch?v=EXeTwQWrcwY")
equilibrium = media.Movie("Equilibrium", "a great action movie, with a deep message",
                        "http://www.gstatic.com/tv/thumb/movieposters/30590/p30590_p_v8_aa.jpg"
, "https://www.youtube.com/watch?v=raleKODYeg0")

#print(toyStory.story)
#toyStory.show_trailer()

if __name__ == '__main__':
	print ('This program is being run by itself')
else:
	print ('I am being imported from another module')
				
