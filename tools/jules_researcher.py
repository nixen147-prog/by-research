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

        template_path = "Templates/Bygning.md"
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()

        replacements = {
            "{{name}}": location,
            "{{city}}": data.get("city", "Ukendt"),
            "{{year}}": str(data.get("year", "Ukendt")),
            "{{architect}}": data.get("architect", "Ukendt"),
            "{{style}}": data.get("style", "Ukendt"),
            "{{area}}": str(area),
            "{{foundation_type}}": data.get("foundation_type", "Pælefundering"),
            "{{piles}}": str(piles),
            "{{depth}}": str(depth),
            "{{description}}": data.get("description", "Research i gang..."),
            "{{hidden_infra_type}}": data.get("hidden_infra_type", "Ukendt"),
            "{{status}}": data.get("status", "Identificeret"),
            "{{photo_link}}": data.get("photo_link", "mangler.jpg"),
            "{{date}}": datetime.now().strftime('%Y-%m-%d')
        }

        for key, value in replacements.items():
            content = content.replace(key, value)

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
