import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Khởi tạo ứng dụng Tkinter
root = tk.Tk()
root.title("Ứng dụng dịch văn bản")
root.geometry("400x300")

# Khởi tạo Translator
translator = Translator()

# Hàm để thực hiện dịch
def translate_text():
    try:
        input_text = input_text_box.get("1.0", tk.END).strip()
        dest_lang = lang_combobox.get()
        
        if not input_text:
            messagebox.showerror("Lỗi", "Vui lòng nhập văn bản cần dịch.")
            return
        
        # Lấy mã ngôn ngữ đích từ giá trị chọn
        lang_code = lang_codes.get(dest_lang, "vi")
        
        # Dịch văn bản
        translated = translator.translate(input_text, dest=lang_code)
        
        # Hiển thị kết quả
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể dịch: {e}")

# Mã ngôn ngữ hỗ trợ
lang_codes = {
    "Tiếng Việt": "vi",
    "Tiếng Anh": "en",
    "Tiếng Pháp": "fr",
    "Tiếng Nhật": "ja",
    "Tiếng Trung": "zh-cn"
}

# UI: Nhập văn bản
tk.Label(root, text="Nhập văn bản:").pack(pady=5)
input_text_box = tk.Text(root, height=5, width=40)
input_text_box.pack(pady=5)

# UI: Chọn ngôn ngữ đích
tk.Label(root, text="Ngôn ngữ đích:").pack(pady=5)
lang_combobox = ttk.Combobox(root, values=list(lang_codes.keys()), state="readonly")
lang_combobox.set("Tiếng Việt")
lang_combobox.pack(pady=5)

# Nút dịch
translate_button = tk.Button(root, text="Dịch", command=translate_text)
translate_button.pack(pady=10)

# UI: Kết quả
tk.Label(root, text="Kết quả dịch:").pack(pady=5)
output_text_box = tk.Text(root, height=5, width=40, state="normal")
output_text_box.pack(pady=5)

# Chạy ứng dụng
root.mainloop()
