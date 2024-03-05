
# Create your views here.
from django.shortcuts import render
from .models import Profile
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from authentication.forms import UserForm
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm, ProfilePictureForm
import requests
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def profile(request, pk):
    if request.user.is_authenticated:

        profile = Profile.objects.get(user_id=pk)
        # Obtener los juegos de la wishlist:
        wishlist = profile.wishlist

        if wishlist:
            games = wishlist.split(',')
            games = [int(game) for game in games if game.isdigit()]

            # Obtener los juegos de la api:
            api_token = '8l9mgsu53ovhckv2ktpuh7f9v0bujc'
            client_id = 'oh1a4v2eabzyogqacl9a5vynyhrai6'
            
            # Define the IGDB API endpoint
            api_url_game = 'https://api.igdb.com/v4/games'
            query = request.GET.get('query','')

            # Define the parameters for the API request
            params_game = {
                'fields': f'id, name, cover.image_id, summary; where id = ({", ".join(map(str, games))})',  # Specify the fields you want to retrieve
                'limit': '200' # Adjust the limit as needed
            }

            # Set up headers with your API key
            headers = {
                'Client-ID': client_id,
                'Authorization': f'Bearer {api_token}',
                'grant_type':'client_credentials',
            }

            # Make the API request
            response_games = requests.post(api_url_game, headers=headers, params=params_game)
            # response_cover = requests.post(api_url_cover, headers=headers, params=params_cover)

            # Check if the request was successful (status code 200)
            if response_games.status_code == 200:
                # Parse the JSON response
                data_games = response_games.json()
                

            return render(request, 'profile.html', {'profile': profile, 'data': data_games})
        
        else: # Si no hay juegos en la wishlist, se renderiza la pagina sin los juegos
            return render(request, 'profile.html', {'profile': profile})
    else:
        messages.error(request, 'Debes logearte para ver esta pagina.')
        return redirect('login')
    
def edit_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user_id=request.user.id)
        form = CustomUserChangeForm(request.POST, instance=current_user)
        picture_form = ProfilePictureForm(request.POST, request.FILES, instance=profile)

        if request.method == 'POST':
            if form.is_valid() and picture_form.is_valid():
                form.save()
                picture_form.save()
                messages.success(request, 'Tu perfil ha sido actualizado.')
                return redirect('profile', pk=request.user.id)
        else:
            form = CustomUserChangeForm(instance=current_user)
            picture_form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        return render(request, 'edit_profile.html', {'form': form , 'picture_form': picture_form})
    else:
        messages.error(request, 'Debes logearte para ver esta pagina.')
        return redirect('login')
   
def remove_from_wishlist(request, game_id):
    # Get the user's profile
    profile = get_object_or_404(Profile, user_id=request.user.id)

    # Convert the wishlist into a list
    wishlist = profile.wishlist.split(',')

    # Remove the game ID from the wishlist
    if str(game_id) in wishlist:
        wishlist.remove(str(game_id))

    # Convert the wishlist back into a string
    profile.wishlist = ','.join(wishlist)

    # Save the profile
    profile.save()

    # Redirect to the profile page
    return redirect('profile', pk=request.user.id)