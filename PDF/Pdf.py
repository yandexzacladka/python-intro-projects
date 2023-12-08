import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from translate import Translator


class PDFViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Viewer")
        self.pdf_text = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Frame для размещения виджетов
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Кнопки для открытия PDF и листания страниц
        open_button = tk.Button(frame, text="Открыть PDF", command=self.open_pdf)
        open_button.grid(row=0, column=0, padx=5, pady=5)

        next_page_button = tk.Button(frame, text="Следующая страница", command=self.next_page)
        next_page_button.grid(row=0, column=1, padx=5, pady=5)

        pred_page_button = tk.Button(frame, text="Предыдущая страница", command=self.pred_page)
        pred_page_button.grid(row=0, column=2, padx=5, pady=5)

        # Текстовое поле для отображения всего текста на странице
        self.full_text_display = tk.Text(frame, wrap=tk.WORD, height=10, width=70)
        self.full_text_display.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        # Кнопка для выделения текста
        h_button = tk.Button(frame, text="Выделить текст", command=self.h_text)
        h_button.grid(row=2, column=0, padx=5, pady=5, columnspan=3)

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_reader = PdfReader(file_path)
            self.current_page = 0
            self.display_page()

    def next_page(self):
        if hasattr(self, 'pdf_reader') and self.current_page < len(self.pdf_reader.pages) - 1:
            self.current_page += 1
            self.display_page()

    def pred_page(self):
        if hasattr(self, 'pdf_reader') and self.current_page > 0:
            self.current_page -= 1
            self.display_page()

    def display_page(self):
        if hasattr(self, 'pdf_reader'):
            page = self.pdf_reader.pages[self.current_page]
            text = page.extract_text()
            self.pdf_text.set(text)

            # Очистить и вставить текст в текстовое поле для отображения всего текста на странице
            self.full_text_display.delete(1.0, tk.END)
            self.full_text_display.insert(tk.END, text)

    def h_text(self):
        selected_text = self.full_text_display.get(tk.SEL_FIRST, tk.SEL_LAST)

        # Перевод выделенного текста на русский
        translated_text = self.translate_text(selected_text)

        # Краткий пересказ переведенного текста
        summary = self.summarize_text(translated_text)

        # Новое окно для отображения выделенного, переведенного текста и краткого пересказа
        top_level = tk.Toplevel(self.root)
        top_level.title("Выделенный, переведенный текст и краткий пересказ")

        # Отображение выделенного текста
        selected_text_label = tk.Label(top_level, text=f"Выделенный текст: {selected_text}")
        selected_text_label.pack(padx=10, pady=5)

        # Отображение переведенного текста
        translated_text_label = tk.Label(top_level, text=f"Переведенный текст: {translated_text}")
        translated_text_label.pack(padx=10, pady=5)

        # Отображение краткого пересказа
        summary_label = tk.Label(top_level, text=f"Краткий пересказ: {summary}")
        summary_label.pack(padx=10, pady=5)

    def translate_text(self, text):
        translator = Translator(to_lang="ru")
        translation = translator.translate(text)
        return translation

    def summarize_text(self, text):
        # Просто возвращаю первые 50 символов текста в качестве краткого пересказа
        return text[:50]

# Главное окно
root = tk.Tk()
app = PDFViewer(root)
root.mainloop()
