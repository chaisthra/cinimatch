import re
import inspect
class Rating():
    ratings=[]
    def __init__(self, title, genre, lang, male_actor, female_actor, boc, review, days_ott, ott_platform, budget, shoot_days, next_film,watched):
       self.genre=genre
       self.title=title
       self.lang=lang
       self.male_actor=male_actor
       self.female_actor=female_actor
       self.boc=boc
       self.review=review
       self.days_ott=days_ott
       self.ott_platform=ott_platform
       self.budget=budget
       self.shoot_days=shoot_days
       self.next_film=next_film
       self.watched=watched
       self.w=0
    
    def gen(self,genre):
        if self.genre=="sci-fi":
            self.w+=2
        elif self.genre=="drama":
            self.w+=2
        elif self.genre=="romance":
            self.w+=1
        elif self.genre=="rom-com":
            self.w+=1
        elif self.genre=="action":
            self.w+=1
        elif self.genre=="tragedy":
            self.w+=1
        elif self.genre=="comedy":
            self.w+=2
        else:
            self.w+=0
    def language(self,lang):
        regional=["kannada", "telugu", "tamil", "malayalam", "marathi", "tulu"]
        if self.lang=="english":
            self.w+=1
        elif self.lang=="hindi":
            self.w+=1
        elif self.lang in regional:
            self.w+=2
        else:
            self.w+=0
            
    def maleactor(self,male_actor):
        actor_listm_nf=["tiger shroff", "ishan khatter", "yuva", "sandeep kishan", "sharwanand", "priyatham"]
        actor_listm_famous=["shah rukh khan", "irrfan khan", "rajni", "salman khan", "ajay devgn", "akshay kumar", "amitabh bacchan", "abhishek bacchan", "tom cruise", "ranbir kapoor", "vin diesel", "leonardo dicaprio", "cillian murphy", "robert doself.wney jr.", "siddharth malhotra", "aditya roy kapur", "varun dhaself.wan", "mahesh babu", "vijay sethupathi", "dulquer salman", "ganesh", "raksith shetty", "puneeth rajkumar"]
        if self.male_actor in actor_listm_famous:
            self.w+=2
        elif self.male_actor in actor_listm_nf:
            self.w+=1
        else:
            self.w+=0
            
    def femaleactor(self,female_actor):
        actor_listf_nf=["janvi kappor", "ananya pandey", "tara sutharia"]
        actor_listf_famous=["tabu", "shraddha kappor", "alia bhatt", "deepika padukone", "katrina kaif", "pooja gandhi", "kajal aggarself.wal", "taapsee pannu"]
        if self.female_actor in actor_listf_famous:
            self.w+=2
        elif self.female_actor in actor_listf_nf:
            self.w+=1
        else:
            self.w+=0
    
    def box_office(self,boc):
        if boc > 100:
            self.w+=2
        elif boc in range(50,100):
            self.w+=1
        else:
            self.w+=0
            
    def reviews(self,review):
        nice=re.compile('good|excellent|mindblowing|amazing')
        okay=re.compile('okay|average')
        bad=re.compile('bad|disgusting|self.waste|awful')
        if nice.search(review):
            self.w+=2
        elif okay.search(review):
            self.w+=1
        elif bad.search(review):
            self.w+=0
        else:
            self.w+=0
   
    def day_to_ott(self,days_ott):
        if self.days_ott > 90:
            self.w+=2
        elif self.days_ott in range (45,90):
            self.w+=1
        elif self.days_ott < 45:
            self.w+=0
        else:
            self.w+=0
    
    def ott(self,ott_platform):
        best=["netflix", "prime", "hotstar"]
        oka=["sonyliv", "zee5", "jiocinema"]
        if self.ott_platform in best:
            self.w+=2
        elif self.ott_platform in oka:
            self.w+=1
        else:
            self.w+=0
    
    def budgett(self,budget):
        if self.budget > 100:
            self.w+=0
        elif self.budget in range(50-100):
            self.w+=1
        elif self.budget <50:
            self.w+=2
        else:
            self.w+=0
            
    def shooting_days(self,shoot_days):
        if self.shoot_days > 100:
            self.w+=1
        elif self.shoot_days in range (50,100):
            self.w+=2
        else:
            self.w+=0
    def film_signed(self,next_film):
        if self.next_film in range (3,5):
            self.w+=2
        elif self.next_film in range (2,3):
            self.w+=1
        else:
            self.w+=0
    def watched_already(self,watched):
        if self.watched =="yes":
            self.w+=1
        elif self.watched=="no":
            self.w+=0
        else:
            print("invalid")
    def calc_rating(self):
        
        if self.w>25:
            rating=10
            
        elif self.w in range(23,25):
            rating = 9
            
        elif self.w in range(21,23):
            rating = 8
            
        elif self.w in range(19,21):
            rating = 7
            
        elif self.w in range(17,19):
            rating = 6
            
        elif self.w in range(15,17):
            rating = 5
           
        elif self.w in range(13,15):
            rating = 4
            
        elif self.w in range(11,13):
            rating = 3
            
        elif self.w in range(9,11):
            rating = 2
            
        elif self.w in range(7,9):
            rating = 1
            
        elif self.w in range(0,7):
            rating = 0
        else:
            print("invalid")
        if rating in self.ratings:
            while True:
                rating -=(0.25)
                if rating not in self.ratings:
                    break
        self.ratings.append(rating)
        print("Rating:",rating)
            
    @staticmethod
    def run_all_methods(title, genre, lang, male_actor, female_actor, boc, review, days_ott, ott_platform, budget, shoot_days, next_film,watched):
        r=Rating(title, genre, lang, male_actor, female_actor, boc, review, days_ott, ott_platform, budget, shoot_days, next_film,watched)
        
        r.gen(genre)
        r.language(lang)
        r.maleactor(male_actor)
        r.femaleactor(female_actor)
        r.box_office(boc)
        r.reviews(review)
        r.day_to_ott(days_ott)
        r.ott(ott_platform)
        r.budgett(budget)
        r.shooting_days(shoot_days)
        r.film_signed(next_film)
        r.watched_already(watched)
        r.calc_rating()
          
print("IT ALL STARTS HERE")
print("WELCOME TO CINIMATCH")
def add_movie():
    movies={}
    m=int(input("Enter the number of movies you wish to enter"))
    for i in range(m):
        movie={}
        title=input("\nEnter the movie {} name: ".format(i+1))
        movie['title']=title
        genre=input("Genre: ").lower
        movie['genre']=genre
        lang=input("Language:").lower()
        movie['lang']=lang
        male_actor=input("Male actor's name:").lower()
        movie['male_actor'] = male_actor
        female_actor=input("Female actor's name:").lower()
        movie['female_actor'] = female_actor
        boc=int(input("Enter box office collection in crores:"))
        movie['box_office_collection'] = boc
        review=str(input("Enter critics review:")).lower()
        movie['review'] = review
        days_ott=int(input("No.of days to release in ott:"))
        movie['days_to_release_in_ott'] = days_ott
        ott_platform=input("Ott platform:").lower()
        movie['ott_platform'] = ott_platform
        budget=int(input("Enter budget of the movie in crores:"))
        movie['budget'] = budget
        shoot_days=int(input("No.of days to shoot the movie:"))
        movie['shoot_days'] = shoot_days
        next_film=int(input("No.of new films signed:"))
        movie['next_film'] = next_film
        watched=input("Have you watched the movie?").lower()
        movie['watched'] = watched
        movies[i+1] = movie
        Rating.run_all_methods(title, genre, lang, male_actor, female_actor, boc, review, days_ott, ott_platform, budget, shoot_days, next_film,watched)
        movies[i + 1] = movie
    return movies

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[1]['rating'] > pivot[1]['rating']]
    middle = [x for x in arr if x[1]['rating'] == pivot[1]['rating']]
    right = [x for x in arr if x[1]['rating'] < pivot[1]['rating']]
    return quicksort(left) + middle + quicksort(right)

def sort_movies_by_rating(movies):
    movies_list = list(movies.items())
    sorted_movies_list = quicksort(movies_list)
    sorted_movies = dict(sorted_movies_list)
    return sorted_movies

def display_movies(movies):
    for movie_id, movie in movies.items():
        print(f"\nMovie {movie_id}:")
        for key, value in movie.items():
            print(f"{key.capitalize()}: {value}")

def delete_movies(movie):
    movie_title = input("Enter the movie title you wish to delete: ").lower()
    movie_found = False
    for key, value in list(movies.items()):
        if value['title'].lower() == movie_title:
            del movies[key]
            movie_found = True
            print(f"Movie '{movie_title}' successfully deleted.")
            break
    if not movie_found:
        print(f"Movie '{movie_title}' not found.")    

def recommend(movies):
    filtered_movies = {k: v for k, v in movies.items() if v['genre'] == genre.lower()}
    top_movies = dict(list(filtered_movies.items())[:3])
    if not top_movies:
        print(f"No movies found for genre: {genre}")
    else:
        print(f"Top 3 movies in the genre '{genre}':")
        display_movies(top_movies)

def search_movie(movies):
    movie_title = input("Enter the movie title you wish to search: ").lower()
    movie_found = False
    for key, value in movies.items():
        if value['title'].lower() == movie_title:
            print(f"\nMovie found: ID {key}")
            for k, v in value.items():
                print(f"{k.capitalize()}: {v}")
            movie_found = True
            break
    if not movie_found:
        print(f"Movie '{movie_title}' not found.")
while True:
    print("Menu")
    print("1. Add new movies")
    print("2. Display movies")
    print("3. Search movies")
    print("4. Recommend moovies")
    print("5. Delete movies")
    option=input("What do want to do today?")
    match option:
        case "1":
            movies=add_movie()
            print("Movies added successfully")
        case "2":
            sorted_movies = sort_movies_by_rating(movies)
            display_movies(sorted_movies)
        case "3":
            search_movie(sorted_movies)
        case "4": 
            sorted_movies = sort_movies_by_rating(movies)
            recommend(sorted_movies, input("Enter the genre for recommendations: "))
        case "5":
            delete_movie(sorted_movies)
        case _:
            print("Good day")

    
