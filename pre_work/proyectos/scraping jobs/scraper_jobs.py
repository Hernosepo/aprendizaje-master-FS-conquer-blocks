import requests
from bs4 import BeautifulSoup
import csv
import re

main_url = "https://www.hireinsouth.com/jobs"
response = requests.get(main_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

iframe = soup.find("iframe")
if not iframe:
    raise SystemExit("❌ No se encontró ningún iframe en la página principal.")

iframe_src = iframe.get("src", "")
print(f"🔎 Iframe encontrado, src completo:\n{iframe_src}")

# Detectar el slug (empresa) después de recruiterflow.com/
match = re.search(r"recruiterflow\.com/([^/]+)/", iframe_src)
if not match:
    raise SystemExit(f"❌ No se pudo extraer el identificador de empresa. iframe src: {iframe_src}")

company_slug = match.group(1)
print(f"🏢 Identificador de empresa encontrado: {company_slug}")

# Endpoint correcto (usa slug en lugar de subdominio)
api_url = f"https://recruiterflow.com/widget/api/openings?company_id={company_slug}"
print(f"🔗 Consultando API: {api_url}")

r = requests.get(api_url)
if r.status_code != 200:
    raise SystemExit(f"❌ Error {r.status_code} al acceder a la API: {api_url}")

data = r.json()

filename = "hireinsouth_jobs.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Título", "Ubicación", "Link"])

    openings = data.get("openings", [])
    for job in openings:
        title = job.get("title", "Sin título")
        location = job.get("location", "Sin ubicación")
        link = job.get("url", "Sin link")
        writer.writerow([title, location, link])

print(f"✅ Se guardaron {len(openings)} empleos en '{filename}'")