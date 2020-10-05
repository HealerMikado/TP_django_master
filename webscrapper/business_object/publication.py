from abc import ABC, abstractmethod


class Publication(ABC):
    def __init__(self, auteur="", lien="", contenu=""):
        self.lien = lien
        self.contenu = contenu
        self.auteur = auteur



if __name__ == '__main__':
    print("je suis passé par ici")
    pub = Publication("a", "b", "c")
    print(pub.get_auteur())


