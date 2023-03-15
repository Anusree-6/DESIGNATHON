from flask import Flask,render_template, url_for, request
import requests
app = Flask(__name__)


#route = url = link

@app.route("/")
def main():
    rawData = requests.get("https://api.themoviedb.org/3/search/movie?api_key=7fe2453274cf59d6f0f5c8f4d29bf3c4&query=the+departed")
    movies = rawData.json()
    return render_template("home.html",movies=movies)
                           

@app.route("/<title>")
def movies_by_title(title):
    rawData = requests.get("https://api.themoviedb.org/3/search/movie?api_key=7fe2453274cf59d6f0f5c8f4d29bf3c4&query="+title)
    movies = rawData.json()
    return render_template("home.html",movies=movies)

@app.route("/single_movie/<title>")
def single_movie(title):
    rawData = requests.get("https://api.themoviedb.org/3/search/movie?api_key=7fe2453274cf59d6f0f5c8f4d29bf3c4&query="+title)
    movie = rawData.json()
    return render_template("single_movie.html",movie=movie)


@app.route("/search")
def search_form():
    return render_template("search.html")


@app.route("/search_by_title",methods=["POST"])
def search_by_title():
    title=request.form["title"]
    year = request.form["year"]
    if year !="":
        rawData = requests.get("https://api.themoviedb.org/3/search/movie?api_key=7fe2453274cf59d6f0f5c8f4d29bf3c4&query="+title+"&y="+year)
    else:
        rawData = requests.get("https://api.themoviedb.org/3/search/movie?api_key=7fe2453274cf59d6f0f5c8f4d29bf3c4&query="+title)
    movie = rawData.json
    return render_template("search.html",movie=movie)


                               
    
        
 


if __name__=="__main__":
    app.run(debug=True)