from tkinter import Frame, Canvas, PhotoImage

from gui import player_widget
from gui.player_widget import PlayerWidget
from tkinter import Label


class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.canvas_width = 1206
        self.canvas_height = 801
        self.canvas = None
        self.players = []  # Liste pour stocker les joueurs

        # Variables pour le déplacement des joueurs
        self.selected_player = None
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.drag_delay = 10  # Délai en millisecondes entre chaque déplacement
        self.drag_motion_id = None

        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self.master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

    def load_background_image(self, image_path):
        self.background_image = PhotoImage(file=image_path)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image, tags="terrain")

    def add_player(self, x, y, image_path):
        player = player_widget.PlayerWidget(self.canvas, x, y, image_path, scale=0.15)

        # Variables pour suivre les mouvements de la souris spécifiques à chaque joueur
        prev_x, prev_y = 0, 0

        # Fonctions de suivi des mouvements de la souris pour déplacer le joueur
        def on_press(event):
            nonlocal prev_x, prev_y
            prev_x, prev_y = event.x, event.y

        def on_drag(event):
            nonlocal prev_x, prev_y
            delta_x = event.x - prev_x
            delta_y = event.y - prev_y
            self.canvas.move(player.tag, delta_x, delta_y)

            # Access the label through the player object and move it along with the player
            self.canvas.move(player.label, delta_x, delta_y)

            prev_x, prev_y = event.x, event.y

        def on_release(event):
            pass

        # Lier les fonctions de suivi des mouvements de la souris aux événements de la souris
        player.bind("<ButtonPress-1>", on_press)
        player.bind("<B1-Motion>", on_drag)
        player.bind("<ButtonRelease-1>", on_release)

        # Créer une balise "player" pour le joueur, afin que l'on puisse les identifier ultérieurement
        player.tag = "player"

        # Ajouter le joueur à la liste et sur le canvas
        self.players.append(player)
        player.tag = self.canvas.create_window(x, y, anchor="nw", window=player)



    def add_opponent(self, x, y, image_path):
        player = PlayerWidget(self.canvas, x, y, image_path, scale=0.15)
        player.bind("<ButtonPress-1>", self.on_player_press)
        player.bind("<B1-Motion>", self.on_player_drag)
        player.bind("<ButtonRelease-1>", self.on_player_release)
        player.tag = self.canvas.create_window(x, y, anchor="nw", window=player)
        self.players.append(player)

    def delete_player(self, player):
        self.players.remove(player)
        self.canvas.delete(player.tag)


    def on_canvas_click(self, event):
        x = event.x
        y = event.y

        player_id = self.canvas.find_overlapping(x, y, x, y)
        if player_id:
            self.selected_player = player_id[0]
            self.last_mouse_x = x
            self.last_mouse_y = y
        else:
            self.selected_player = None

    def on_canvas_drag(self, event):
        if self.selected_player:
            x = event.x
            y = event.y

            current_player = self.canvas.find_withtag(self.selected_player)
            if current_player:
                player_tags = self.canvas.gettags(current_player[0])

                if "terrain" not in player_tags and "dragging" not in player_tags:
                    delta_x = x - self.last_mouse_x
                    delta_y = y - self.last_mouse_y

                    if not self.is_outside_terrain(self.selected_player, delta_x, delta_y):
                        self.canvas.addtag_withtag("dragging", self.selected_player)

                        self.canvas.move(current_player[0], delta_x, delta_y)
                        self.last_mouse_x = x
                        self.last_mouse_y = y

    def is_outside_terrain(self, player, delta_x, delta_y):
        if not player or not isinstance(player, int):
            return True

        player_coords = self.canvas.bbox(player)

        if not player_coords:
            return True

        new_coords = [
            player_coords[0] + delta_x,
            player_coords[1] + delta_y,
            player_coords[2] + delta_x,
            player_coords[3] + delta_y
        ]

        terrain_coords = self.canvas.bbox("terrain")
        if (new_coords[0] < terrain_coords[0] or new_coords[1] < terrain_coords[1] or
                new_coords[2] > terrain_coords[2] or new_coords[3] > terrain_coords[3]):
            return True

        return False

    def on_canvas_release(self, event):
        pass

    def on_player_press(self, event):
        self.canvas.itemconfig(self.selected_player, highlightthickness=0)
        self.selected_player = event.widget
        self.last_mouse_x = self.canvas.winfo_pointerx() - self.master.winfo_rootx()
        self.last_mouse_y = self.canvas.winfo_pointery() - self.master.winfo_rooty()

        self.start_drag_motion()

    def on_player_release(self, event):
        if self.drag_motion_id:
            self.after_cancel(self.drag_motion_id)
        self.selected_player = None
        # afficher les coordonnées du joueur

    def on_player_drag(self, event):
        if self.selected_player:
            delta_x = event.x - self.last_mouse_x
            delta_y = event.y - self.last_mouse_y

            self.canvas.move(self.selected_player.tag, delta_x, delta_y)

            self.last_mouse_x = event.x
            self.last_mouse_y = event.y


    def start_drag_motion(self):
        self.drag_motion()

    def drag_motion(self):
        if self.selected_player:
            x = self.canvas.winfo_pointerx() - self.master.winfo_rootx()
            y = self.canvas.winfo_pointery() - self.master.winfo_rooty()
            delta_x = x - self.last_mouse_x
            delta_y = y - self.last_mouse_y

            self.canvas.move(self.selected_player.tag, delta_x, delta_y)

            self.last_mouse_x = x
            self.last_mouse_y = y

        self.drag_motion_id = self.after(self.drag_delay, self.drag_motion)

    def add_text(self, x, y, text):
        text_object = self.canvas.create_text(x, y, text=text, anchor="nw", font=("Arial", 30), fill="black")

        # Variables pour suivre les mouvements de la souris
        prev_x, prev_y = 0, 0

        # Fonctions de suivi des mouvements de la souris pour déplacer le texte
        def on_press(event):
            nonlocal prev_x, prev_y
            prev_x, prev_y = event.x, event.y

        def on_drag(event):
            nonlocal prev_x, prev_y
            delta_x = event.x - prev_x
            delta_y = event.y - prev_y
            self.canvas.move(text_object, delta_x, delta_y)
            prev_x, prev_y = event.x, event.y

        def on_release(event):
            pass

        # Lier les fonctions de suivi des mouvements de la souris aux événements de la souris
        self.canvas.tag_bind(text_object, "<ButtonPress-1>", on_press)
        self.canvas.tag_bind(text_object, "<B1-Motion>", on_drag)
        self.canvas.tag_bind(text_object, "<ButtonRelease-1>", on_release)



