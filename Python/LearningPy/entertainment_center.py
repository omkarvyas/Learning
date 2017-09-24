import media

toy_story = media.Movie("Toy Story",
                       "A Story of a boy and his toys that come to life",
                       "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)


avatar = media.Movie("Avatar",
                       "A Marin who goes on alian planet",
                       "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                       "https://www.youtube.com/watch?v=d1_JBMrrYw8")
print(avatar.storyline)

avatar.show_trailer()


baahubali = media.Movie("Baahubali",
                       "Story of a king and queen",
                       "https://en.wikipedia.org/wiki/Baahubali:_The_Beginning#/media/File:Baahubali_poster.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")
print(baahubali.storyline)

baahubali.show_trailer()
