# Cyber-Forensics-Toolkit
📁 Cyber Forensics Toolkit A Python + PyQt5 desktop app for digital forensics. 🔍 Metadata Extractor 🧩 File Carver ♻️ Deleted File Recovery 🔐 Hash Checker 📅 Timeline Generator Modular backend, clean GUI, exportable reports built for investigators and forensic analysts.


# 🛡️ Cyber Forensics Toolkit

A high-utility, cross-platform forensic analysis suite built for **offline** use. Developed in **Python** with a modern **PyQt5** interface, this toolkit empowers digital investigators, cybersecurity professionals, and students to inspect files and disk images — efficiently and privately.

---

## 🚀 Why Use This Toolkit?

Ditch command-line guesswork and raw hex dumps.

This GUI-based solution provides a clean, productive experience for key forensic tasks:

✅ Extract metadata from PDFs, DOCX, images, and archives  
✅ Carve hidden files from raw binary memory/disk dumps  
✅ Recover deleted files from FAT/NTFS disk images  
✅ Verify file integrity with MD5, SHA1, SHA256  
✅ Generate forensic timelines from file system metadata  

🔒 100% offline — your data stays on your machine.

---

## 🧰 Feature Overview

| 🧩 **Module**             | 📝 **Description**                                                                 |
|--------------------------|------------------------------------------------------------------------------------|
| 🔍 Metadata Extractor     | Extracts metadata from images, documents, archives, and common file types         |
| 🪓 File Carver            | Recovers embedded ZIP, JPEG, PDF from raw `.bin`, `.dd`, `.raw` dumps             |
| ♻️ Deleted File Recovery  | Restores deleted files from FAT/NTFS images (unallocated space scanning)          |
| 🔐 Hash Checker           | Verifies file integrity using MD5, SHA-1, and SHA-256                             |
| 📊 Timeline Generator     | Builds forensic timeline reports from file timestamps and metadata                |

---

## 🖼️ Interface Preview

> _📸 GUI screenshots coming soon!_  
> Built with dark-themed **QSS styling**, polished layouts, and modular tab system.

---

## 📦 Installation Guide

### ✅ Requirements

- Python 3.11+
- OS: Windows, macOS, or Linux
- Optional: Virtual environment (recommended)

### 🔧 Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/cyber-forensics-toolkit.git
cd cyber-forensics-toolkit
pip install -r requirements.txt
python main.py
```

---

## 🧪 Tested File Types

- `.pdf`, `.docx`, `.jpg`, `.png`, `.zip` (metadata extraction)
- `.bin`, `.dd`, `.raw` (file carving & recovery)
- FAT32 and NTFS disk images
- Large directories (1000+ files) for hash & timeline analysis

---

## 🖥️ Build Standalone Executable

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py
```

Output will be inside the `dist/` directory.

---

## 📁 Project Structure

```
cyber-forensics-toolkit/
├── main.py
├── ui/                    # PyQt5 interface for each tool
├── core/                  # Backend logic for forensics modules
├── assets/                # Icons, dark theme
├── output/                # Carved/recovered/timeline exports
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

- **Python 3.11**
- **PyQt5** – UI framework
- **PyPDF2**, **python-docx**, **Pillow**, **pytsk3**
- **Custom QSS** for polished dark theme UI

---

## 📂 Ideal Use Cases

- 🎓 Academic digital forensics labs
- 🕵️‍♂️ Law enforcement file inspections
- 🛡️ Cybersecurity incident response
- 🧰 File integrity verification in secure setups
- 📁 Local system audit automation

---

## ⚠️ Legal Disclaimer

This tool is strictly intended for **educational and lawful forensic use** only. The author is not responsible for any misuse or violation of data privacy regulations.

---

## 👤 Author

**Subin Samu**  
M.Sc. Applied Computer Science  
Cyber Forensics & Automation Enthusiast  
[🔗 LinkedIn](https://www.linkedin.com/in/subinsamu)

---

© Subin Samu. All rights reserved.
