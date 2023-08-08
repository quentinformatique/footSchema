from tkinter import Menu, messagebox, filedialog
from PIL import ImageGrab
from tkinter.simpledialog import askstring


from gui import player_widget


class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent, tearoff=False, bg="#e0e0e0", fg="#000000", activebackground="#e0e0e0",)


        self.parent = parent
        self.canvas = parent.canvas

        self.oponent = 0
        self.x = 300

        # Créez les menus et les commandes ici
        self.file_menu = Menu(self, tearoff=False)
        self.app_menu = Menu(self, tearoff=False)
        self.affichage_menu = Menu(self, tearoff=False)

        self.file_menu.add_command(label="Enregistrer", command=self.save_file)

        self.app_menu.add_command(label="Aide", command=self.help)
        self.app_menu.add_command(label="A propos", command=self.about)

        self.affichage_menu.add_command(label="ajouter un adversaire", command=self.add_adversaire)
        self.affichage_menu.add_command(label="ajouter du texte", command=self.add_text)

        self.add_cascade(label="Fichier", menu=self.file_menu)
        self.add_cascade(label="Application", menu=self.app_menu)
        self.add_cascade(label="Affichage", menu=self.affichage_menu)


    def help(self):
        messagebox.showinfo("Aide", "Déplacez vos joueurs avec la souris en cliquant sur le joueur et en le déplaçant."
                                    "\nAppuyez Fichier puis Enregistrer afin de télécharger votre composition."
                                    "\n\nPour plus d'informations, veuillez contacter l'administrateur du système.")

    def about(self):
        messagebox.showinfo("A propos", "Application développée par : COSTES Quentin"
                                        "\nVersion 1.0"
                                        "\n2023"
                                        "\nTous droits réservés."
                                        "\n\nApplication développée avec Python 3.8.2 et Tkinter 8.6."
                                        "\n\nPour plus d'informations, veuillez contacter l'administrateur du système.")

    def save_file(self):
        # Ouvrir une boîte de dialogue pour sélectionner l'emplacement de sauvegarde
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
        if file_path:
            try:
                # Obtenir les coordonnées et la taille du canevas
                x = self.canvas.winfo_rootx()
                y = self.canvas.winfo_rooty()
                width = self.canvas.winfo_width()
                height = self.canvas.winfo_height()

                # Capturer l'image du terrain sans la barre de menu
                image = ImageGrab.grab(bbox=(x, y, x + width, y + height))

                # Enregistrer l'image au format PNG
                image.save(file_path)

                messagebox.showinfo("Sauvegarde réussie", "Fichier sauvegardé avec succès.")
            except Exception as e:
                messagebox.showerror("Erreur", "Erreur lors de la sauvegarde du fichier : {}".format(str(e)))

    def add_adversaire(self):

        if self.oponent > 11:
            messagebox.showerror("Erreur", "Vous ne pouvez pas ajouter plus de 11 adversaires.")
            return
        self.parent.add_player(self.x, 650, "assets/adversaire.png")
        self.oponent += 1
        self.x += 50

    def add_text(self):
        # Ouvre une fenêtre pour entrer du texte et le place sur le terrain
        text = askstring("Ajouter du texte", "Entrez le texte à placer sur le terrain:")
        if text:
            x, y = 500, 50
            self.parent.add_text(x, y, text)


