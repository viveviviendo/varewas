import os
import json
import re

ROOT = "src"

def limpiar_archivo(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Si detecta estructura JSON...
    if '"files"' in content:
        try:
            # Extraer el JSON completo
            json_match = re.search(r'\{.*}', content, re.DOTALL)
            if json_match:
                data = json.loads(json_match.group(0))
                nuevo_contenido = data["files"][0]["content"]

                # Escribir el contenido real
                with open(path, "w", encoding="utf-8") as f:
                    f.write(nuevo_contenido)

                print(f"✔ Limpiado: {path}")
                return

        except Exception as e:
            print(f"❌ Error limpiando {path}: {e}")

    else:
        print(f"✔ OK (sin JSON): {path}")


# Recorrer el proyecto
for subdir, dirs, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".astro"):
            limpiar_archivo(os.path.join(subdir, file))

print("\n🎉 Limpieza completada.")