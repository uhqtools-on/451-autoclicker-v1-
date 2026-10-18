import tkinter as tk
import threading
import time
import pyautogui
import keyboard

# Désactive la sécurité de pyautogui pour aller plus vite
pyautogui.PAUSE = 0.001

class SuperAutoclicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Autoclicker")
        self.root.geometry("320x250")
        self.root.resizable(False, False)
        
        self.running = False

        # --- ÉLÉMENTS DE L'INTERFACE ---
        
        title_label = tk.Label(root, text="⚡ 451 TOOL AUTOCLICKER ⚡", font=("Arial", 12, "bold"))
        title_label.pack(pady=10)

        self.status_label = tk.Label(root, text="Statut : EN PAUSE", font=("Arial", 10), fg="red")
        self.status_label.pack(pady=5)

        # Vitesse (Délai en millisecondes)
        speed_frame = tk.Frame(root)
        speed_frame.pack(pady=10)
        
        tk.Label(speed_frame, text="Délai entre les clics (ms) :").pack(side=tk.LEFT, padx=5)
        self.delay_entry = tk.Entry(speed_frame, width=6)
        self.delay_entry.insert(0, "1")  # Très rapide par défaut
        self.delay_entry.pack(side=tk.LEFT)

        # Boutons Démarrer / Arrêter
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="Démarrer", bg="green", fg="white", font=("Arial", 10, "bold"), width=10, command=self.start_clicking)
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Arrêter", bg="red", fg="white", font=("Arial", 10, "bold"), width=10, command=self.stop_clicking)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        self.stop_btn.config(state=tk.DISABLED)

        # Instructions pour le raccourci
        info_label = tk.Label(root, text="Raccourci Global :\nTouche [F6] pour Activer / Couper", font=("Arial", 8, "bold"), fg="blue")
        info_label.pack(pady=5)

        # Enregistre le raccourci clavier global (fonctionne même en jeu)
        # Tu peux remplacer 'f6' par 'esc' ou n'importe quelle autre touche si tu préfères
        keyboard.add_hotkey('f6', self.toggle_click)

    def click_loop(self):
        while self.running:
            try:
                user_delay = float(self.delay_entry.get()) / 1000.0
            except ValueError:
                user_delay = 0.001

            pyautogui.click()
            if user_delay > 0:
                time.sleep(user_delay)

    def start_clicking(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Statut : EN COURS 🚀", fg="green")
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            
            self.thread = threading.Thread(target=self.click_loop, daemon=True)
            self.thread.start()

    def stop_clicking(self):
        if self.running:
            self.running = False
            self.status_label.config(text="Statut : EN PAUSE", fg="red")
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)

    def toggle_click(self):
        if self.running:
            self.stop_clicking()
        else:
            self.start_clicking()

if __name__ == "__main__":
    root = tk.Tk()
    app = SuperAutoclicker(root)
    root.mainloop()