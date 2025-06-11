from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def profile():
    # Profil tetap
    your_name = "Imba"
    lover_name = "Jingga"
    date_anniversary = datetime.strptime("2022-08-29", "%Y-%m-%d")

    # Perhitungan hari bersama
    days = (datetime.now() - date_anniversary).days
    date_formatted = date_anniversary.strftime("%d %B %Y")

    # Kata-kata romantis (tidak lebay)
    message = f"""
    {lover_name} & {your_name} ❤️

    Bersama sejak {date_formatted}, telah melewati {days} hari yang penuh warna.
    Terima kasih telah menjadi bagian dari hidup ini, 
    dalam tawa, pelukan, dan keheningan yang paling hangat.
    """

    return render_template("love.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)