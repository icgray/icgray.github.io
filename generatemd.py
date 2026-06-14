import csv
from pathlib import Path

TEMPLATE = """# {title}

**Years:** {years}  
**Role:** {role}  
**Tech:** {tech}

## Overview

_Describe what this project is about._

## Highlights

- Key result or impact
- Another highlight
- A third one

## Technical details

_Describe algorithms, models, hardware, etc._

## Links

- [Code repo](#)
- [Demo video](#)
"""

def main():
    docs_dir = Path("docs/projects")
    docs_dir.mkdir(parents=True, exist_ok=True)

    with open("projects.csv", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            slug = row["slug"]
            md_path = docs_dir / f"{slug}.md"
            if md_path.exists():
                print(f"Skipping existing {md_path}")
                continue
            content = TEMPLATE.format(
                title=row["title"],
                years=row["years"],
                role=row["role"],
                tech=row["tech"],
            )
            md_path.write_text(content, encoding="utf-8")
            print(f"Wrote {md_path}")

if __name__ == "__main__":
    main()
