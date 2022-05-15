def construire_table_transitions(alphabets, etats, transitions):
    table_transitions = [
        [' ' for _ in range(len(alphabets))] for _ in range(len(etats))]
    for transition in transitions:
        temp = transition.split(',')
        ligne = etats.index(temp[0])
        col = alphabets.index(temp[1])

        if table_transitions[ligne][col] != ' ':
            # Ajout d'une transition sans écraser la précédente
            cellule = table_transitions[ligne][col].split(',')
            if temp[2] not in cellule:
                table_transitions[ligne][col] += ',' + temp[2]

        else:
            table_transitions[ligne][col] = temp[2]
    return table_transitions


def afficher_table_transitions(alphabets, etats, initiaux, terminaux, table_transitions):

    # Affichage de la première ligne : alphabet
    for i in range(len(alphabets)):
        if i == 0:
            print('     |', alphabets[i], end='')
        else:
            print('| ', alphabets[i], end='')

    # Affichage du reste de la table (flèches, états et transitions)
    for i in range(len(table_transitions)):
        print()
        fleche = get_fleche(etats[i], initiaux, terminaux)
        print(fleche, etats[i], '| ', end='')
        for j in range(len(alphabets)):
            if table_transitions[i][j] is None:
                print('   ', end='')
            else:
                print(table_transitions[i][j], '  ', end='')

    # Retour à la ligne
    print("")


def get_fleche(etat, etats_initiaux, etats_terminaux):
    if etat in etats_initiaux and etat in etats_terminaux:
        return "↔"
    elif etat in etats_initiaux:
        return "→"
    elif etat in etats_terminaux:
        return "←"
    else:
        return " "
