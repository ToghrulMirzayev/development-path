from flask import Flask, render_template
from teams import manage_teams_bp
from developer import manage_skills_bp

app = Flask(__name__)

@app.route('/')
def buttons():
    return render_template('index.html')

app.register_blueprint(manage_teams_bp)
app.register_blueprint(manage_skills_bp)

if __name__ == "__main__":
    app.run()
