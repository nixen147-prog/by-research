import sys
import json
import os
from datetime import datetime

class JulesResearcher:
    def __init__(self):
        self.output_dir = "Byer"
        self.arkitektur_dir = "Arkitektur"
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.arkitektur_dir, exist_ok=True)

    def generate_research_entry(self, location, data):
        """
        Generates a standardized Markdown entry for a location.
        'data' should be a dictionary with architectural measurements and history.
        """
        filename = f"{self.arkitektur_dir}/{location.replace(' ', '_')}.md"
        
        # Estimate measurements if missing
        area = data.get("area", 1000)
        piles = data.get("piles", int(area / 6.25)) # Estimate 1 pile per 6.25m2
        depth = data.get("depth", "-6.0m")
        
        content = f"""# Bygning: {location}

- **By:** [[Byer/{data.get("city", "Ukendt")}]]
- **Årstal:** {data.get("year", "Ukendt")}
- **Arkitekt:** {data.get("architect", "Ukendt")}
- **Stilart:** {data.get("style", "Ukendt")}

---

## Tekniske Data (Mål)
- **Areal:** {area} m²
- **Fundament:** {data.get("foundation_type", "Pælefundering")}
- **Antal pæle (Estimeret):** {piles}
- **Dybde:** {depth}

## Historie & Beskrivelse
{data.get("description", "Research i gang...")}

## Skjult Infrastruktur
- **Type:** {data.get("hidden_infra_type", "Ukendt")}
- **Status:** {data.get("status", "Identificeret")}

---
Tags: #arkitektur #bygning #jules-research #maalinger
Created: {datetime.now().strftime('%Y-%m-%d')}
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        
        return filename

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python jules_researcher.py 'Location Name' 'JSON_DATA'")
        sys.exit(1)
    
    location_name = sys.argv[1]
    raw_data = sys.argv[2]
    
    try:
        data_dict = json.loads(raw_data)
        researcher = JulesResearcher()
        path = researcher.generate_research_entry(location_name, data_dict)
        print(f"Research entry created: {path}")
    except Exception as e:
        print(f"Error: {e}")
