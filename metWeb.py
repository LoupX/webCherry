# -*- coding: utf-8 -*-
import cherrypy
from requetes import BDPortableORM
from funciones import fonctions
import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))


class Web():

    def head(self):
        _head = '''
                <!doctype html>
                <!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
                <!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en"> <![endif]-->
                <!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en"> <![endif]-->
                <!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en"> <![endif]-->
                <!--[if IE 9]>    <html class="no-js ie9" lang="en" itemscope itemtype="http://schema.org/Product"> <![endif]-->
                <!-- Consider adding an manifest.appcache: h5bp.com/d/Offline -->
                <!--[if gt IE 9]><!--> <html class="no-js" lang="en" itemscope itemtype="http://schema.org/Product"> <!--<![endif]-->
                <head>
                    <meta charset="utf-8">
                    <title>Chery Py</title>
                    <link rel="stylesheet" href="https://josevargastr.koding.com/portables/css/imports.css">
                    <script src="https://josevargastr.koding.com/portables/js/libs/modernizr-2.0.6.min.js"></script>
                </head>
                <body>
        '''
        return _head
    head.exposed = True

    def nav(self):
        _nav = ('\n'
                '\n'
                '        <div class="row">\n'
                '            <p><h1 class="centrado">Portables</h1></p>\n'
                '            <nav class="pretty navbar clearfix" id="prettynav">\n'
                '                <ul>\n'
                '                    <li><a href="index">Accueil</a></li>\n'
                '                    <li><a href="#">Chercher</a>\n'
                '                        <div class="dropdown">\n'
                '                            <ul>\n'
                '                                <li><a href="trierFab">Trier par Fabricant</a></li>\n'
                '                                <li><a href="trierPrix">Trier par Prix</a></li>\n'
                '                                <li><a href="moinsCher">Moins cher</a></li>\n'
                '                            </ul>\n'
                '                        </div>\n'
                '                    </li>\n'
                '                    <li><a href="#">Administrer</a>\n'
                '                        <div class="dropdown">\n'
                '                            <ul>\n'
                '                                <li><a href="ajouterPortable">Ajouter Portable</a></li>\n'
                '                                <li><a href="effacerPortable">Effacer</a></li>\n'
                '                            </ul>\n'
                '                        </div>\n'
                '                    </li>\n'
                '                </ul>\n'
                '            </nav>\n'
                '         </div>\n'
                '        '
        )
        return _nav
    nav.exposed = True

    def foot(self):
        _foot = '''
            <footer>
                <script src="https://josevargastr.koding.com/portables/js/libs/jquery-1.7.2.min.js"></script>
                <script src="https://josevargastr.koding.com/portables/js/libs/gumby.min.js"></script>
                <script src="https://josevargastr.koding.com/portables/js/plugins.js"></script>
                <script src="https://josevargastr.koding.com/portables/js/main.js"></script>
                <div class="row inline">
                    <p>&nbsp;</p>
                </div>
                <div class="row">
                    <hr size="2" width="100%" noshade style="color:#000000" align="center" />
                    <p>Crée par VARGAS José. IUT Valence, France. 2013</p>
                </div>
            </footer>
            </body>
            </html>
        '''
        return _foot
    foot.exposed = True

    def index(self):
        _head = self.head()
        _foot = self.foot()
        _nav = self.nav()
        _corp = '''
                    <div class="row">
                        <p>Veuillez choisir une des options disponibles dans le menu de navigation</p>
                    </div>
                '''
        return _head + _nav + _corp + _foot
    index.exposed = True

    def ajouterPortable(self):
        _head = self.head()
        _nav = self.nav()
        _foot = self.foot()
        _ajout = '''
                    <div class="row">
                    <form action="ajouter" method=POST>
                        <h4>Veuillez entrer les données :</h4>
                        <table>
                        <tr><td>Modele :</td><td><input name="mod" required></td></tr>
                        <tr><td>Fabricant :</td><td><input name="fab" required></td></tr>
                        <tr><td>Type :</td><td><input name="typ" required></td></tr>
                        <tr><td>Prix :</td><td><input name="prix" required></td></tr>
                        <tr><td>Distributeur :</td><td><input name="dist" required></td></tr>
                        </table>
                        <input type=submit class="btn" value="Valider">
                    </form>
                    </div>
            '''
        return _head + _nav + _ajout + _foot
    ajouterPortable.exposed = True

    def ajouter(self,mod, fab, typ, prix, dist):
        try:
            bdd.ajPortable(str(mod), str(fab), str(typ),str(prix),str(dist))
        except (Exception, IndexError, ValueError) as err :
            raise cherrypy.HTTPRedirect('index')
        raise cherrypy.HTTPRedirect('trierPrix')
    ajouter.exposed = True

    def effacerPortable(self):
        _head = self.head()
        _nav = self.nav()
        _foot = self.foot()
        _ajout = '''
                    <div class="row">
                    <form action="effacer" method=POST>
                        <h4>Veuillez entrer les données :</h4>
                        <table>
                            <tr><td>Modele :</td><td><input name="mod" required></td></tr>
                            <tr><td>Distributeur :</td><td><input name="dist" required></td></tr>
                        </table>
                        <input type=submit class="btn" value="Valider">
                    </form>
                    </div>
            '''
        return _head + _nav + _ajout + _foot
    effacerPortable.exposed = True

    def effacer(self,mod,dist):
        try:
            bdd.efPortable(str(mod), str(dist))
        except (Exception, IndexError, ValueError) as err :
            raise cherrypy.HTTPRedirect('index')
        raise cherrypy.HTTPRedirect('trierFab')
    effacer.exposed = True

    def suprimer(self):
        _head = self.head()
        _foot = self.foot()
        _sup = '''

        '''
        return _head + _sup + _foot
    suprimer.exposed = True

    def trierFab(self):
        _head = self.head()
        _foot = self.foot()
        _nav = self.nav()
        try:
            _list = bdd.getParFab()
            _list = fon.traitementString(_list)
            return _head + _nav + _list + _foot
        except Exception as err:
            raise cherrypy.HTTPRedirect('error',303)
    trierFab.exposed = True

    def trierPrix(self):
        _head = self.head()
        _foot = self.foot()
        _nav = self.nav()
        try:
            _list = bdd.getParPrix()
            _list = fon.traitementString(_list)
            return _head + _nav + _list + _foot
        except Exception as err:
            raise cherrypy.HTTPRedirect('error',303)
    trierPrix.exposed = True

    def moinsCher(self):
        _head = self.head()
        _foot = self.foot()
        _nav = self.nav()
        try:
            _list = bdd.getMoinCher()
            _list = fon.traitementString(_list)
            return _head + _nav + _list + _foot
        except Exception as err:
            raise cherrypy.HTTPRedirect('error',303)
    moinsCher.exposed = True

    def getAllFab(self):
        fabs = bdd.getAllFab()

    def error(self):
        _head = self.head()
        _foot = self.foot()
        _nav = self.nav()
        cherrypy.engine.restart()
        _error = '''
                <div class="row center">
                    <p class="center">Ups! On avait trouvé un petit erreur</p>
                    <div class="btn" onclick="restart()" onmouseover="this.style.cursor='pointer';">Restart</div>
                    <div id="lblRestart"></div>
                </div>
                <script src="http://gigondas/web/js/main.js"></script>
                '''
        return _head + _nav + _error + _foot
    error.exposed = True


###################################################################

bdd = BDPortableORM()
fon = fonctions()
cherrypy.quickstart(Web(), config="page.conf")
