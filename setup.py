import sys
from cx_Freeze import setup, Executable

# Chemin de votre fichier principal Python (main.py)
main_script = 'main.py'

# Options de configuration pour l'exécutable
build_exe_options = {
    'packages': ['tkinter', 'gui', 'PIL', ],  # Liste des packages utilisés par votre application
    'excludes': [],  # Liste des modules à exclure
    'include_files': [('assets', 'assets')]  # Liste des fichiers supplémentaires requis (images, etc.)
}

# Création de l'exécutable
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'  # Si vous voulez une application sans console sur Windows

executable = Executable(script=main_script, base=base)

# Configuration de la construction
setup(
    name='projet_football',
    version='1.0',
    description='application permettant la création de schéma de comoosition de football',
    options={'build_exe': build_exe_options},
    executables=[executable]
)
