from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get the first 150 Pokémon from the API
    response = requests.get("https://spoonacular.com/food-api")
    data = response.json()
    food = data['results']
    
    food = []
    
    for food in food_list:
        url = food['url']
        parts = url.strip("/").split("/")
        id = parts[-1]  # The last part is the Pokémon's ID
        
        # Create an image URL using the Pokémon's ID
        image_url = f"https://api.spoonacular.com/recipes/{id}/information.png"
        
        food.append({
            'name': food['name'].capitalize(),
            'id': id,
            'image': image_url
        })
    
    # Send the Pokémon list to the index.html page
    return render_template("index.html", food=food)

# New route: When a user clicks a Pokémon card, this page shows more details and a stats chart
@app.route("/food/<int:id>")
def food_detail(id):
    # Get detailed info for the Pokémon using its id
    response = requests.get(f"https://api.spoonacular.com/recipes/{id}/information")
    data = response.json()
    
    # Extract extra details like types, height, and weight
    ingredients = data.get('ingredients')
    recipe = data.get('recipe')
    name = data.get('name').capitalize()
    image_url = f"https://api.spoonacular.com/recipes/{id}/information.png"
    
    # Send all details to the food.html template
    return render_template("food.html", food={
        'name': name,
        'recipe': recipe,
        'ingredients': ingredients,
    })

if __name__ == '__main__':
    app.run(debug=True)