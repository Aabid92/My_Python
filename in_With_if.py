movie_watched = {"green", "blue", "white", "yellow"}

user_movie = input("Enter somthing that you watched: ").lower()

if user_movie in movie_watched:
    print(f"Wow i Also Watched '{user_movie}' movie")
    
else:
    print(f"I want to see that '{user_movie}' movie")
