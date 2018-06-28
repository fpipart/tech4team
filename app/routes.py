from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.models import File
import io
import csv

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def uploadXlsm():
    if request.method == 'POST':
        print('POST')
        f = request.files['fileToUpload']
        if not f:
            return "No file"
        stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream, delimiter=';')
        first_line = 0
        try:
            for i in csv_input:
                if (first_line == 0):
                    first_line = 1
                else:
                    record = File(**{
                        'Numero_billet' : i[0],
                        'Reservation' : i[1],
                        'Date_reservation' : i[2],
                        'Heure_reservation' : i[3],
                        'Cle_spectacle' : i[4],
                        'Spectacle' : i[5],
                        'Cle_representation' : i[6],
                        'Representation' : i[7],
                        'Date_representation' : i[8],
                        'Heure_representation' : i[9],
                        'Date_fin_representation' : i[10],
                        'Heure_fin_representation' : i[11],
                        'Prix' : i[12],
                        'Type_de_produit' : i[13],
                        'Filiere_de_vente' : i[14],
                        'Nom' : i[15],
                        'Prenom' : i[16],
                        'Email' : i[17],
                        'Adresse' : i[18],
                        'Code_postal' : i[19],
                        'Pays' : i[20],
                        'Age' : i[21],
                        'Sexe' : i[22]
                    })
                    db.session.add(record)
                    db.session.commit()
        except:
            db.session.rollback()
        return render_template('upload.html')
