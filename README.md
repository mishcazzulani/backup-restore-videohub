<img width="301" height="239" alt="save-videohub" src="https://github.com/user-attachments/assets/ce1c6a6d-19e8-4c2f-895f-82dcf9aa470a" />

# 🎛️ Videohub Configuration Tool

A simple Python GUI tool to **backup, load, and send configurations** to a Blackmagic Videohub device over the network.

Built with `socket` and `tkinter`, this utility allows quick management of Videohub routing and labels without needing complex software.

---

## ✨ Features

- 📥 Save configuration from a Videohub device
- 📂 Load configuration from a backup file
- 📤 Send configuration back to a Videohub
- 🖥️ Simple and lightweight GUI (Tkinter-based)
- ⚡ Direct TCP communication (port `9990`)

---

## 📋 Requirements

- Python 3.x
- No external dependencies (standard library only)

---

## 🚀 Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/mishcazzulani/backup-restore-videohub.git
    cd backup-restore-videohub
    ```

2. Run the script:

    ```bash
    python save-videohub.py
    ```

3. Enter your Videohub IP address in the GUI.

---

## 🧭 How It Works

### Save Configuration
- Connects to the Videohub via TCP
- Downloads the current configuration
- Saves it as a `.txt` file (named after the IP address)

### Load Configuration
- Opens a previously saved `.txt` file
- Stores it in memory for later use

### Send Configuration
- Parses the loaded configuration
- Sends only relevant sections:
  - `INPUT LABELS`
  - `OUTPUT LABELS`
  - `VIDEO OUTPUT ROUTING`
- Applies changes to the Videohub

---

## 📁 File Format

Saved configuration files are plain text and contain sections like:

    INPUT LABELS:
    ...

    OUTPUT LABELS:
    ...

    VIDEO OUTPUT ROUTING:
    ...

---

## ⚠️ Notes

- Ensure the Videohub is reachable on the network
- Default port used: `9990`
- Only specific sections are sent back to avoid overwriting unnecessary data
- No authentication is implemented (assumes trusted network)

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

Developed by Michele Cazzulani

Feel free to contribute or open issues!
