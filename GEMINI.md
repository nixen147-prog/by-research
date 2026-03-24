# GEMINI.md - Dansk By-Research (Danish City Research)

This project is an Obsidian-based research vault dedicated to Danish city history, architecture, and hidden infrastructure. It integrates automated research generation (Python) and interactive 3D visualizations (Three.js/HTML).

## Project Overview
- **Purpose**: Researching and documenting Danish cities, their architecture, and hidden/underground infrastructure.
- **Technologies**: 
  - **Markdown**: Obsidian-compatible documentation with wiki-links.
  - **Python**: `tools/jules_researcher.py` for automated Markdown generation.
  - **HTML/Three.js**: Interactive 3D visualizations with an "X-Ray" aesthetic.
  - **Automation**: GitHub Actions (`.github/workflows/jules-research.yml`).
- **Visual Style**: "Digital Architect / Neon-Grid Noir" (Cyan #00ffcc for visible, Pink #ff3366 for hidden, on a Black #050505 background).

## Directory Structure
- `Byer/`: Detailed notes on Danish cities (e.g., `Helsingør.md`).
- `Arkitektur/`: Individual building notes and architectural research.
- `Infrastruktur/`: Notes on bunkers, tunnels, and hidden systems.
- `Templates/`: Standardized Markdown templates for research entries.
- `tools/`: Python scripts for automation and data generation.
- `Kort_og_Billeder/`: Assets and visual documentation.
- `3d_visualizer.html`, `index.html`, etc.: 3D visualization dashboards.

## Key Files
- `Start_Her.md`: The entry point for researchers.
- `AGENTS.md`: Detailed guidelines for AI agents working in this project.
- `Templates/Design_Guidelines.md`: Visual and stylistic standards for 3D/documentation.
- `tools/jules_researcher.py`: Main script for generating architectural research files.

## Building and Running

### Python Research Generator
Generate a new building/architecture file:
```bash
python tools/jules_researcher.py "Location Name" '{"city": "CityName", "year": "1900", "architect": "Name"}'
```

### 3D Visualizer Dashboard
Run a local server to view the Three.js visualizations:
```bash
python -m http.server 8000
# Open http://localhost:8000/index.html
```

### GitHub Actions
Manual trigger for research workflows:
```bash
gh workflow run jules-research.yml -f location="Aarhus Hovedbanegård" -f data='{"city": "Aarhus"}'
```

## Development Conventions

### Documentation (Markdown)
- Use **Danish** for content, but keep system-level keys in English where appropriate.
- Use **Obsidian Wiki-links**: `[[Byer/Helsingør]]`.
- Tags are mandatory: `#arkitektur`, `#bygning`, `#infrastruktur`, `#research`.
- Date format: `YYYY-MM-DD`.

### Python Coding Style
- Follow PEP 8 (4-space indentation).
- Use **f-strings** for string formatting.
- **Type hints** are preferred for functions/methods.
- Standard library imports first.

### HTML/Three.js Visuals
- Use **Cyan (#00ffcc)** for visible structures.
- Use **Pink (#ff3366)** for hidden/underground elements.
- Use **LineSegments** and **EdgesGeometry** for a wireframe/x-ray look.
- Background should always be **#050505**.

### Git Commit Style
- Automated research: `Jules: Automatiseret research af [Location]`
- Manual changes: `Add:`, `Fix:`, `Update:` followed by a brief description.

## Usage for AI Agents
When creating new research entries, prioritize using `tools/jules_researcher.py` to ensure consistency. Always adhere to the "Digital Architect" visual style when generating HTML or Three.js code.
