from flask import Flask, render_template, request
import requests

app = Flask(__name__)

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
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            artists = data.get("artists", [])
            return render_template("artists.html", artists=artists, query=query)
        except Exception as e:
            return render_template("index.html", error=f"Error fetching artists: {e}")
    
    return render_template("index.html")

@app.route("/artist/<artist_id>")
def artist_albums(artist_id):
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

        return render_template("artist_albums.html", albums=albums)
    except Exception as e:
        return f"Error fetching albums: {e}", 403

if __name__ == "__main__":
    app.run(debug=True)