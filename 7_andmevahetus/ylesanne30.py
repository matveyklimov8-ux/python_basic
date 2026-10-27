from pathlib import Path
kaust = Path(__file__).resolve().parent
kirjed = []
with open(kaust / "opilased.txt", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        if len(osad) > 1:
            nimi = osad[0]
            hinded = [int(x) for x in osad[1:]]
            kirjed.append((nimi, sum(hinded) / len(hinded)))
ridade_keskmised = [keskmine for _, keskmine in kirjed]
klassikeskmine = sum(ridade_keskmised) / len(ridade_keskmised) if ridade_keskmised else 0
aruande_read = [f"{nimi}: keskmine hinne {keskmine:.2f}" for nimi, keskmine in kirjed]
aruande_read.append(f"Klassi keskmine õpilaste keskmiste põhjal: {klassikeskmine:.2f}")
aruanne = "\n".join(aruande_read) + "\n"
print(aruanne, end="")
(kaust / "opilaste_aruanne.txt").write_text(aruanne, encoding="utf-8")
