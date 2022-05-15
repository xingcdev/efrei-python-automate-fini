from deterministe import est_deterministe, est_complet, completer


def lang_complementaire(etats, alphabet, transitions, liste_initiaux, ancien_terminaux, table_transitions):
    """Trouver le langage complémentaire d'un automate

    Args:
        etats (list): liste des états de l'automate 
        liste_initiaux (list): les états initiaux
        ancien_terminaux (list): les états terminaux (pour l'instant)
        table_transitions (list): la table de transition

    Returns:
        list_terminaux: les nouveaux états terminaux de l'automate
    """

    if not est_deterministe(liste_initiaux, table_transitions):
        print("Language complémentaire impossible car non déterministe")
        # On renvoie 3 listes suivantes non modifées.
        return

    if not est_complet(table_transitions):
        print("L'automate n'est pas complet. Complétion...")
        completer(
            alphabet, etats, transitions, table_transitions)

    nouv_terminaux = []
    for etat in etats:
        if etat not in ancien_terminaux:
            nouv_terminaux.append(etat)

    # On renvoie la nouvelle liste des états terminaux
    return nouv_terminaux
