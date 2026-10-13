# PDF Sorter by DyogoCodes

Automatically organize PDFs into folders using keywords in their filenames. Works on macOS, Windows and Linux with Python 3, with no extra packages.

## Run

1. Download this repository using **Code > Download ZIP**, then extract it.
2. Open a terminal in the extracted folder.
3. Run:

```bash
python3 pdf_sorter.py
```

On Windows, use `py pdf_sorter.py` if needed.

## What happens

The script **moves** PDFs directly inside your Downloads folder into `Downloads/Sorted_PDFs/`:

| Folder | Filename keywords |
| --- | --- |
| Invoices | invoice, rechnung |
| Contracts | contract, vertrag |
| Offers | offer, quote, angebot |
| CVs | cv, resume, lebenslauf |
| Reports | report, bericht |
| Other | No matching keyword |

Matching ignores case. The first matching category wins. PDFs in subfolders are not processed. Existing destination filenames receive a numeric suffix instead of being overwritten.

This script sorts by filename, not PDF contents. Test with sample files first. Files must not be changed by another program while sorting.

## Customize

Edit `SOURCE` to choose a different input folder. Edit `RULES` to change categories and keywords. `DESTINATION` controls the output folder.

## Help

Questions? Contact **dyogocodes@gmail.com**.

YouTube: https://www.youtube.com/@dyogocodes
