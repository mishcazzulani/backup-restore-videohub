import socket
import tkinter as tk
from tkinter import filedialog, messagebox

def get_videohub_status(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9990))
    data = ""
    while True:
        chunk = s.recv(4096).decode("utf-8", errors="ignore")
        if not chunk:
            break
        data += chunk
        if "END PRELUDE:" in data:
            break
    s.close()
    return data

def send_to_videohub(ip, payload):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9990))
    s.sendall(payload.encode("utf-8"))
    s.close()

def parse_sections(raw):
    sections = {}
    current = None
    for line in raw.splitlines():
        if line.endswith(":"):
            current = line
            sections[current] = []
            continue
        if current and line.strip():
            sections[current].append(line)
    return sections

def save_config():
    ip = ip_entry.get().strip()
    if not ip:
        messagebox.showerror("Error", "Please insert a valid IP address")
        return
    try:
        raw = get_videohub_status(ip)
    except Exception as e:
        messagebox.showerror("Connection error", str(e))
        return
    filename = f"{ip.replace('.', '-')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(raw)
    messagebox.showinfo("OK", f"Configuration saved as {filename}")

def load_config():
    global loaded_config
    path = filedialog.askopenfilename(
        filetypes=[("Videohub backup", "*.txt")]
    )
    if not path:
        return
    with open(path, "r", encoding="utf-8") as f:
        loaded_config = f.read()
    messagebox.showinfo("OK", "Configuration loaded")

def send_config():
    ip = ip_entry.get().strip()
    if not ip:
        messagebox.showerror("Error", "Please insert a valid IP address")
        return
    if not loaded_config:
        messagebox.showerror("Error", "No configuration loaded")
        return
    sections = parse_sections(loaded_config)
    payload = ""
    for key in (
        "INPUT LABELS:",
        "OUTPUT LABELS:",
        "VIDEO OUTPUT ROUTING:",
    ):
        if key in sections:
            payload += key + "\n"
            for line in sections[key]:
                payload += line + "\n"
            payload += "\n"
    try:
        send_to_videohub(ip, payload)
        messagebox.showinfo("OK", "Configuration sent to VideoHub")
    except Exception as e:
        messagebox.showerror("Send error", str(e))

loaded_config = ""
root = tk.Tk()
root.title("Videohub")
tk.Label(root, text="VideoHub IP:").grid(row=0, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root, width=20)
ip_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Save configuration", width=20, command=save_config).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
tk.Button(root, text="Load a config file", width=20, command=load_config).grid(row=2, column=0, columnspan=2, padx=10, pady=0)
tk.Button(root, text="Send to Videohub", width=20, command=send_config).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()
