import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikmedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikmedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

print(avatar.storyline)

the_empire_strikes_back = media.Movie("The Empire Strikes Back",
                                      "Luke Skywalker battles Darth Vader",
                                      "https://mattadavid.files.wordpress.com/2015/09/url-6.jpg",
                                      "https://www.youtube.com/watch?v=mz_YWNhKOkM")

the_empire_strikes_back.show_trailer()
