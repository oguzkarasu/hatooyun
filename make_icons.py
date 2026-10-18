import os, shutil
from PIL import Image

RES = "android/app/src/main/res"
art = Image.open("cover-art.png").convert("RGBA")
sizes = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}

# yeni Android'in "adaptive" ikon tanimini kaldir, duz ikonlari kullan
shutil.rmtree(os.path.join(RES, "mipmap-anydpi-v26"), ignore_errors=True)

for d, s in sizes.items():
    out = os.path.join(RES, "mipmap-" + d)
    os.makedirs(out, exist_ok=True)
    a = art.copy()
    a.thumbnail((s, s), Image.LANCZOS)
    c = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    c.alpha_composite(a, ((s - a.width) // 2, (s - a.height) // 2))
    for n in ("ic_launcher.png", "ic_launcher_round.png", "ic_launcher_foreground.png"):
        c.save(os.path.join(out, n))
print("ikonlar tamam")
