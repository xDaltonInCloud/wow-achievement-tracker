# WoW Achievement Tracker

**Description**  
The WoW Achievement Tracker is a Python-based web application that retrieves, processes, and displays *World of Warcraft* character achievements using the Blizzard API. This project demonstrates API integration, data processing, and web visualization using Flask.

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Modules](#modules)
- [Example](#example)
- [License](#license)

---

## Features

- Authentication with Blizzard API
- Fetches and processes character achievement data
- Displays achievements with progress bars and completion rates
- Optional goal tracking and notifications

## Requirements

- Python 3.x
- Flask
- Requests
- ConfigParser

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wow-achievement-tracker.git
   cd wow-achievement-tracker

Install required libraries:

    pip install -r requirements.txt

Configuration

    Create a config.ini file with your Blizzard API credentials.

    Example configuration:

    [blizzard_api]
    client_id = your_blizzard_client_id
    client_secret = your_blizzard_client_secret
    region = us

    Note: Do not include config.ini in version control for security reasons. Use .gitignore to exclude it and consider providing a config_sample.ini file as an example.

Usage

    Start the Flask application:

    python visualization_ui.py

    Open your browser and go to http://127.0.0.1:5000.

Modules

    API Integration Module (api_integration.py):
        Handles authentication with the Blizzard API and retrieves character achievement data.
        Functions:
            authenticate(): Authenticates with the Blizzard API using OAuth2, retrieving an access token.
            get_character_achievements(realm, character_name): Retrieves achievements for a specified character.

    Data Processing Module (data_processing.py):
        Processes raw data into structured achievements and calculates completion rates.
        Functions:
            process_achievements(): Extracts relevant fields from raw achievement data.
            calculate_completion_rate(achievements): Calculates the percentage of completed achievements.

    Visualization & UI Module (visualization_ui.py):
        Uses Flask to create a simple web interface for displaying achievement data.
        Routes:
            /: Displays a form for entering character and realm information.
            /character: Retrieves and displays achievements for a specified character.

    Notifications & Goal Tracker Module (Optional) (notifications_goals.py):
        Allows users to set achievement completion goals and receive notifications when goals are met.
        Functions:
            set_goal(target_completion_rate): Sets a target completion rate for achievements.
            check_goal(current_completion_rate): Checks if the target goal has been reached.

Example

    Go to http://127.0.0.1:5000 in your browser.
    Enter a character’s realm and name, then submit.
    View the achievements and completion rate displayed on the page.

License

This project is licensed under the MIT License.
