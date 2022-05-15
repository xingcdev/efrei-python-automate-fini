from reconnaissance_mot import mot_reconnu
from standardisation import est_standard, standardiser, mot_vide_reconnu, eliminer_mot_vide, ajouter_mot_vide
from table_transitions import construire_table_transitions, afficher_table_transitions
from deterministe import est_deterministe, est_complet
from complementaire import lang_complementaire


def filtrer_contenu(contenu, num_ligne, num_caractere, separateur):
    return contenu[num_ligne][num_caractere:].split(separateur)


def lire_fichier(chemin):
    with open(chemin, 'r') as fichier:
        # splitline permet d'enlever '\n'
        liste_lignes = fichier.read().splitlines()

        liste_alphabets = filtrer_contenu(liste_lignes, 0, 4, ',')

        liste_etats = filtrer_contenu(liste_lignes, 1, 4, ',')

        liste_initiaux = filtrer_contenu(liste_lignes, 2, 4, ',')

        liste_terminaux = filtrer_contenu(liste_lignes, 3, 4, ',')

        liste_transitions = []
        for ligne in liste_lignes[4:]:
            liste_transitions.append(ligne)

        return liste_alphabets, liste_etats, liste_initiaux, liste_terminaux, liste_transitions


def demo_automate(chemin):
    alphabet, etats, initiaux, terminaux, transitions = lire_fichier(
        chemin)

    # Remplissage de l'intérieur de la table des transitions
    # Les flèches, l'alphabet et l'état apparaissent à l'affichage
    table_transitions = construire_table_transitions(
        alphabet, etats, transitions)

    print("\n--- Affichage de la table des transitions ---")
    afficher_table_transitions(
        alphabet, etats, initiaux, terminaux, table_transitions)

    if est_deterministe(initiaux, table_transitions):
        print("L'automate est déterministe.")
    else:
        print("L'automate n'est pas déterministe")
    if est_complet(table_transitions):
        print("L'automate est complet.")
    else:
        print("l'automate n'est pas complet.")

    mot = input("Indiquez un mot à faire reconnaître par l'automate.\nSi aucun message n'indique que le mot est "
                "reconnu, c'est qu'il n'est pas reconnu.\n> ")
    if est_deterministe(initiaux, table_transitions):
        if mot_reconnu(initiaux, table_transitions, mot, alphabet, terminaux, transitions):
            print("Le mot est bien reconnu par l'automate !")
    else:
        # En cas d'automate non déterministe, la fonction fait elle-même l'affichage
        mot_reconnu(initiaux, table_transitions, mot, alphabet, terminaux, transitions)

    if not est_standard(initiaux, transitions):
        print("L'automate n'est pas standard. Voici la version standardisée :\n")
        etats_std, initiaux_std, terminaux_std, transitions_std = standardiser(etats, initiaux, terminaux, transitions)
        table_transitions_std = construire_table_transitions(alphabet, etats_std, transitions_std)
        afficher_table_transitions(alphabet, etats_std, initiaux_std, terminaux_std, table_transitions_std)
        if mot_vide_reconnu(initiaux_std, terminaux_std):
            saisie = input("Le mot vide est reconnu. Souhaitez-vous l'éliminer ? (écrivez 'oui' ou rien sinon)\n")
            if saisie == "oui":
                terminaux_std = eliminer_mot_vide(initiaux_std, terminaux_std, transitions_std)
        else:
            saisie = input("Le mot vide n'est pas reconnu. Souhaitez-vous l'ajouter ? (écrivez 'oui' ou rien sinon)\n")
            if saisie == "oui":
                terminaux_std = ajouter_mot_vide(initiaux_std, terminaux_std, transitions_std)
        print("Table de transition standard après modification éventuelle :")
        afficher_table_transitions(alphabet, etats_std, initiaux_std, terminaux_std, table_transitions_std)

    terminaux = lang_complementaire(
        etats, alphabet, transitions, initiaux, terminaux, table_transitions)

    # Si on a réussi à obtenir le langage complémentaire
    if est_deterministe(initiaux, table_transitions):
        print("Langage complémentaire à l'automate d'origine : ")
        table_transitions = construire_table_transitions(
            alphabet, etats, transitions)
        afficher_table_transitions(
            alphabet, etats, initiaux, terminaux, table_transitions)


def main():
    while True:
        num = input("\nEntrez le numéro de l'automate à tester (entre 1 et 7)\n")
        if 0 < int(num) < 8:
            demo_automate('demo/automate' + num + '.txt')
        else:
            print("Veuillez saisir un chiffre entre 1 et 7.")


main()
