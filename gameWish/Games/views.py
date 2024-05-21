from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
import requests
from Core.models import Profile
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def fetch_games_data(request):
    
    if request.method == 'GET':

        api_token = 'srqa03mld4byy83shbpnwymwlg9mb7'
        client_id = 'oh1a4v2eabzyogqacl9a5vynyhrai6'
        
        # Define the IGDB API endpoint
        api_url_game = 'https://api.igdb.com/v4/games'
        query = request.GET.get('query','')

        # Define the parameters for the API request
        params_game = {
            'search': query, 
            'fields': ' id, name, cover.image_id',  # Specify the fields you want to retrieve
            'limit': '200' # Adjust the limit as needed
        }

        # Set up headers with your API key
        headers = {
            'Client-ID': client_id,
            'Authorization': f'Bearer {api_token}',

        }

        # Make the API request
        response_games = requests.post(api_url_game, headers=headers, params=params_game)
        # response_cover = requests.post(api_url_cover, headers=headers, params=params_cover)

        # Check if the request was successful (status code 200)
        if response_games.status_code == 200:
            # Parse the JSON response
            data_games = response_games.json()
            return render(request, 'success.html', {'data': data_games,})
        else:
            # Display an error message if the request was unsuccessful
            return render(request, 'error.html', {'message': f'Error obteniendo datos: {response_games.status_code}'})
        
    else:
        return render(request, 'error.html', {'message': 'Método no permitido'})

def game_details(request, id):
    if request.method == 'GET':
            
            api_token = 'srqa03mld4byy83shbpnwymwlg9mb7'
            client_id = 'oh1a4v2eabzyogqacl9a5vynyhrai6'
            
            # Define the IGDB API endpoint
            api_url_game = 'https://api.igdb.com/v4/games'
            # id = request.GET.get('id','')
    
            # Define the parameters for the API request
            params_game = {
                'fields': f'id, name, cover.image_id, summary, total_rating, platforms; where id = {id}',  # Specify the fields you want to retrieve
            }
    
            # Set up headers with your API key
            headers = {
                'Client-ID': client_id,
                'Authorization': f'Bearer {api_token}',
                'grant_type':'client_credentials',

            }
    
            # Make the API request
            response_game = requests.post(api_url_game, headers=headers, params=params_game)
            # response_cover = requests.post(api_url_cover, headers=headers, params=params_cover)
    
            # Check if the request was successful (status code 200)
            if response_game.status_code == 200:
                # Parse the JSON response
                data_game = response_game.json()
                data_game[0]['total_rating'] = round(data_game[0]['total_rating']/10, 2) # Redondeo a 2 decimales

                # Obtener el nombre de las plataformas:
                platforms = data_game[0]['platforms']
                platforms = [int(platform) for platform in platforms]
                api_url_platform = 'https://api.igdb.com/v4/platforms'
                params_platform = {
                    'fields': f'name; where id = ({", ".join(map(str, platforms))})',  # Specify the fields you want to retrieve
                }
                response_platform = requests.post(api_url_platform, headers=headers, params=params_platform)
                if response_platform.status_code == 200:
                    data_platform = response_platform.json()
                    data_game[0]['platforms'] = data_platform
                    return render(request, 'game_detail.html', {'game': data_game,})
                else:
                    return render(request, 'error.html', {'message': f'Error obteniendo datos: {response_platform.status_code}'})
                
                
                
            else:
                # Display an error message if the request was unsuccessful
                return render(request, 'error.html', {'message': f'Error obteniendo datos: {response_game.status_code}'})
            
    else:
        return render(request, 'error.html', {'message': 'Método no permitido'})


@login_required
def add_to_wishlist(request):
    game_id = request.GET.get('game_id')
    if game_id is not None:
        profile = Profile.objects.get(user=request.user)
        if str(game_id) not in profile.wishlist.split(','):
            profile.wishlist += f'{game_id},'
            profile.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid game ID'})