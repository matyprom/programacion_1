from pathlib import Path

carpeta = Path.cwd()
print(carpeta)

for elemento in carpeta.iterdir():
    print(elemento.name)
    print("  Archivo:", elemento.is_file())
    print("  Directorio:", elemento.is_dir())