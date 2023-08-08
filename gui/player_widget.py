from tkinter import Tk, Canvas
from PIL import Image, ImageTk


class PlayerWidget(Canvas):
    def __init__(self, master, x, y, image_path, scale=1.0):
        self.label = None
        self.image_path = image_path
        self.scale = scale

        # Charger l'image avec PIL en conservant la transparence
        image = Image.open(image_path).convert("RGBA")

        # Redimensionner l'image si nécessaire
        if scale != 1.0:
            width = int(image.width * scale)
            height = int(image.height * scale)
            image = image.resize((width, height), Image.ANTIALIAS)

        # Créer l'image Tkinter à partir de l'image PIL
        photo_image = ImageTk.PhotoImage(image=image)

        # Appeler le constructeur de la classe parente pour créer le canvas
        Canvas.__init__(self, master, width=photo_image.width(), height=photo_image.height(), highlightthickness=2, highlightbackground="#00a153")
        self.create_image(0, 0, image=photo_image, anchor="nw")
        self.config(bg="#00a153")


        # Placer le widget du joueur sur le canvas aux coordonnées spécifiées
        self.place(x=x, y=y)

        self.image = photo_image  # Sauvegarder une référence vers l'image




    def on_player_drag(self, event):
        if self.selected_player:
            delta_x = event.x - self.last_mouse_x
            delta_y = event.y - self.last_mouse_y
            self.master.master.canvas.move(self.tag, delta_x, delta_y)
            self.last_mouse_x = event.x
            self.last_mouse_y = event.y

    def get_position(self):
        """Récupère les coordonnées du joueur (coin supérieur gauche)"""
        x = self.winfo_x()
        y = self.winfo_y()
        return x, y

    def get_center(self):
        """Récupère les coordonnées du centre du joueur"""
        x, y = self.get_position()
        width = self.winfo_width()
        height = self.winfo_height()
        center_x = x + width / 2
        center_y = y + height / 2
        return center_x, center_y
