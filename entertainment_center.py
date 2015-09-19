# standard library imports
import media

# third party imports
import fresh_tomatoes

# Create six movie objects with a title, storyline, poster, and trailer
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://cdn.hellogiggles.com/wp-content/uploads/2013/07/05/toystory.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Jurassic Park",
                     "Man creates dinosaur, dinosaur eats man",
                     "http://www.movieartarena.com/imgs/jurassicparkay.jpg",
                     "https://www.youtube.com/watch?v=sgjDSfbB2ok")

the_empire_strikes_back = media.Movie("The Empire Strikes Back",
                                      "Luke Skywalker battles Darth Vader",
                                      "https://mattadavid.files.wordpress.com/2015/09/url-6.jpg",
                                      "https://www.youtube.com/watch?v=mz_YWNhKOkM")

ghostbusters = media.Movie("Ghostbusters",
                           "A team of scientists battle the supernatural for money",
                           "http://www.moviesontheroof.com/2010/images/ghostbusters.jpg",
                           "https://www.youtube.com/watch?v=vntAEVjPBzQ")

beetlejuice = media.Movie("Beetlejuice",
                          "A couple find themselves stuck haunting their country residence",
                          "http://www.joblo.com/posters/images/full/1988-beetlejuice-poster1.jpg",
                          "https://www.youtube.com/watch?v=2hovKm9oFiM")

city_slickers = media.Movie("City Slickers",
                            "Three friends find themselves as they drive cattle",
                            "http://www.impawards.com/1991/posters/city_slickers_xlg.jpg",
                            "https://www.youtube.com/watch?v=rpxVp1g8xMQ")

# collect all movies in preperation fo rendering
movies = [toy_story,
          avatar,
          the_empire_strikes_back,
          ghostbusters,
          beetlejuice,
          city_slickers]

# generate the html file to serve content
fresh_tomatoes.open_movies_page(movies)
