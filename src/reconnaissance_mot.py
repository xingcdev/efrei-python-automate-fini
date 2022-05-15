from deterministe import est_deterministe


def get_etat_cible(etat, symbole_courant, transitions):
    """
    Obtenir l'état cible d'une transition d'un état par un symbole donné.
    Il faut pour cela que l'automate soit déterministe
    :param etat:
    :param symbole_courant:
    :param transitions:
    :return:
    """
    for transition in transitions:
        temp = transition.split(',')
        # transition : [etat_depart, symbole, etat_arrivée]
        if temp[0] == etat and temp[1] == symbole_courant:
            return temp[2]
    return '#'


# Reconnaissance de mot
def mot_reconnu(initiaux, table_transitions, mot, alphabet, terminaux, transitions):
    etat_actuel = False
    if est_deterministe(initiaux, table_transitions):
        etat_courant = initiaux[0]
        symbole_courant = mot[0] if len(mot) != 0 else ''
        cpt = 0
        while True:
            if cpt == len(mot):
                if etat_courant in terminaux:
                    return True
                else:
                    return False
            etat_cible = get_etat_cible(etat_courant, symbole_courant, transitions)

            # s'il existe une transition (courant,symbole,cible)
            if (etat_courant + ',' + symbole_courant + ',' + etat_cible) in transitions:
                etat_courant = etat_cible
                cpt += 1
                if cpt < len(mot):
                    symbole_courant = mot[cpt]
            else:
                return False

    else:
        if mot == '':
            for etat in initiaux:
                if etat in terminaux:
                    print("Le mot est bien reconnu par l'automate !")
                    return True

        fini = False
        j = 0
        x = 0
        for lettre in mot:
            j = j + 1
            i = 0
            if lettre in alphabet:
                i = alphabet.index(lettre)
            else:
                return False
            for ligne in range(len(table_transitions)):
                z = -1
                for iInitial in initiaux:
                    z = z + 1
                    if ligne == int(iInitial) - 1:
                        for colonne in range(len(table_transitions[ligne])):
                            if colonne == i:
                                etat_actuel = table_transitions[ligne][colonne]
                                if etat_actuel.find(',') == True: # Ne pas simplifier cette expression
                                    test = etat_actuel.split(',')
                                    for etat in test:
                                        recursive_non_deterministe(fini, table_transitions, alphabet, terminaux, x, j,
                                                                   etat,
                                                                   mot[1:])
                                        if fini:
                                            print("On a trouvé que l'automate reconnait le mot")
                                            return fini
                                else:
                                    # x = 0
                                    recursive_non_deterministe(fini, table_transitions, alphabet, terminaux, x, j,
                                                               etat_actuel,
                                                               mot[1:])
                                    if fini:
                                        print("On a enfin trouvé que l'automate reconnait le mot")
                                        return fini


def recursive_non_deterministe(fini, table_transitions, alphabet, terminaux, i, j, etat_actuel, mot):
    if fini:
        return fini
    for lettre in mot:
        i = 0
        while lettre != alphabet[i]:
            i = i + 1
            if len(alphabet) < i < 0:
                print("ERREUR LA LETTRE N'EXISTE PAS DANS L'ALPHABET")
                return False
        if i > len(alphabet):
            return -1
        for ligne in range(len(table_transitions)):
            if etat_actuel and etat_actuel != ' ':
                if ligne == int(etat_actuel) - 1:
                    for colonne in range(len(table_transitions[ligne])):
                        if colonne == i:
                            etatActuel1 = table_transitions[ligne][colonne]
                            if etat_actuel == " " or etat_actuel == "" or etat_actuel == "  ":
                                break

                            elif etatActuel1.find(',') == True:
                                test = etatActuel1.split(',')
                                for etat in test:
                                    x = 0
                                    recursive_non_deterministe(fini, table_transitions, alphabet, terminaux, x, j, etat,
                                                               mot[1:])
                            else:
                                if etatActuel1 in terminaux and len(mot) == 1:
                                    print("Le mot est bien reconnu par l'automate !")
                                    fini = True
                                    return fini

                                etat = etatActuel1
                                x = 0
                                recursive_non_deterministe(fini, table_transitions, alphabet, terminaux, x, j, etat,
                                                           mot[1:])
