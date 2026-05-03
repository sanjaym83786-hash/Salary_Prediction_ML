import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.helper import load_model, predict

model, edu_encoder, gender_encoder = load_model()

history = []

def predict_salary():
    try:
        exp = float(entry_exp.get())
        edu = combo_edu.get()
        gender = combo_gender.get()

        if edu == "" or gender == "":
            messagebox.showwarning("Input Error", "Select all fields")
            return

        salary = predict(model, edu_encoder, gender_encoder, exp, edu, gender)

        output_label.config(text=f"₹ {salary:,}")

        record = f"Exp:{exp} | Edu:{edu} | Gender:{gender} | ₹{salary}"
        history.append(record)
        update_history()

    except:
        messagebox.showerror("Error", "Invalid input")

def update_history():
    history_box.delete(0, tk.END)
    for item in history:
        history_box.insert(tk.END, item)

root = tk.Tk()
root.title("Salary Predictor (Kaggle)")
root.geometry("500x450")

tk.Label(root, text="Salary Prediction System",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Years of Experience").pack()
entry_exp = tk.Entry(root)
entry_exp.pack()

tk.Label(root, text="Education Level").pack()
combo_edu = ttk.Combobox(root, values=["Bachelor's", "Master's", "PhD"])
combo_edu.pack()

tk.Label(root, text="Gender").pack()
combo_gender = ttk.Combobox(root, values=["Male", "Female"])
combo_gender.pack()

tk.Button(root, text="Predict Salary", command=predict_salary).pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack()

tk.Label(root, text="Prediction History").pack()
history_box = tk.Listbox(root, width=60, height=10)
history_box.pack()

root.mainloop()