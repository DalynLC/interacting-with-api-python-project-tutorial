import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

artist_id = "6RHTUrRF63xao58xh9FXYJ"
canciones = []
popularidad = []
duracion = []

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret))
results = spotify.artist_top_tracks(artist_id)

for track in results['tracks'][:10]:
    canciones.append(track['name'])
    popularidad.append(track['popularity'])
    duracion.append(track['duration_ms']/(1000*60)%60)

datos = {
    'Titles': canciones,
    'Popularidad': popularidad,
    'Duracion': duracion
}

df = pd.DataFrame(datos)
df = df.sort_values(by = 'Popularidad')
print(df)

scatter_plot = sns.scatterplot(data = df, y ='Popularidad', x = 'Duracion')

# Etiquetas y título
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot1.png")