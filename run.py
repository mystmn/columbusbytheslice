from flask import Flask, render_template
app = Flask(__name__)

#  https://deliciouslyella.com/videos/

@app.route('/')
def index():
    name = ""
    return render_template('index.html')

@app.route('/videos')
def beta():
    return render_template('videos.html')

if __name__ == "__main__":
    app.run()