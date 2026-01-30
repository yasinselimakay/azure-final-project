import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ÖNEMLİ: Azure Environment Variable'dan okuyoruz
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Veritabanı Tablosu
class Kitap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isim = db.Column(db.String(100), nullable=False)
    yazar = db.Column(db.String(100), nullable=False)

# Tabloyu oluştur (Uygulama ilk açıldığında)
with app.app_context():
    db.create_all()

# ANA SAYFA - Listeleme
@app.route('/')
def index():
    kitaplar = Kitap.query.all()
    # Basit HTML arayüzü (Senin gönderdiğin buton stiline benzer renkler ekledim)
    html = """
    <body style="font-family:sans-serif; background:#f4f7f6; padding:20px;">
        <h2 style="color:#2D8B9A;">Azure Kitaplık Yönetimi</h2>
        <form action="/ekle" method="POST" style="margin-bottom:20px;">
            <input name="isim" placeholder="Kitap Adı" required>
            <input name="yazar" placeholder="Yazar" required>
            <button type="submit" style="background:#2D8B9A; color:white; border:none; padding:5px 15px; border-radius:5px;">Ekle</button>
        </form>
        <table border="1" style="width:100%; border-collapse:collapse; background:white;">
            <tr style="background:#eee;"><th>Kitap</th><th>Yazar</th><th>İşlem</th></tr>
    """
    for k in kitaplar:
        html += f"<tr><td>{k.isim}</td><td>{k.yazar}</td><td><a href='/sil/{k.id}' style='color:red;'>Sil</a></td></tr>"
    html += "</table></body>"
    return html

# EKLEME İŞLEMİ
@app.route('/ekle', methods=['POST'])
def ekle():
    yeni_kitap = Kitap(isim=request.form.get('isim'), yazar=request.form.get('yazar'))
    db.session.add(yeni_kitap)
    db.session.commit()
    return redirect('/')

# SİLME İŞLEMİ
@app.route('/sil/<int:id>')
def sil(id):
    kitap = Kitap.query.get(id)
    db.session.delete(kitap)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run()
