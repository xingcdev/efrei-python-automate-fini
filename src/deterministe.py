def est_complet(table_transitions):
    """Vérifier si pour tout état, il existe au moins une transition pour chaque symbole de l'alphabet

    Args:
        table_transitions (list): table sous forme de liste à 2 dimensions

    Returns:
        boolean: est complet ou non
    """
    for ligne in range(len(table_transitions)):
        for colonne in range(len(table_transitions[ligne])):
            etat_actuel = table_transitions[ligne][colonne]
            if etat_actuel == " ":
                return False
    return True


def completer(alphabet, etats, transitions, table_transitions):
    """ Complète un automate

    :param alphabet: Alphabet du langage
    :param etats: Liste des états
    :param transitions: Liste des transitions [source,symbole,destination]
    :param table_transitions: Table de transitions
    :return: Nouvelles listes d'états et de transitions
    """
    junk_state = 'P'
    junk_state_added = False

    for ligne in range(len(table_transitions)):
        for colonne in range(len(table_transitions[ligne])):
            if table_transitions[ligne][colonne] == " ":
                if not junk_state_added:
                    etats.append(junk_state)
                    for i in range(len(alphabet)):
                        transitions.append(junk_state + ',' + alphabet[i] + ',' + junk_state)
                    junk_state_added = True
                transitions.append(etats[ligne] + ',' + alphabet[colonne] + ',' + junk_state)
    return etats, transitions


def est_deterministe(liste_initiaux, table_transitions):
    """Un automate est déterministe s'il y a qu'un seul état initial et 
    plusieurs transitions d'un même alphabet sur un état

    Args:
        liste_initiaux (list): liste des états initiaux
        table_transitions (list): table sous forme de liste à 2 dimensions

    Returns:
        boolean: est déterministe ou non
    """

    # S'il y a plusieurs états initiaux
    if len(liste_initiaux) != 1:
        return False

    for ligne in range(len(table_transitions)):
        for colonne in range(len(table_transitions[ligne])):
            etat_actuel = table_transitions[ligne][colonne]

            if "," in etat_actuel:
                return False

    return True
