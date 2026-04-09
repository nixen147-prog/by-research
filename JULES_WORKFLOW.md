# 🤖 Jules' Auto-Research Workflow & Master Prompts

Dette dokument samler de specifikke, optimerede prompts og instruktioner for AI-agenten Jules (eller andre agenter) i projektet **Dansk By-Research**. Følg dette multistep-workflow for maksimal kvalitet i alle aspekter af projektet.

---

## 🚀 Multistep Auto Workflow: Fra Data til 3D

Når du beder Jules om at researche et nyt sted, skal processen forløbe i disse trin. Som bruger kan du enten køre `tools/auto_research.sh <URL>` (hvis scriptet er opsat), eller give Jules følgende master-prompt:

> *"Jules, udfør fuld research-workflow for [Stednavn / URL]. Gennemfør Trin 1 til 4 ifølge `JULES_WORKFLOW.md` og opdater mig løbende."*

---

### Trin 1: Data-Indsamling (Webscraping & API)
**Mål:** Skaffe præcise grunddata (areal, fundament, historie) uden brug af eksterne pakker (pga. netværksrestriktioner).

**Agent Instruks / Prompt:**
> "Brug `tools/webscraper.py` på den angivne URL for at udtrække metadata. Analyser teksten for at finde byggeår, arkitekt og primær anvendelse. Hvis URL ikke er angivet, eller data mangler, søg i åbne danske registre (BBR, OIS.dk) for at udfylde hullerne. Husk at Python-scripts **kun** må bruge standardbiblioteker (som `urllib`, `html.parser`, `json`). Generér et validt JSON-objekt med nøglerne: `city`, `year`, `architect`, `style`, `area`, `foundation_type`, `description`, `hidden_infra_type`, `status`."

---

### Trin 2: Obsidian Markdown Generering
**Mål:** Oprette standardiseret dokumentation i det korrekte bibliotek (`Arkitektur/` eller `Infrastruktur/`).

**Agent Instruks / Prompt:**
> "Brug det genererede JSON fra Trin 1 til at køre `python tools/jules_researcher.py "[Stednavn]" '[JSON_STRING]'`. Verificér med `cat` eller `read_file` at filen er oprettet korrekt. Tjek at filen anvender den opdaterede skabelon fra `Templates/Bygning.md`, at dato-tagget `Created: YYYY-MM-DD` er tilføjet korrekt, og at de danske overskrifter og Obsidian wiki-links (f.eks. `[[Byer/ByNavn]]`) er bevaret intakte uden formateringsfejl."

---

### Trin 3: 3D-Visualisering (HTML/Three.js)
**Mål:** Oversætte matrikel- og bygningsdata til et interaktivt, browserbaseret "X-Ray" dashboard i rodmappen.

**Agent Instruks / Prompt:**
> "Skriv en ny HTML-fil for stedet (f.eks. `[stednavn]_scan.html`). Følg STRICT 'Neon-Grid Noir' guidelines:
> 1.  **Farver**: `#050505` baggrund. Synlig arkitektur: Cyan (`#00ffcc`). Skjult/underjordisk infrastruktur: Transparent Pink (`#ff3366`). Hjælpelinjer: `#333333` & `#111111`.
> 2.  **Kode-optimering (KRITISK)**: Instantiér **ALTID** `THREE.BufferGeometry`, `THREE.EdgesGeometry`, og `THREE.Material` objekter **UDENFOR** for-loops. Genbrug dem ved at oprette `new THREE.LineSegments` eller `THREE.Mesh` inde i loopet for at undgå garbage collection lag.
> 3.  **Bibliotek**: Brug eksisterende unpkg CDN-links for Three.js og OrbitControls (v0.160.0), præcis som i `index.html`. Ingen npm-installationer er tilladt.
> 4.  **Stil**: Bygningen skal fremstå som en præcis wireframe model (`EdgesGeometry`). Føj en OrbitControls instans til for interaktion, og en `GridHelper` i bunden."

---

### Trin 4: QA & Pre-commit Verifikation
**Mål:** Sikre, at visualiseringen ikke fejler, og at al koden overholder projektets strenge.

**Agent Instruks / Prompt:**
> "Udfør følgende QA-tjek før submit:
> 1. Start den lokale python HTTP server (`python -m http.server 8000 &`).
> 2. Brug Playwright (via `frontend_verification_instructions`) til at indlæse den nye `[stednavn]_scan.html` fil.
> 3. Tag et screenshot. Analyser billedet med `read_media_file` for at sikre, at farveskemaet (Sort/Cyan/Pink) fremstår korrekt, og at der ikke er rendering-fejl.
> 4. Tjek terminalens output for eventuelle TypeError eller manglende JSON-keys fra Trin 1 og Trin 2.
> 5. Udfør `pre_commit_instructions` før du anvender `submit` tool."

---

## 🛠️ Opsummering for Agenter (Jules' "Gyldne Regler")
- **Standard Libs Only:** Byg scripts med `urllib` og indbyggede værktøjer.
- **Three.js Performance:** Flyt Materials/Geometries ud af loops.
- **Neon-Grid Noir:** Hold fast i projektets visuelle signatur (Cyan/Pink på Sort).
- **Dansk Sprog:** Kode-kommentarer kan være engelske, men indhold og markdown er på dansk.