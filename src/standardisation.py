nouvel_etat = 'i'


def est_standard(initiaux, transitions):
    # Un seul état initial
    if len(initiaux) == 1:
        etat_initial = initiaux[0]
        for transition in transitions:
            temp = transition.split(',')
            # Aucune transition ne doit arriver sur l'état initial
            if temp[2] == etat_initial:
                return False
        return True
    return False


def standardiser(etats, initiaux, terminaux, transitions):
    """
    Standardise un automate
    :param etats: Liste de tous les états
    :param initiaux: Liste des états initiaux
    :param terminaux: Liste des états terminaux
    :param transitions: Liste des transitions
    :return: Nouvelles listes d'états, d'états initiaux, d'états terminaux et de transitions
    """
    etats_std = etats.copy()
    terminaux_std = terminaux.copy()
    transitions_std = transitions.copy()

    initiaux_reconnait_mot_vide = False
    for etat in initiaux:
        if etat in terminaux:
            initiaux_reconnait_mot_vide = True
        for transition in transitions:
            temp = transition.split(',')
            if temp[0] == etat:
                transitions_std.append(nouvel_etat + ',' + temp[1] + ',' + temp[2])
    initiaux_std = [nouvel_etat]
    etats_std.append(nouvel_etat)
    if initiaux_reconnait_mot_vide:
        terminaux_std.append(nouvel_etat)
    return [etats_std, initiaux_std, terminaux_std, transitions_std]


def ajouter_mot_vide(initiaux, terminaux, transitions):
    terminaux_std = terminaux.copy()
    # Le seul état initial devient donc également terminal
    if est_standard(initiaux, transitions):
        terminaux_std.append(initiaux[0])
    return terminaux_std


def eliminer_mot_vide(initiaux, terminaux, transitions):
    terminaux_std = terminaux.copy()
    # On enlève l'état de standardisation des états terminaux
    if est_standard(initiaux, transitions):
        terminaux_std.remove(nouvel_etat)
    return terminaux_std


def mot_vide_reconnu(initiaux, terminaux):
    # Si l'un des états initiaux est également terminal, le mot vide est reconnu
    for etat in initiaux:
        if etat in terminaux:
            return True
    return False
