from flask import Flask, render_template
from teams import manage_teams_bp
from developer import manage_skills_bp
import os

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)


@app.route('/')
def buttons():
    return render_template('index.html')


app.register_blueprint(manage_teams_bp)
app.register_blueprint(manage_skills_bp)

if __name__ == "__main__":
    app.run()
