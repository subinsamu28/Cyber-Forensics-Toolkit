# 🛡️ Cyber Forensics Toolkit

A desktop-grade forensic analysis application built for offline use. Powered by Python and PyQt5, this toolkit helps digital investigators, cybersecurity analysts, and forensic students perform file and disk image analysis — all from a clean, modern GUI.

---

## 🚀 Why This Toolkit?

Forget CLI tools and raw hex dumps. The Cyber Forensics Toolkit gives you an intuitive, pro-level interface for core forensic tasks:

- Extract metadata from files (PDF, DOCX, images, ZIPs)
- Carve hidden files from raw binary dumps
- Recover deleted files from disk images (FAT/NTFS)
- Verify file integrity using modern hashing algorithms
- Generate timeline reports from file timestamps

Everything works **offline**. No data ever leaves your machine.

---

## 🧰 Features at a Glance

| Module | Description |
|--------|-------------|
| 🔍 **Metadata Extractor** | Pulls metadata from documents, images, and archives |
| 🪓 **File Carver** | Recovers embedded JPEG, ZIP, or PDF files from raw binary |
| ♻️ **Deleted File Recovery** | Scans FAT/NTFS disk images and restores unallocated files |
| 🔐 **Hash Checker** | Calculates MD5, SHA1, and SHA256 for integrity checks |
| 📊 **Timeline Generator** | Builds forensic timelines from file system metadata |

---

## 🖼️ Interface Preview

> _Screenshots coming soon..._  
> Show off the beautiful dark-themed GUI, powered by custom QSS styling.

---

## 📦 Installation

### ✅ Requirements

- Python 3.11+
- Windows, macOS, or Linux
- Recommended: Virtual environment

### 🔧 Setup

```bash
git clone https://github.com/YOUR_USERNAME/cyber-forensics-toolkit.git
cd cyber-forensics-toolkit
pip install -r requirements.txt
python main.py
```

---

## 🧪 Tested With

- `.pdf`, `.docx`, `.jpg`, `.png`, `.zip` (for metadata)
- `.bin`, `.dd`, `.raw` dumps (for carving/recovery)
- FAT32 and NTFS disk images
- Directory structures with 1000+ files for timeline/hash analysis

---

## 💻 Build Standalone Executable

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py
```

Output will be inside `dist/`.

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

## 🧠 Tech Stack

- Python 3.11
- PyQt5
- PyPDF2, python-docx, PIL, pytsk3
- Custom QSS Styling for Premium GUI

---

## 📂 Sample Use Cases

- 🔬 Academic digital forensics labs
- 🕵️‍♂️ Law enforcement file inspections
- 🛡️ Cybersecurity incident analysis
- 🧰 Integrity verification in secure environments
- 📁 Local file system audits

---

## ⚠️ Disclaimer

This tool is intended for **legal and educational** use only. You are responsible for any misuse or violation of privacy laws.

---

## 🧑‍💻 Author

**Subin Samu**  
M.Sc. Applied Computer Science  
Cyber Forensics & Automation Enthusiast  
[LinkedIn →](https://www.linkedin.com/in/subinsamu)

---

© Subin Samu. All rights reserved.
