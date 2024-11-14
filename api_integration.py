import requests
import configparser
import os
from urllib.parse import urlencode

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

class BlizzardAPI:
    def __init__(self):
        self.client_id = config['blizzard_api']['client_id']
        self.client_secret = config['blizzard_api']['client_secret']
        self.region = config['blizzard_api']['region']
        self.access_token = None

    def authenticate(self):
        # Authenticate with Blizzard OAuth
        url = f"https://{self.region}.battle.net/oauth/token"
        response = requests.post(
            url,
            data={'grant_type': 'client_credentials'},
            auth=(self.client_id, self.client_secret)
        )
        
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            print("Authentication successful!")
        else:
            print(f"Failed to authenticate: {response.status_code}")
            self.access_token = None

    def get_character_achievements(self, realm, character_name):
        # Ensure authenticated
        if not self.access_token:
            self.authenticate()
        
        # Fetch character achievements
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realm}/{character_name}/achievements"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Battlenet-Namespace': 'profile-us'
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()  # Returns JSON data with achievements
        else:
            print(f"Failed to retrieve achievements: {response.status_code}")
            return None
