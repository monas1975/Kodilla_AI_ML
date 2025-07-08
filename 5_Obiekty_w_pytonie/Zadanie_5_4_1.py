class Movie:
    def __init__(self, title, year, movie_genre):
        self.title = title
        self.issue_year = year
        self.movie_genre = movie_genre
        #Variables
        self.number_of_plays = 0
    
    def play(self, step=1):
        self.number_of_plays +=step
    
    def __str__(self):
        return f'{self.title} ({str(self.issue_year)})'
   

    
class TvSeries(Movie):
    def __init__(self,episod_number, sezon_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episod_number = episod_number
        self.sezon_number = sezon_number
    def __str__(self):
        txt1  = "{:02d}".format(self.episod_number)
        txt2  = "{:02d}".format(self.sezon_number)
        return f'{self.title} S{txt1}E{txt2}'

def get_movies(list):
    list_of_movies =[]
    kind_of_class =""
    text ="Movie"
    for i in range(0,len(list)):
        kind_of_class = str(type(list[i]))
        if  text in kind_of_class:           
            list_of_movies.append(list[i])
    return list_of_movies

def get_series(list):
    list_of_series=[]
    kind_of_class =""
    text ="TvSeries"
    for i in range(0,len(list)):
        kind_of_class = str(type(list[i]))
        if  text in kind_of_class:           
            list_of_series.append(list[i])
    return list_of_series

def search(list,title):
    result =[]
    for i in range(0,len(list)):
        if list[i].title == title:
            result.append(list[i])
    for n in range(0, len(result)):
        print(result[n])

list_of_movies_series=[]


movie1 = Movie(title="Jurasic Park. Odrodzenia",year = 2025, movie_genre="Sci-Fi")

tvserie1 = TvSeries(title="Star Gate",year = 1996, movie_genre="Sci-Fi", episod_number=1, sezon_number = 1)
tvserie2 = TvSeries(title="Star Gate",year = 1996, movie_genre="Sci-Fi", episod_number=2, sezon_number = 1)
tvserie3 = TvSeries(title="Star Gate",year = 1996, movie_genre="Sci-Fi", episod_number=1, sezon_number = 2)
tvserie4 = TvSeries(title="Star Gate",year = 1996, movie_genre="Sci-Fi", episod_number=1, sezon_number = 2)
tvserie5 = TvSeries(title="Andor",year = 2025, movie_genre="Sci-Fi", episod_number=2, sezon_number = 11)
tvserie6 = TvSeries(title="Star Gate",year = 2025, movie_genre="Sci-Fi", episod_number=1, sezon_number = 12)
movie2 =  Movie(title="Star Wars New Hope",year = 1977, movie_genre="Sci-Fi")
movie3 =  Movie(title="Star Wars The Empire Strikes Back",year = 1980, movie_genre="Sci-Fi")
movie4 =   Movie(title="Star Wars Return of the Jedi",year = 1983, movie_genre="Sci-Fi")

print(tvserie1)
print(str(movie1.number_of_plays))
movie1.play()
movie1.play()
print(str(movie1.number_of_plays))
print(str(tvserie1.number_of_plays))
tvserie1.play()
tvserie1.play()
tvserie1.play()
tvserie1.play()
print(str(tvserie1.number_of_plays))

print("--------------------------------------")
list_of_movies_series.append(movie1)
list_of_movies_series.append(tvserie1)
list_of_movies_series.append(tvserie2)
list_of_movies_series.append(tvserie3)
list_of_movies_series.append(movie2)
list_of_movies_series.append(movie3)
list_of_movies_series.append(tvserie4)
list_of_movies_series.append(tvserie5)
list_of_movies_series.append(tvserie6)
list_of_movies_series.append(movie4)
#list_of_movies_series.append(movie5)



for item in list_of_movies_series:
    print(item)

print("++++-----------------------------------------------")
list_of_movies = get_movies(list_of_movies_series)
for item in list_of_movies:
   print(item)

print("===================================================")
list_of_series = get_series(list_of_movies_series)
for item in list_of_series:
    print(item)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
search(list_of_movies_series,"Andor")
search(list_of_movies_series,"Star Gate")