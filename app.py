from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Baca data
    df = pd.read_csv("data.csv")

    # Ambil 5 data pertama
    head = df.head().to_html(classes="table", index=False)

    # Statistik deskriptif
    stats = df.describe().to_html(classes="table")

    # Jumlah orang per kota
    kota_count = df['Kota'].value_counts().to_frame(name='Jumlah').to_html(classes="table")

    # Rata-rata usia
    rata_rata = round(df['Usia'].mean(), 2)

    return render_template("indeks.html",
                           head=head,
                           stats=stats,
                           kota_count=kota_count,
                           rata_rata=rata_rata)

if __name__ == "__main__":
    app.run(debug=True)
