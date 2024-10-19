from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route("/")
def profile():
    return render_template('profile.html')

@app.route("/courses")
def courses():
    return render_template('courses.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')

@app.route("/rating")
def rating():
    return render_template('rating.html')

@app.route("/course/basic-test")
def basic_test():
    return render_template('/course/basic-test.html')

@app.route("/course/smart-contracts")
def smart_contracts():
    return render_template('/course/smart-contracts.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
