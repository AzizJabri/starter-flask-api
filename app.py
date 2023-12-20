from flask import Flask, render_template
import os
import datetime
from video_generator import VideoGenerator

RELEASE_DATE = datetime.date(2025, 9, 23)

def getDaysUntil():
    return (RELEASE_DATE - datetime.date.today()).days

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to days until gta 6 api!'

@app.route('/days_until')
def days_until():
    return 'Days until: ' + str(getDaysUntil())

@app.route("/generate")
def generate():
    # Get the day number from the URL
    day_number = getDaysUntil()

    # Get the template path
    template_path = os.path.join(os.getcwd(), 'templates', 'template.mp4')

    # Generate the reel
    reel_path = VideoGenerator.create_reel_with_day_name(day_number, template_path)

    # Return the path to the generated reel
    return reel_path

@app.route("/generate_frame")
def generate_frame():
    # Get the day number from the URL
    day_number = getDaysUntil()

    # Get the template path
    template_path = os.path.join(os.getcwd(), 'templates', 'template.mp4')

    # Generate the reel
    reel_path = VideoGenerator.generate_1_frame(day_number, )

    # Return the path to the generated reel
    return reel_path

