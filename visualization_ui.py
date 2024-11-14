from flask import Flask, render_template, request
from api_integration import BlizzardAPI
from data_processing import AchievementProcessor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/character', methods=['POST'])
def character_achievements():
    realm = request.form['realm']
    character_name = request.form['character_name']
    
    # Fetch data from Blizzard API
    blizzard_api = BlizzardAPI()
    raw_data = blizzard_api.get_character_achievements(realm, character_name)
    
    # Process achievement data
    if raw_data:
        processor = AchievementProcessor(raw_data)
        achievements = processor.process_achievements()
        completion_rate = processor.calculate_completion_rate(achievements)
        
        return render_template(
            'character.html', 
            achievements=achievements, 
            completion_rate=completion_rate,
            character_name=character_name,
            realm=realm
        )
    else:
        return render_template('error.html', message="Failed to retrieve char
