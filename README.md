# 🛡️ Secure Keystroke Monitoring & Forensic Analysis System

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![License](https://img.shields.io/badge/License-Educational-green)
![Status](https://img.shields.io/badge/Status-Research-blueviolet)

---

## 🌟 Overview

The **Secure Keystroke Monitoring & Forensic Analysis System** is a **cybersecurity research project** designed to demonstrate how keyboard input events can be **captured, encrypted, stored, and analyzed** in a controlled and ethical environment. This project simulates keylogger behavior **safely** for **educational purposes**, helping cybersecurity learners understand **monitoring software, digital forensics, and data security**.

---

## 🖥️ What is a Keylogger?

A **keylogger** (or keystroke logger) is a software or hardware tool that records **every key pressed** on a keyboard.  
Keyloggers are widely studied in cybersecurity because attackers often use them to steal sensitive information like **passwords, banking credentials, and private communications**.  
Studying keyloggers helps security professionals **detect threats, analyze malware, and improve defense mechanisms**.

---

## 🔹 Types of Keyloggers

**1️⃣ Software Keyloggers** – Programs installed on the operating system that capture keyboard events via APIs.  
**2️⃣ Hardware Keyloggers** – Physical devices connected between the keyboard and computer to record keystrokes.  

*Software keyloggers are more common in modern attacks due to malware deployment or phishing techniques.*

---

## ⚡ How Keyloggers Work

- Monitor keyboard events whenever a key is pressed  
- Convert events into readable characters  
- Store data in **encrypted log files**  
- Decrypt, analyze, and generate reports for study  

**This project** uses **Python (`pynput`)** to capture input, **`cryptography`** to encrypt logs, and **`reportlab`** to generate PDF reports.

---

## 🎯 Why Study Keyloggers?

Keylogger research is important for:

- **Malware Analysis** – Understand how attackers capture data  
- **Digital Forensics** – Reconstruct user activity  
- **Insider Threat Monitoring** – Detect unusual behavior  
- **Defensive Security** – Build better detection tools  

*Ethical research ensures that skills are learned safely without harming anyone.*

---

## 🛠️ Project Features

- 🖱️ **Secure Keyboard Logging** – Capture typing events locally  
- 🔐 **Encrypted Log Storage** – Protect data with Fernet encryption  
- 📖 **Log Viewer** – Decrypt and inspect logs  
- 📊 **Analyzer Module** – Generate keystroke statistics  
- 📄 **PDF Report Generator** – Summarize project findings  
- 🧩 **Modular Architecture** – Easy to understand and extend  

---

## 💻 Technologies Used

- **Python 3.13**  
- **`pynput`** – Keyboard event monitoring  
- **`cryptography`** – Encryption / decryption  
- **`reportlab`** – PDF generation  

---

## 📂 Project Structure

keylogger_project/
│
├── src/
│ ├── logger.py # Captures keyboard events
│ ├── encryptor.py # Encryption & decryption
│ ├── viewer.py # Decrypt and view logs
│ ├── analyzer.py # Analyze keystroke statistics
│ └── report_generator.py # Generates PDF reports
│
├── logs/
│ └── keystrokes.log # Encrypted logs
│
├── reports/ # Generated PDF reports
├── requirements.txt # Project dependencies
└── README.md # Documentation

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/keylogger_project.git
cd keylogger_project
pip3 install -r requirements.txt
pip3 install pynput cryptography reportlab

▶️ How to Run

1. Navigate to the source folder:

cd src

2. Start the keylogger simulation:

python3 logger.py

3. Type normally in the terminal.

4. Press ESC to stop the logger.


📖 Viewing Logs
python3 viewer.py

Example output:

2026-03-05 21:20:10 : hello cybersecurity
2026-03-05 21:20:18 : testing my project

📊 Analyzing Logs
python3 analyzer.py

Example output:

Total Keystrokes: 120
Letters: 95
Special Keys: 25


| Pros                           | Cons                            |
| ------------------------------ | ------------------------------- |
| Detailed activity capture      | Can be abused by attackers      |
| Learn encryption & analysis    | Unauthorized use is illegal     |
| Forensic & behavioral research | Local only, no network features |
| PDF reporting & statistics     | Simplified simulation           |


Created by Gaurav Jain
