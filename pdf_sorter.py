from pathlib import Path
import shutil

SOURCE = Path.home() / "Downloads"
DESTINATION = SOURCE / "Sorted_PDFs"

RULES = {
    "Invoices": ["invoice", "rechnung"],
    "Contracts": ["contract", "vertrag"],
    "Offers": ["offer", "quote", "angebot"],
    "CVs": ["cv", "resume", "lebenslauf"],
    "Reports": ["report", "bericht"],
}


def unique_path(path):
    """Avoid overwriting existing files."""
    counter = 1
    candidate = path

    while candidate.exists():
        candidate = path.with_name(
            f"{path.stem}_{counter}{path.suffix}"
        )
        counter += 1

    return candidate


def main():
    if not SOURCE.is_dir():
        print(f"Folder not found: {SOURCE}")
        return

    count = 0

    for pdf in SOURCE.iterdir():
        if not pdf.is_file() or pdf.suffix.lower() != ".pdf":
            continue

        filename = pdf.name.lower()
        category = "Other"

        for folder, keywords in RULES.items():
            if any(keyword in filename for keyword in keywords):
                category = folder
                break

        target_folder = DESTINATION / category
        target_folder.mkdir(parents=True, exist_ok=True)

        target = unique_path(target_folder / pdf.name)
        shutil.move(str(pdf), str(target))

        print(f"{pdf.name} → {category}/{target.name}")
        count += 1

    print(f"\nDone! Sorted {count} PDFs.")


if __name__ == "__main__":
    main()
