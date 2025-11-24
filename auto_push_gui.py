import os
import threading
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess

running = False  # Auto Push state

# ---------- Hidden Git Runner ----------
def run_git(cmd):
    try:
        subprocess.Popen(
            cmd,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
    except Exception as e:
        log(f"Git Error: {e}")

# ---------- GUI Helper Functions ----------
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        repo_path_entry.delete(0, tk.END)
        repo_path_entry.insert(0, folder)

def log(text):
    root.after(0, lambda: _log(text))

def _log(text):
    log_box.insert(tk.END, text + "\n")
    log_box.see(tk.END)

# ---------- Auto Push Thread ----------
def auto_push_thread(repo_path, delay_minutes):
    global running
    delay_seconds = delay_minutes * 60

    while running:
        try:
            os.chdir(repo_path)
            log("Checking for changes...")

            # Check for git changes
            changes = os.popen("git status -s").read().strip()

            if changes == "":
                log("No changes found. Skipping commit.")
            else:
                changed_files = [line.strip() for line in changes.splitlines()]
                files_summary = ", ".join([f.split()[-1] for f in changed_files])

                commit_msg = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - {files_summary}"
                log(f"Commit Message: {commit_msg}")

                # Run git silently
                run_git(["git", "add", "."])
                time.sleep(1)  # small delay  
                
                run_git(["git", "commit", "-m", commit_msg])
                time.sleep(1)

                run_git(["git", "push", "origin", "main"])

                log("Pushed to GitHub Successfully!")

        except Exception as e:
            log(f"Error: {e}")

        log(f"⏳ Waiting {delay_minutes} minutes...")
        time.sleep(delay_seconds)

    log("Auto Push Stopped.")

# ---------- Start / Stop ----------
def start_auto_push():
    global running

    repo_path = repo_path_entry.get().strip()
    delay = delay_entry.get().strip()

    if not repo_path or not delay.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "Enter a valid Repo path & Delay time in minutes!")
        return

    running = True
    start_btn.config(state=tk.DISABLED)
    stop_btn.config(state=tk.NORMAL)

    delay_minutes = float(delay)
    t = threading.Thread(target=auto_push_thread, args=(repo_path, delay_minutes))
    t.start()

    log("Auto Push Started.")

def stop_auto_push():
    global running
    running = False
    start_btn.config(state=tk.NORMAL)
    stop_btn.config(state=tk.DISABLED)

# -------------------- GUI --------------------
root = tk.Tk()
root.title("GitHub Auto Push Tool")
root.geometry("650x500")
root.resizable(False, False)

tk.Label(root, text="Git Repo Folder:", font=("Arial", 11)).pack(pady=5)
frame = tk.Frame(root)
frame.pack()

repo_path_entry = tk.Entry(frame, width=50, font=("Arial", 10))
repo_path_entry.pack(side=tk.LEFT, padx=5)

browse_btn = tk.Button(frame, text="Browse", command=browse_folder)
browse_btn.pack(side=tk.LEFT)

tk.Label(root, text="Delay (minutes):", font=("Arial", 11)).pack(pady=5)

delay_entry = tk.Entry(root, width=20, font=("Arial", 10))
delay_entry.insert(0, "3")  # Default 3 minutes
delay_entry.pack()

start_btn = tk.Button(root, text="Start Auto Push", bg="#4CAF50", fg="white",
                    font=("Arial", 11), width=20, command=start_auto_push)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop", bg="orange", fg="white",
                    font=("Arial", 11), width=20, command=stop_auto_push,
                    state=tk.DISABLED)
stop_btn.pack(pady=5)

log_box = scrolledtext.ScrolledText(root, width=70, height=15,
                                    font=("Consolas", 10))
log_box.pack(pady=10)

root.mainloop()
