from datetime import datetime
from app import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Numero_billet = db.Column(db.Integer, index=True)
    Reservation = db.Column(db.Integer)
    Date_reservation = db.Column(db.String(64))
    Heure_reservation = db.Column(db.String(64))
    Cle_spectacle = db.Column(db.Integer)
    Spectacle = db.Column(db.String(64))
    Cle_representation = db.Column(db.Integer)
    Representation = db.Column(db.String(64))
    Date_representation = db.Column(db.String(64))
    Heure_representation = db.Column(db.String(64))
    Date_fin_representation = db.Column(db.String(64))
    Heure_fin_representation = db.Column(db.String(64))
    Prix = db.Column(db.Integer)
    Type_de_produit = db.Column(db.String(64))
    Filiere_de_vente = db.Column(db.String(64))
    Nom = db.Column(db.String(64))
    Prenom = db.Column(db.String(64))
    Email = db.Column(db.String(64))
    Adresse = db.Column(db.String(64))
    Code_postal = db.Column(db.Integer)
    Pays = db.Column(db.String(64))
    Age = db.Column(db.Integer)
    Sexe = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.username)
