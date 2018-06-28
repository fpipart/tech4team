from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
import io
import sys
import pandas as pd

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
        df = pd.read_csv(stream, sep=';')
        try:
            df.to_sql(name='tickets', con=db.engine, index=False)
        except:
            print('Can\'t load the databse')
        return render_template('upload.html')

@app.route('/resume')
def resume():
    try:
        df = pd.read_sql('SELECT * FROM tickets', db.engine)
        print('-----------------Mesure 1-----------------')
        countRes = df['Reservation'].value_counts()
        print('le nombre de reservation est de :', countRes.size)
        print('-----------------Mesure 2-----------------')
        df['acheteur'] = df['Nom'] + '-' +df['Prenom']
        countBuyer = df['acheteur'].value_counts()
        print('Le nombre d\'acheteur unique est de :' + str(countBuyer.size))
        print('-----------------Mesure 3-----------------')
        dfBuyer = df[['acheteur', 'Age']].drop_duplicates('acheteur')
        dfBuyer['Age'] = pd.to_numeric(dfBuyer['Age'])
        meanAge = dfBuyer['Age'].mean()
        print('L\'age moyen des acheteurs est de : ', meanAge)
        print('-----------------Mesure 4-----------------')
        dfRepresentation = df[['Representation', 'Prix']].drop_duplicates('Representation')
        # print('Prix de la representation :')
        # print(dfRepresentation)
        print('Prix moyen d\'une representation : ', dfRepresentation['Prix'].mean())
        print('-----------------Mesure 5-----------------')
        dfBuyerTotalPrice = df.groupby(['acheteur'],as_index = False).sum()
        dfBuyerTotalPrice = dfBuyerTotalPrice[['acheteur','Prix']]
        # print('Prix total payé par chaque acheteur')
        # print(dfBuyerTotalPrice)
        print('Prix moyen payé par un acheteur : ', dfBuyerTotalPrice['Prix'].mean())
    except:
        print('Invalid table!')
    return render_template('upload.html')