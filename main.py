from flask import Flask, render_template, request
import tmdb_client
import random



app = Flask(__name__)
LIST_TYPES = ['now_playing', 'popular', 'top_rated', 'upcoming']

@app.route('/', methods=['GET'])
def homepage():
    passed_list = request.args.get('list_type', '')

    if passed_list in LIST_TYPES:
        selected_list = passed_list
    else:
        selected_list = 'popular'

    movies = tmdb_client.get_movies_list(selected_list, 12)
    return render_template('homepage.html', movies=movies, list_types=LIST_TYPES, selected=selected_list)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

if __name__ == '__main__':
    app.run(debug=True)




