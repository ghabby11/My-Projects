import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def predict_tides():
    try:
        # Collect user inputs
        high1_time = high1_time_entry.get().strip()
        high1_height = float(high1_height_entry.get().strip())
        high2_time = high2_time_entry.get().strip()
        high2_height = float(high2_height_entry.get().strip())

        low1_time = low1_time_entry.get().strip()
        low1_height = float(low1_height_entry.get().strip())
        low2_time = low2_time_entry.get().strip()
        low2_height = float(low2_height_entry.get().strip())

        predict_times_raw = predict_times_entry.get("1.0", tk.END).strip()

        # Handle pasted Excel times (either column or comma separated)
        predict_times = [t.strip() for t in predict_times_raw.replace("\n", ",").split(",") if t.strip()]

        # Build tide data
        tide_data = [
            (datetime.strptime(high1_time, "%H:%M"), high1_height),
            (datetime.strptime(low1_time, "%H:%M"), low1_height),
            (datetime.strptime(high2_time, "%H:%M"), high2_height),
            (datetime.strptime(low2_time, "%H:%M"), low2_height)
        ]
        tide_data.sort(key=lambda x: x[0])

        # Interpolate for prediction
        predictions = []
        for pt in predict_times:
            pt_dt = datetime.strptime(pt, "%H:%M")
            for i in range(len(tide_data) - 1):
                t1, h1 = tide_data[i]
                t2, h2 = tide_data[i + 1]
                if t1 <= pt_dt <= t2:
                    ratio = (pt_dt - t1) / (t2 - t1)
                    height = h1 + ratio * (h2 - h1)
                    predictions.append(f"{height:.2f}")
                    break

        # Display output (one per line for Excel)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "\n".join(predictions))

    except ValueError:
        messagebox.showerror("Format Error", "Please use HH:MM format for times and numeric values for heights.")

# GUI Setup
root = tk.Tk()
root.title("Tide Predictor")
root.geometry("600x800")
root.configure(bg="#e8f0fe")

title_label = tk.Label(root, text="Tide Predictor", font=("Helvetica", 20, "bold"), bg="#e8f0fe", fg="#003366")
title_label.pack(pady=15)

# Date
tk.Label(root, text="Date (e.g. 2025-10-06):", font=("Helvetica", 12), bg="#e8f0fe").pack()
date_entry = tk.Entry(root, font=("Helvetica", 12), width=25)
date_entry.pack(pady=5)

# --- High Tides ---
tk.Label(root, text="High Tide 1", font=("Helvetica", 14, "bold"), bg="#e8f0fe").pack(pady=5)
frame_high1 = tk.Frame(root, bg="#e8f0fe")
frame_high1.pack()
tk.Label(frame_high1, text="Time (HH:MM):", font=("Helvetica", 12), bg="#e8f0fe").grid(row=0, column=0, padx=5)
high1_time_entry = tk.Entry(frame_high1, font=("Helvetica", 12), width=10)
high1_time_entry.grid(row=0, column=1)
tk.Label(frame_high1, text="Height (m):", font=("Helvetica", 12), bg="#e8f0fe").grid(row=0, column=2, padx=5)
high1_height_entry = tk.Entry(frame_high1, font=("Helvetica", 12), width=10)
high1_height_entry.grid(row=0, column=3)

tk.Label(root, text="High Tide 2", font=("Helvetica", 14, "bold"), bg="#e8f0fe").pack(pady=5)
frame_high2 = tk.Frame(root, bg="#e8f0fe")
frame_high2.pack()
tk.Label(frame_high2, text="Time (HH:MM):", font=("Helvetica", 12), bg="#e8f0fe").grid(row=0, column=0, padx=5)
high2_time_entry = tk.Entry(frame_high2, font=("Helvetica", 12), width=10)
high2_time_entry.grid(row=0, column=1)
tk.Label(frame_high2, text="Height (m):", font=("Helvetica", 12), bg="#e8f0fe").grid(row=0, column=2, padx=5)
high2_height_entry = tk.Entry(frame_high2, font=("Helvetica", 12), width=10)
high2_height_entry.grid(row=0, column=3)

# --- Low Tides ---
tk.Label(root, text="Low Tide 1", font=("Helvetica", 14, "bold"), bg="#e8f0fe").pack(pady=5)
frame_low1 = tk.Frame(root, bg="#e8f0fe")
frame_low1.pack()
tk.Label(frame_low1, text="Time (HH:MM):", font=("Helvetica", 12), bg="#e8f0fe").grid(row=0, column=0, padx=5)
low1_time_entry = tk.Entry(frame_low1, font=("Helvetica", 12), width=10)
low1_time_entry.grid(row=0, column=1)
tk.Label(frame_low1, text="Height (m):", font=("Helvetica", 12), bg="#e8f0fe").grid(row=0, column=2, padx=5)
low1_height_entry = tk.Entry(frame_low1, font=("Helvetica", 12), width=10)
low1_height_entry.grid(row=0, column=3)

tk.Label(root, text="Low Tide 2", font=("Helvetica", 14, "bold"), bg="#e8f0fe").pack(pady=5)
frame_low2 = tk.Frame(root, bg="#e8f0fe")
frame_low2.pack()
tk.Label(frame_low2, text="Time (HH:MM):", font=("Helvetica", 12), bg="#e8f0fe").grid(row=0, column=0, padx=5)
low2_time_entry = tk.Entry(frame_low2, font=("Helvetica", 12), width=10)
low2_time_entry.grid(row=0, column=1)
tk.Label(frame_low2, text="Height (m):", font=("Helvetica", 12), bg="#e8f0fe").grid(row=0, column=2, padx=5)
low2_height_entry = tk.Entry(frame_low2, font=("Helvetica", 12), width=10)
low2_height_entry.grid(row=0, column=3)

# --- Times to Predict ---
tk.Label(root, text="Input Required Times to Predict (HH:MM each on new line or comma separated):",
         font=("Helvetica", 12), bg="#e8f0fe", wraplength=550).pack(pady=8)
predict_times_entry = tk.Text(root, font=("Helvetica", 12), height=8, width=40)
predict_times_entry.pack(pady=5)

# --- Predict Button ---
predict_btn = tk.Button(root, text="Predict Tides", font=("Helvetica", 14, "bold"),
                        bg="#003366", fg="#00008B", command=predict_tides)
predict_btn.pack(pady=15)

# --- Output (for Excel) ---
tk.Label(root, text="Predicted Heights:",
         font=("Helvetica", 12), bg="#e8f0fe").pack()
output_text = tk.Text(root, height=10, width=25, font=("Helvetica", 12))
output_text.pack(pady=10)

root.mainloop()