import math
from math import acos, degrees
import pandas as pd

x_player = 5
y_player = 5
player_pos = (x_player, y_player)
player_facing = "n"

carte = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]
carte = pd.DataFrame(carte)


def chercher_element_dans_carte(type_element: int, carte: pd.DataFrame):
    # liste vide
    liste = []

    # isin() va retourner une df avec des valeurs booleennes
    # où True sera la position d'un objet existant
    result = carte.isin([type_element])

    # any() method will return
    # a boolean series
    seriesObj = result.any()

    # Get list of column names where
    # element exists
    columnNames = list(seriesObj[seriesObj == True].index)

    # Iterate over the list of columns and
    # extract the row index where element exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)

        for row in rows:
            liste.append((row, col))

    # This list contains a list tuples with
    # the index of element in the dataframe
    print(liste)
    return liste


def calculer_angle(vecteur: tuple):
    """
    :param vecteur: un vecteur (x, y) qui est relatif à la position du joueur et à la position d'un point
    :return: une liste avec l'angle du point en int et la distance du point avec l'origine en int
    """
    _x = vecteur[0]
    _y = vecteur[1]
    # on évite l'erreur de division par zéro
    if _x == 0:
        _x = 0.0000000000000001
    if _y == 0:
        _y = 0.0000000000000001

    def carre(nombre):
        return nombre * nombre

    _hypotenuse = (carre(_x) + carre(_y))
    _longeur_hyp = math.sqrt(_hypotenuse)

    _resultat = degrees(acos((carre(_y) + carre(_longeur_hyp) - carre(_x)) / (2.0 * _y * _longeur_hyp)))
    # on retourne un degré en int
    # si x est négatif alors on retourne un angle de plus de 180°
    if _x < 0:
        return [360 - round(_resultat), round(_longeur_hyp)]
    # sinon on retourne un angle de moins de 180°
    else:
        return [round(_resultat), round(_longeur_hyp)]


print(calculer_angle((-2, 2)))

liste_objet = chercher_element_dans_carte(type_element=1, carte=carte)


def vectorisation(origine: tuple, arrivee: tuple):
    """
    :param origine: tuple (x, y) coordonnées du joueur
    :param arrivee: tuple (x, y) coordonnées de l'objet
    :return: un vecteur au format tuple (x, y)
    """
    return (arrivee[0] - origine[0], arrivee[1] - origine[1])


def orientation(angle: int, facing: str):
    """
    :param angle: un angle en °
    :return:
    """
    if facing == "e":
        pass
    elif facing == "s":
        angle = angle + 270
    elif facing == "o":
        angle = angle + 180
    elif facing == "n":
        angle = angle + 90
    if angle > 359:
        angle = angle - 360
    return angle


for objet in liste_objet:
    print("coordonée de l'objet {}".format(objet))
    vecteur = vectorisation(player_pos, objet)
    print("vecteur {}".format(vecteur))
    angle_distance = calculer_angle(vecteur)
    angle_distance[0] = orientation(angle=angle_distance[0], facing=player_facing)
    print("l'objet {} est à {}° et {}m de distance du joueur qui fait face au {}".format(objet, angle_distance[0],
                                                                                         angle_distance[1],
                                                                                         player_facing))
