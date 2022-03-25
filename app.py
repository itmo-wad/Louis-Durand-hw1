from flask import Flask, render_template, redirect
import random

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

@app.route("/")
def goToProfile():
    return redirect("/profile")

@app.route('/profile')
def profile():
    stylesheet = app.static_url_path + "/css/style.css"
    images = [
        "/static/img/aliosha_view.jpg",
        "/static/img/murmansk_train_station.jpg",
        "/static/img/neva.jpg",
    ]
    return render_template('profile.html', luckyNbr=random.randint(0,13), stylesheet=stylesheet, images=images)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)