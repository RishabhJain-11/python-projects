import requests

def get_anime_list(anime_name):
    query = '''
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        title {
          romaji
          english
        }
        genres
        description
      }
    }
    '''

variables = {
    'search'
}