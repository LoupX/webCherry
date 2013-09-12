# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy import and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, Float
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import func

Base = declarative_base()


class Portable(Base):
    __tablename__ = 'portable'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    modele = Column(String)
    fabriquant = Column(String)
    type = Column(String)
    talleEcran = Column(Float)
    prix = Column(Float)
    distributeur = Column(String)

    def __init__(self, modele, fabriquant, type, prix, distributeur):
        self.id = None
        self.modele = modele
        self.fabriquant = fabriquant
        self.type = type
        self.prix = prix
        self.distributeur = distributeur

    def __str__(self):
        return "{};{};{};{};{}€".format(self.fabriquant, self.modele,self.type, self.distributeur,self.prix)


class BDEError(Exception):
    def __init__(self, mess):
        self.mess = mess

    def __str__(self):
        return self.mess


class BDPortableORM:
    def __init__(self, dbName="db.sqlite3"):
        self.dbName = dbName
        self.session = None
        if not os.path.isfile(dbName):
            raise BDEError(
                "Connexion avec la base de données a échoué :\nErreur detectee : {} n'existe pas\n".format(dbName))
        try:
            engine = create_engine('sqlite:///' + dbName, echo=True)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise BDEError('Connexion avec la base de donnees a echoue :\nErreur detectee :\n%s' % err)

    def reset(self):
        """ Remise à zéro de la table """
        for port in self.session.query(Portable):
            self.session.delete(port)
        self.session.commit()

    def __str__(self):
        s = ''
        for port in self.session.query(Portable):
            s = s + str(port) + "\n"
        return s

    def maj(self):
        self.session.commit()

    def getParPrix(self):
        """
        Aficher les portables par prix décroissant.
        """
        s = ''
        for port in self.session.query(Portable).order_by(Portable.prix.desc()):
            s = s + str(port) + "\n"
        return s

    def getParFab(self):
        s = ''
        for port in self.session.query(Portable).order_by(Portable.fabriquant):
            s = s + str(port) + "\n"
        return s

    def getMoinCher(self):
        port = self.session.query(Portable).order_by(Portable.prix.asc()).first()
        return str(port)

    def ajPortable(self, mod, fab, typ, prix, dist):
        """ Insertion d'un étudiant dans la collection"""
        port = Portable(mod, fab, typ, float(prix), dist)
        self.session.add(port)
        self.session.commit()

    def filtPort(self, nomFab):
        """Filtrar"""
        s = ''
        for port in self.session.query(Portable).filter(Portable.fabriquant == str(nomFab)):
            s = s + str(port) +"\n"
        return s

    def getAllFab(self):
        s = ''
        for port in self.session.query(Portable).distinct(Portable.fabriquant):
            s = s + str(port)+'\n'
        return s

    def efPortable(self, mod, dist):
        """ Suppression d'un (ou plusieurs) étudiant dans la collection"""
        for port in self.session.query(Portable).filter(and_(Portable.modele == mod, Portable.distributeur == dist)):
            self.session.delete(port)
        self.session.commit()

