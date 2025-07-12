from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

quotes = [
    "kejayaan bermula dengan langkah pertama. 💪",
    "jangan pernah putus asa. Setiap hari adalah peluang baru. 🌞",
    "kamu hebat dan luar biasa. Teruskan usaha! 🚀",
    "ingat… usaha + doa = kejayaan. 🙏📘",
    "walaupun perlahan, teruskan berjalan. 🐢💖",
    "hari ini lebih baik dari semalam! 🔥",
    "kamu dilahirkan untuk berjaya. 🌟",
    "teruskan walau sukar. Kejayaan milik mereka yang tidak berputus asa. 💼🔥",
    "setiap kegagalan adalah batu loncatan ke arah kejayaan. 📈💡",
    "percayalah pada diri sendiri. Kamu lebih kuat dari yang kamu sangka. 🛡️🌈",
    "ilmu itu cahaya. Terus belajar, terus bersinar. 📚✨",
    "jangan takut gagal. Takutlah jika tidak mencuba langsung. 🚀❌",
    "kejayaan tidak datang dengan mudah, tetapi ia sangat berbaloi. 🏆💪",
    "kamu tidak bersendirian. Kami semua menyokong kamu! 👏🤝",
    "hari ini kamu belajar, esok kamu akan memimpin. 🎓🌟",
    "jangan bandingkan diri kamu dengan orang lain. Jadilah versi terbaik dirimu. 🧭❤️",
    "dengan disiplin dan usaha, tiada apa yang mustahil. ⏳🏋️‍♂️"
]

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = "eja"
        message = f"{name}, {random.choice(quotes)}"
    return render_template_string("""
        <html>
        <head>
            <title>Kata Motivasi for Eja</title>
            <style>
                body { font-family: Arial; padding: 20px; text-align: center; background: #f5f5f5; }
                button { padding: 12px 20px; font-size: 16px; margin-top: 20px; cursor: pointer; }
                h2 { color: #333; }
                h3 { color: #007700; margin-top: 30px; }
            </style>
        </head>
        <body>
            <h2>🎉  Hi Syg, Kata Motivasi for you hari ini .🎉</h2>
            <form method="POST">
                <button type="submit">Dapatkan kata Motivasi</button>
            </form>
            <h2>Have a fantastic day, love you <3</h2>
            <h3>{{ message }}</h3>
        </body>
        </html>
    """, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
