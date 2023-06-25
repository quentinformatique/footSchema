from tkinter import Tk, PhotoImage
from gui.main_window import MainWindow
from gui.menu_bar import MenuBar

if __name__ == "__main__":
    root = Tk()
    root.title("foot schéma")  # Modifier le titre de la fenêtre principale

    root.wm_attributes("-transparentcolor", "gray")
    root.configure(bg="#303030")
    root.config(bg="gray")

    # Charger le logo de l'application
    logo = PhotoImage(file="assets/maillot.png")
    root.iconphoto(True, logo)  # Définir le logo de l'application

    app = MainWindow(root)
    app.configure(bg="#333333")  # Définir la couleur de fond de la fenêtre principale

    menu_bar = MenuBar(app)  # Instancier la classe MenuBar et passer l'instance de MainWindow

    app.load_background_image("assets/terrain.png")

    app.add_player(100, 100, "assets/maillot.png")
    app.add_player(200, 100, "assets/maillot.png")
    app.add_player(300, 100, "assets/maillot.png")
    app.add_player(400, 100, "assets/maillot.png")
    app.add_player(100, 200, "assets/maillot.png")
    app.add_player(200, 200, "assets/maillot.png")
    app.add_player(300, 200, "assets/maillot.png")
    app.add_player(400, 200, "assets/maillot.png")
    app.add_player(100, 300, "assets/maillot.png")
    app.add_player(200, 300, "assets/maillot.png")
    app.add_player(300, 300, "assets/maillot.png")

    root.config(menu=menu_bar)  # Définir la barre de menu dans la fenêtre principale

    root.mainloop()
