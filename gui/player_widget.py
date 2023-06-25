from tkinter import Tk, Canvas
from PIL import Image, ImageTk


class PlayerWidget(Canvas):
    def __init__(self, master, x, y, image_path, scale=1.0):
        self.image_path = image_path
        self.scale = scale

        # Charger l'image avec PIL en conservant la transparence
        image = Image.open(image_path)
        image = image.convert("RGBA")

        # Redimensionner l'image si nécessaire
        if scale != 1.0:
            width = int(image.width * scale)
            height = int(image.height * scale)
            image = image.resize((width, height), Image.ANTIALIAS)

        # Créer l'image Tkinter à partir de l'image PIL
        photo_image = ImageTk.PhotoImage(image=image)

        # Appeler le constructeur de la classe parente pour créer le canvas
        Canvas.__init__(self, master, width=photo_image.width(), height=photo_image.height(), highlightthickness=0)
        self.create_image(0, 0, image=photo_image, anchor="nw")

        # Placer le widget du joueur sur le canvas aux coordonnées spécifiées
        self.place(x=x, y=y)

        self.image = photo_image  # Sauvegarder une référence vers l'image



    def load_image(self):
        image = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED)
        width = int(image.shape[1] * self.scale)
        height = int(image.shape[0] * self.scale)
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

        image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
        self.image = ImageTk.PhotoImage(image=Image.fromarray(image_rgba))

    def on_player_drag(self, event):
        if self.selected_player:
            delta_x = event.x - self.last_mouse_x
            delta_y = event.y - self.last_mouse_y
            self.master.master.canvas.move(self.tag, delta_x, delta_y)
            self.last_mouse_x = event.x
            self.last_mouse_y = event.y
