# -*- coding: utf-8 -*-
__author__ = 'VARGAS Jose'

import sqlite3, os

reqCreat = """
CREATE TABLE IF NOT EXISTS `portable` (
  `id` INTEGER NOT NULL,
  `modele` VARCHAR(45) NOT NULL,
  `fabriquant` VARCHAR(45) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `talleEcran` DOUBLE,
  `prix` DOUBLE NOT NULL,
  `distributeur` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`)
);
"""
#
reqInsert = [
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('iPhone 4','Apple','Telephone',3.5,300,'SFR');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('iPhone 5','Apple','Telephone',4,400,'Orange');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('Galaxy SIII','Samsung','Telephone',4.8,180,'Bouygues');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('Lumia','Nokia','Telephone',3.7,98,'Orange');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('Desire C','HTC','Telephone',3.5,60,'Bouygues');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('iPad','Apple','Tablet',9.7,450,'Orange');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('iPhone 5','Apple','Telephone',4,400,'SFR');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('Galaxy SII','Samsung','Telephone',4.27,70.5,'SFR');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('iPhone 5','Apple','Telephone',4,400,'Bouygues');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('Galaxy Nexus','Samsung','Telephone',4.65,350,'Orange');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('Galaxy S','Samsung','Telephone',4,49.9,'Bouygues');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('Note 2','Samsung','Tablet',5.5,280,'Bouygues');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('Note 2','Samsung','Tablet',5.5,280,'SFR');", \
    "INSERT INTO `portable` (modele,fabriquant,type,talleEcran,prix,distributeur) VALUES ('Note 2','Samsung','Tablet',5.5,280,'Orange');"]

print("Pour info, dans le repertoire courant : \n", os.listdir("."))
fich = raw_input("Entrez le nom du fichier à créer (contenant la base!) : ")
fich = fich + ".sqlite3"
db = sqlite3.connect(fich.strip())
cursor = db.cursor()
cursor.execute(reqCreat)
for req in reqInsert:
    cursor.execute(req)
cursor.close()
db.commit()
db.close()
q = raw_input('Une touche pour finir')