# -*- coding: utf-8 -*-

class fonctions():


    def traitementString(self, l):

        liste = str(l)
        liste = liste.split('€')
        self.string = '''<div class="row">
                        <table class="center">
                        <tr>
                            <th>Fabriquant</th>
                            <th>Modele</th>
                            <th>Type</th>
                            <th>Distributeur</th>
                            <th>Prix</th>
                        </tr>
                    '''
        for x in range((len(liste)) - 1): #Por cada linea, separa en elementos después del ';'
            ligne = liste[x].split(';')
            self.string += '<tr>\n'             #inicializo el string para empezar la nueva línea

            for y in range(len(ligne)): #Para cada elemento en la linea creada en el primer FOR
                self.string += '<td> {} </td>\n'.format(ligne[y])
            self.string += '</tr>\n'
        self.string += '</table></div>\n'
        return self.string