from tkinter import Tk, PhotoImage
from gui.main_window import MainWindow
from gui.menu_bar import MenuBar

if __name__ == "__main__":
    root = Tk()
    root.title("foot schéma")  # Modifier le titre de la fenêtre principale

    root.wm_attributes("-transparentcolor", "gray")
    root.configure(bg="#303030")
    root.config(bg="gray")
    root.resizable(False, False)  # Empêcher le redimensionnement de la fenêtre principale

    # Charger le logo de l'application
    logo = PhotoImage(file="assets/maillot.png")
    root.iconphoto(True, logo)  # Définir le logo de l'application

    app = MainWindow(root)
    app.configure(bg="#333333")  # Définir la couleur de fond de la fenêtre principale

    menu_bar = MenuBar(app)  # Instancier la classe MenuBar et passer l'instance de MainWindow

    app.load_background_image("assets/terrain.png")

    # template de compo en 4-2-3-1

    app.add_player(95, 360, "assets/gardien.png")

    app.add_player(250, 270, "assets/maillot03.png")
    app.add_player(250, 470, "assets/maillot04.png")
    app.add_player(250, 90,  "assets/maillot02.png")
    app.add_player(250, 620, "assets/maillot05.png")

    app.add_player(400, 200, "assets/maillot06.png")
    app.add_player(400, 500, "assets/maillot07.png")

    app.add_player(563, 120, "assets/maillot08.png")
    app.add_player(563, 360, "assets/maillot09.png")
    app.add_player(563, 590, "assets/maillot10.png")

    app.add_player(750, 360, "assets/maillot11.png")

    root.config(menu=menu_bar)  # Définir la barre de menu dans la fenêtre principale

    root.mainloop()
