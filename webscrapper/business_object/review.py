from webscrapper.business_object.publication import Publication


class Review(Publication):
    def __init__(self
                 , auteur=""
                 , lien=""
                 , contenu=""
                 , titre=""
                 , note=0
                 , note_max=0):
        super().__init__(auteur, lien, contenu)
        self.note = note
        self.note_max = note_max
        self.titre = titre

    def __str__(self):
        return (" Auteur {}"
                "\n Titre {}"
                "\n Commentaire {}"
                "\n Note : {} / {}".format(self.auteur, self.titre,
                                           self.contenu, self.note,
                                           self.note_max))
