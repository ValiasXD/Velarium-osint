# 🔍 VELARIUM v1.1 — By ValiasXD

**VELARIUM** is a powerful, modular OSINT (Open Source Intelligence) tool designed to collect, analyze, and report on publicly available data related to usernames, domains, IPs, images, and more. It combines search automation, breach checking, metadata analysis, and reporting into one command-line toolkit.

---

## 🚀 Features

### 👤 Username Investigation
- `username <name>` — Search on 50+ popular platforms  
- `username -s <site> <name>` — Check a specific site  
- `username -k <name>` — Check major known platforms  
- `username -l <name>` — Deep scan (slower, more sources)  
- `username -a -f <name>` — Combine search options  

### 📧 Email Lookup
- Breach checks (HaveIBeenPwned support)  
- Leaked credentials scanning  

### 🌐 Domain & IP Intelligence
- `domain <domain>` — WHOIS info  
- `geoip <ip>` — Location, ISP, country  
- `ip -m <ip>` — Google Maps  
- `ip -w <ip>` — Find webcams near IP  
- `ip -s <ip>` — ASN, passive info  

### 📷 Image & Metadata Tools
- `exif <image>` — Extract camera + GPS metadata  
- `reverseimg <image>` — Google reverse image search  
- `imgmeta <image>` — Analyze image file internals  

### 🎥 Webcam Discovery
- `webcam <ip/country>` — Open live feeds (Insecam, public feeds only)

### 📦 Data Collection Toolkit
- `datacollect -F <name>` — Run full recon on a target  
- `datacollect -l <links>` — Accepts user-supplied data for analysis  
- `datacollect -p` — Export PDF/JSON report  
- `datacollect -a` — All-in-one (username, email, IP, image, breach)

### 🧠 AI-Powered OSINT (Optional)
- Summarizes findings  
- Tags potential risks  
- Extracts patterns or warnings  

### 🧾 Reporting
- Export to PDF / JSON / HTML  
- Rich output tables using `tabulate`, `rich`  

---

## 📦 Installation

```bash
git clone
https://github.com/ValiasXD/Velarium-osint.git 
cd velarium-osint
pip install -r requirements.txt
python Velarium.py 
