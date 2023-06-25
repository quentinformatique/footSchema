import tkinter as tk
from PIL import Image, ImageTk

# Créer une fenêtre Tkinter
window = tk.Tk()

# Charger l'image PNG avec transparence
image_path = "assets/maillot.png"
image = Image.open(image_path)

# Convertir l'image en mode RGBA pour conserver la transparence
image_rgba = image.convert("RGBA")

# Créer un fond avec une couleur solide
background_color = "blue"
background = Image.new("RGBA", image_rgba.size, background_color)

# Combiner l'image et le fond
composite_image = Image.alpha_composite(background, image_rgba)

# Créer une image Tkinter à partir de l'image composite
photo_image = ImageTk.PhotoImage(image=composite_image)

# Créer un widget Label pour afficher l'image
label = tk.Label(window, image=photo_image)
label.pack()

# Exécuter la boucle principale Tkinter
window.mainloop()
