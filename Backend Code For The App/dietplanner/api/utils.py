import requests

SPOONACULAR_API_KEY = 'add62861fa63450185b444f315793445'

def get_meals_from_spoonacular(query, dietary_restrictions=None):
    base_url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        'apiKey': SPOONACULAR_API_KEY,
        'query': query,
        'diet': dietary_restrictions if dietary_restrictions else '',
        'number': 5,  # Number of meals to return
        'addRecipeInformation': True
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return []
