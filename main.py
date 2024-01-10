import subprocess
import random
import string
import os

# Replace 'YOUR_TEAM_NAME' with your actual team name
TEAM_NAME = 'ffff'

# Replace 'YOUR_API_KEY' with your actual Heroku API key
HEROKU_API_KEY = 'e8797279-f5d1-488f-aaf0-9ac05c35e779'

# Set the Heroku API key as an environment variable
os.environ['HEROKU_API_KEY'] = HEROKU_API_KEY

# Function to generate a random app name
def generate_random_name():
    random_suffix = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f'{TEAM_NAME}-app-{random_suffix}'

# Loop to create 10 apps with random names
for _ in range(30):
    app_name = generate_random_name()

    # Heroku CLI command to create an app
    command = f'heroku create --region us --stack container {app_name} --team {TEAM_NAME}'

    # Run the Heroku CLI command using subprocess
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        print(f'App {app_name} created successfully.')
    else:
        print(f'Error creating app {app_name}. Error: {result.stderr.strip()}')
