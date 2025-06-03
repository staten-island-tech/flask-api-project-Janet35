from flask import Flask, render_template, request
import requests
app = Flask(__name__)
<<<<<<< HEAD
HEADERS = {
    "User-Agent": "MyMusicApp/1.0 (janetl35@nycstudents.net)"
}
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search = request.form.get("search")
        if not search:
            return render_template("index.html", error="Please enter an artist name.")
        
        url = f"https://musicbrainz.org/ws/2/artist?query={search}&fmt=json"
=======

HEADERS = {
    "User-Agent": "MyMusicApp/1.0 (janetl35@nycstudents.net)"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        if not query:
            return render_template("index.html", error="Please enter an artist name.")
        
        url = f"https://musicbrainz.org/ws/2/artist?query={query}&fmt=json"
>>>>>>> 674b4b1c3b87e53cb75657e6ad7e534a063bb230
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            artists = data.get("artists", [])
<<<<<<< HEAD
            return render_template("artists.html", artists=artists, search=search)
        except Exception as e:
            return render_template("index.html", error=f"Error finding artists: {e}")
=======
            return render_template("artists.html", artists=artists, query=query)
        except Exception as e:
            return render_template("index.html", error=f"Error fetching artists: {e}")
>>>>>>> 674b4b1c3b87e53cb75657e6ad7e534a063bb230
    
    return render_template("index.html")

@app.route("/artist/<artist_id>")
<<<<<<< HEAD
def albums(artist_id):
=======
def artist_albums(artist_id):
>>>>>>> 674b4b1c3b87e53cb75657e6ad7e534a063bb230
    url = f"https://musicbrainz.org/ws/2/release?artist={artist_id}&fmt=json&limit=100"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        releases = data.get("releases", [])

        seen = set()
        albums = []
        for r in releases:
            key = (r.get("title"), r.get("date"))
            if key not in seen:
                seen.add(key)
                albums.append({
                    "id": r.get("id"),
                    "title": r.get("title"),
                    "date": r.get("date", "Unknown")
                })

<<<<<<< HEAD
        return render_template("albums.html", albums=albums)
    except Exception as e:
        return f"Error finding albums: {e}", 404
=======
        return render_template("artist_albums.html", albums=albums)
    except Exception as e:
        return f"Error fetching albums: {e}", 403
>>>>>>> 674b4b1c3b87e53cb75657e6ad7e534a063bb230

if __name__ == "__main__":
    app.run(debug=True)