import media
import fresh_tomatoes

""" This is a file which uses the media class to display some movie trailers """

toy_story = media.Movie("Toy Story", "A Story of a boy and his toys that come to life",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A Marin who goes on alian planet",
                       "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                       "https://www.youtube.com/watch?v=d1_JBMrrYw8")

baahubali = media.Movie("Baahubali", "Story of a king and queen",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")
movies = [toy_story,avatar,baahubali]

def main():
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()

