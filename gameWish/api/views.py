from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GameSerializer
from Games.models import Game
import requests

# Create your views here.

def fetch_game_data(request):
      # Replace YOUR_API_KEY with your actual IGDB API key
    api_token = 'rllg6x3mwy2nlhuo9dgppr0tkeoqe3'
    client_id = 'oh1a4v2eabzyogqacl9a5vynyhrai6'
    
    # Define the IGDB API endpoint
    api_url = 'https://api.igdb.com/v4/games'

    # Define the parameters for the API request
    params = {
        'search': 'zelda',  # Return only games with "zelda" in the title
        'fields': ' name; ',  # Specify the fields you want to retrieve
        'limit': 10,  # Adjust the limit as needed
    }

    # Set up headers with your API key
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {api_token}',
    }

    # Make the API request
    response = requests.post(api_url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Process the data and save it to your Game model
        # for game_data in data:
        #     title = game_data.get('name', '')
        #     image_url = game_data.get('cover', {}).get('url', '')

        #     # Create or update the Game model
        #     game, created = Game.objects.update_or_create(
        #         title=title,
        #         defaults={'image_url': image_url}
        #     )

        return render(request, 'success.html', {'message': 'Data fetched successfully', 'data': data})
    else:
        # Display an error message if the request was unsuccessful
        return render(request, 'error.html', {'message': f'Error obteniendo datos: {response.status_code}'})


