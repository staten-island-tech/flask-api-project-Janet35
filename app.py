from flask import Flask, render_template, request
import requests
app = Flask(__name__)

HEADERS = {
    "User-Agent": "MyMusicApp/1.0 (janetl35@nycstudents.net)"
}
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":
        search = request.form.get("search")
        url = f"https://musicbrainz.org/ws/2/artist?query={search}&fmt=json"
        response =requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        artists = data.get("artists", [])

    else: 
        not search
        return render_template("index.html", error="Please enter an artist name.")
    try:
            return render_template("artists.html", artists=artists, search=search)
    except Exception as e:
            return render_template("index.html", error=f"Error finding artists: {e}")

@app.route("/artist/<artist_id>")
def albums(artist_id):
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

        return render_template("albums.html", albums=albums)
    except Exception as e:
        return f"Error finding albums: {e}", 404

if __name__ == "__main__":
    app.run(debug=True)
