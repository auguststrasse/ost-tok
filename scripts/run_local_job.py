from app.services.script_generator import generate_tiktok_variants

title = "Neue Bahnverbindung zwischen Leipzig und Dresden geplant"
body = """
Das Land Sachsen plant nach Angaben des Verkehrsministeriums eine schnellere
Bahnverbindung zwischen Leipzig und Dresden. Ziel ist es, Pendelzeiten zu
verkürzen und die wirtschaftliche Anbindung zu verbessern. Kritiker verweisen
auf hohe Kosten und lange Bauzeiten.
"""

variants = generate_tiktok_variants(title=title, body=body, region="Sachsen")

for i, variant in enumerate(variants, start=1):
    print(f"\n--- Variante {i} ---")
    print("Angle:", variant["angle"])
    print("Hook:", variant["hook"])
    print("Script:", variant["script"])
    print("Caption:", variant["caption"])
    print("Hashtags:", ", ".join(variant["hashtags"]))