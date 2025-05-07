from flask import Flask, render_template, request, send_file
from scraper import get_news_article
from script_generator import generate_script
from video_generator import create_video
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    video_path = None
    if request.method == "POST":
        topic = request.form["topic"]
        article = get_news_article(topic)
        script = generate_script(article)
        video_path = create_video(script)
    return render_template("index.html", video_path=video_path)

@app.route("/download")
def download_video():
    return send_file("output/final_video.mp4", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)