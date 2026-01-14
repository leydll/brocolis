def calculer_moyenne(liste):
    if not liste:
        return 0
    return sum(liste) / len(liste)


if __name__ == "__main__":
    print(calculer_moyenne([10, 20, 30]))