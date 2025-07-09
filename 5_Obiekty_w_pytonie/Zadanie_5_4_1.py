# import
import random
from datetime import date

#  definicja klas
class Movie:
    def __init__(self, title, year, movie_genre):
        self.title = title
        self.issue_year = year
        self.movie_genre = movie_genre
        #Variables
        self._number_of_plays = 0
        
    @property
    def number_of_plays(self):
        return self._number_of_plays
    
    @number_of_plays.setter
    def number_of_plays(self, value):
        self._number_of_plays = value
    
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
        return f'{self.title} S{txt2}E{txt1}'

#funkcje
def get_movies(list):
    """
        function searching objects of Movie class
    Args:
        list of Movies or TvSeries objects 

    Returns:
        list of Movies object
    """
    list_of_movies =[]
    kind_of_class =""
    text ="Movie"
    for i in range(0,len(list)):
        kind_of_class = str(type(list[i]))
        if  text in kind_of_class:           
            list_of_movies.append(list[i])
    return list_of_movies

def get_series(list):
    """
    
        function searching objects of TvSeries class
    Args:
        list of Movies or TvSeries objects 

    Returns:
        list of TvSeries object
    """

    list_of_series=[]
    kind_of_class =""
    text ="TvSeries"
    for i in range(0,len(list)):
        kind_of_class = str(type(list[i]))
        if  text in kind_of_class:           
            list_of_series.append(list[i])
    return list_of_series

def search(list,title):
    """
        function serach object by Title, result is presented as index number in list
    Args:
        list of Movies or TvSeries objext
        Title as String
     
    """
    result =[]
    for i in range(0,len(list)):
        if list[i].title == title:
            result.append(list[i])
    for n in range(0, len(result)):
        print(result[n])
        
        
def generate_views(lib):
    """
        function generate random amount  of views of randm position in list of Movies or TVSeries
    Args:
        list of Movies or TVSeries objects
    """
    random_index = random.randint(0, len(lib)-1)
    random_views = random.randint(1,100)
    item = lib[random_index]
    item.number_of_plays=random_views
    
def generate_views_in_lib(lib, number):
    """_summary_

    Args:
        list of Movies or TvSeries objexts
        number as integer of object that get random amount of views
    """
    for i in range(1,number):
        #print(i)
        generate_views(lib)
        
def top_movies(item, amount):
    """
     Function search the Movies or TvSeries objext with the highesr views
    Args:
        list of Movies and TvSeries
        amount of top views

    Returns:
        _list of top viewd objexts
    """
    temp_list =[]
    result_list=[]
    temp_list = sorted(item, key=lambda k: k.number_of_plays, reverse=True)  
    for i in range(0,amount):
        result_list.append(temp_list[i])
    return result_list

def add_tvseries_to_lib(title, year_of_issue, genre, number_of_episods, sezon):
    """
    Function add TvSerials episods to list

    Args:
        title as string
        year_of_issue as integer
        genre (_type_): as string
        number_of_episods as integer
        sezon as string

    Returns:
        _list of TvSeries objexts
    """
    
    list=[]
   
    for i in range(0,number_of_episods):
        episod = TvSeries(title=title,year = year_of_issue, movie_genre=genre,  episod_number= i+1, sezon_number = sezon,)
        
        list.append(episod)
        
    return list


# prezentacja wynikow
    
print("########################################################################################")
print("##               Biblioteka filmw                                                     ##")
print("########################################################################################")

# wypelnienie biblioteki filmami i serialami
series=[]
series = add_tvseries_to_lib("Star Gate",1996,"Sci-Fi",22,1 )
list_of_movies_series=[]
list_of_movies_series.extend(series)

movie1 = Movie(title="Jurasic Park. Odrodzenia",year = 2025, movie_genre="Sci-Fi")
list_of_movies_series.append(movie1)
series=[]
series = add_tvseries_to_lib("Star Gate",1997,"Sci-Fi",22,2 )
list_of_movies_series.extend(series)


movie2 =  Movie(title="Star Wars New Hope",year = 1977, movie_genre="Sci-Fi")
list_of_movies_series.append(movie2)
movie3 =  Movie(title="Star Wars The Empire Strikes Back",year = 1980, movie_genre="Sci-Fi")
list_of_movies_series.append(movie3)
series=[]
series = add_tvseries_to_lib("Andor",2023,"Sci-Fi",12,1 )
list_of_movies_series.extend(series)
movie4 =   Movie(title="Star Wars Return of the Jedi",year = 1983, movie_genre="Sci-Fi")
list_of_movies_series.append(movie4)
series = add_tvseries_to_lib("Andor",2025,"Sci-Fi",12,2)
list_of_movies_series.extend(series)

# generowanie ilosci odtworzen

generate_views_in_lib(list_of_movies_series,10)

day = date.today().strftime("%d.%m.%Y")
print("Najpopularniejsze filmy i seriale dnia " + day)

# prezentacja trzech najpopularniejszych pozycji

result = top_movies(list_of_movies_series,3)
for item in result:
    text = str(item)
    print(text + "ilość odsłon: " + str(item._number_of_plays))
   # if ("TvSeries" in str(type(item)))
   # print(item.title + " " + str(item._number_of_plays))


