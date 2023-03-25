from flask import Flask, render_template
import yaml

app = Flask(__name__)

# Load data from YAML file
with open('jane.yaml') as file:
    resume_data = yaml.load(file, Loader=yaml.FullLoader)

# Define route for homepage
@app.route('/')
def index():
    return render_template('index.html', data=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
