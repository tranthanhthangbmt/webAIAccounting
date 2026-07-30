import os
import glob
import time
import tkinter as tk
from tkinter import ttk, messagebox
import fitz  # PyMuPDF
from PIL import Image, ImageTk

# Base directories
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "TaiLieu", "textbookForPractice")
FIGURES_DIR = os.path.join(BASE_DIR, "Figures")

class PDFCropperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Cropper - Extract Figures")
        self.root.geometry("1200x800")
        
        # State variables
        self.pdf_files = []
        self.current_pdf_path = None
        self.doc = None
        self.current_page = 0
        self.zoom_factor = 1.0
        self.fit_to_screen = True
        
        self.rect_id = None
        self.start_x = None
        self.start_y = None
        
        self.image_tk = None
        self.current_pix = None
        
        self.setup_ui()
        self.load_pdf_list()
        
    def setup_ui(self):
        # Left Panel
        left_panel = tk.Frame(self.root, width=250, bg="#f0f0f0")
        left_panel.pack(side=tk.LEFT, fill=tk.Y)
        
        tk.Label(left_panel, text="PDF Files (Ch_01 - Ch_10):", bg="#f0f0f0").pack(pady=5)
        
        self.listbox = tk.Listbox(left_panel, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.listbox.bind('<<ListboxSelect>>', self.on_pdf_select)
        
        controls = tk.Frame(left_panel, bg="#f0f0f0")
        controls.pack(fill=tk.X, padx=5, pady=10)
        
        self.lbl_page = tk.Label(controls, text="Page: 0 / 0", bg="#f0f0f0")
        self.lbl_page.pack(pady=5)
        
        nav_frame = tk.Frame(controls, bg="#f0f0f0")
        nav_frame.pack(fill=tk.X)
        tk.Button(nav_frame, text="< Prev", command=self.prev_page).pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Button(nav_frame, text="Next >", command=self.next_page).pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        zoom_frame = tk.Frame(controls, bg="#f0f0f0")
        zoom_frame.pack(fill=tk.X, pady=10)
        tk.Button(zoom_frame, text="Zoom In", command=self.zoom_in).pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Button(zoom_frame, text="Zoom Out", command=self.zoom_out).pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        tk.Button(controls, text="Fit Screen", command=self.fit_screen).pack(fill=tk.X, pady=5)
        
        tk.Label(controls, text="Drag on image to crop\nand save automatically.", bg="#f0f0f0", fg="blue").pack(pady=10)
        
        tk.Label(controls, text="Cấu hình Tên File Ảnh", bg="#f0f0f0", font=("Arial", 9, "bold")).pack(pady=(10, 2))
        
        row1 = tk.Frame(controls, bg="#f0f0f0")
        row1.pack(fill=tk.X, padx=5, pady=2)
        tk.Label(row1, text="Loại:", bg="#f0f0f0", width=6, anchor="w").pack(side=tk.LEFT)
        self.combo_type = ttk.Combobox(row1, values=["Figure", "ILLUSTRATION", "Table", "BÀI TẬP", "Exercise", "Problem", "Case"], width=15)
        self.combo_type.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        row2 = tk.Frame(controls, bg="#f0f0f0")
        row2.pack(fill=tk.X, padx=5, pady=2)
        tk.Label(row2, text="Chương:", bg="#f0f0f0", width=6, anchor="w").pack(side=tk.LEFT)
        self.entry_chapter = tk.Entry(row2, width=5)
        self.entry_chapter.pack(side=tk.LEFT)
        
        tk.Label(row2, text=" STT:", bg="#f0f0f0").pack(side=tk.LEFT)
        self.entry_seq = tk.Entry(row2, width=5)
        self.entry_seq.pack(side=tk.LEFT)
        self.entry_seq.insert(0, "1")
        
        # Right Panel (Canvas with Scrollbars)
        right_panel = tk.Frame(self.root)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.canvas_frame = tk.Frame(right_panel)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.vbar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.hbar = tk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL)
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.canvas = tk.Canvas(self.canvas_frame, bg="gray", xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.vbar.config(command=self.canvas.yview)
        self.hbar.config(command=self.canvas.xview)
        
        # Bind mouse events for cropping
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        
        # Bind mouse wheel for scrolling
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind_all("<Button-4>", self.on_mouse_wheel)
        self.canvas.bind_all("<Button-5>", self.on_mouse_wheel)
        
        # Bind resize event to auto-fit if needed
        self.canvas.bind("<Configure>", self.on_canvas_resize)

    def load_pdf_list(self):
        if not os.path.exists(BASE_DIR):
            messagebox.showerror("Error", f"Directory not found:\n{BASE_DIR}")
            return
            
        self.pdf_files = []
        for file in os.listdir(BASE_DIR):
            if file.startswith("Ch_") and file.endswith(".pdf"):
                self.pdf_files.append(file)
        
        self.pdf_files.sort()
        for f in self.pdf_files:
            self.listbox.insert(tk.END, f)
            
    def on_pdf_select(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        filename = self.pdf_files[idx]
        self.current_pdf_path = os.path.join(BASE_DIR, filename)
        
        # Auto-fill chapter number from filename (e.g. Ch_02 -> 02)
        try:
            chap_num = filename.split('_')[1].split('.')[0]
            self.entry_chapter.delete(0, tk.END)
            self.entry_chapter.insert(0, chap_num)
        except:
            pass
            
        if self.doc:
            self.doc.close()
        
        try:
            self.doc = fitz.open(self.current_pdf_path)
            self.current_page = 0
            self.fit_to_screen = True
            self.render_page()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open PDF:\n{e}")

    def render_page(self):
        if not self.doc:
            return
            
        page = self.doc.load_page(self.current_page)
        self.lbl_page.config(text=f"Page: {self.current_page + 1} / {len(self.doc)}")
        
        if self.fit_to_screen:
            # Calculate zoom to fit canvas width or height
            canvas_w = self.canvas.winfo_width()
            canvas_h = self.canvas.winfo_height()
            
            if canvas_w > 1 and canvas_h > 1: # ensure canvas is rendered
                rect = page.rect
                zoom_w = canvas_w / rect.width
                zoom_h = canvas_h / rect.height
                self.zoom_factor = min(zoom_w, zoom_h) - 0.05 # 5% margin
            else:
                self.zoom_factor = 1.0
                
        matrix = fitz.Matrix(self.zoom_factor, self.zoom_factor)
        self.current_pix = page.get_pixmap(matrix=matrix)
        
        img = Image.frombytes("RGB", [self.current_pix.width, self.current_pix.height], self.current_pix.samples)
        self.image_tk = ImageTk.PhotoImage(img)
        
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        
    def prev_page(self):
        if self.doc and self.current_page > 0:
            self.current_page -= 1
            self.render_page()
            
    def next_page(self):
        if self.doc and self.current_page < len(self.doc) - 1:
            self.current_page += 1
            self.render_page()
            
    def zoom_in(self):
        self.fit_to_screen = False
        self.zoom_factor *= 1.2
        self.render_page()
        
    def zoom_out(self):
        self.fit_to_screen = False
        self.zoom_factor /= 1.2
        self.render_page()
        
    def fit_screen(self):
        self.fit_to_screen = True
        self.render_page()
        
    def on_canvas_resize(self, event):
        if self.fit_to_screen and self.doc:
            self.render_page()

    def on_mouse_wheel(self, event):
        # Handles Windows/Mac (<MouseWheel>) and Linux (<Button-4>/<Button-5>)
        if event.num == 4 or getattr(event, 'delta', 0) > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or getattr(event, 'delta', 0) < 0:
            self.canvas.yview_scroll(1, "units")

    def get_canvas_coords(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        return x, y

    def on_mouse_down(self, event):
        if not self.doc:
            return
        x, y = self.get_canvas_coords(event)
        self.start_x = x
        self.start_y = y
        if self.rect_id:
            self.canvas.delete(self.rect_id)
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red", width=2)
        
    def on_mouse_drag(self, event):
        if not self.rect_id:
            return
        x, y = self.get_canvas_coords(event)
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, x, y)
        
    def on_mouse_up(self, event):
        if not self.rect_id:
            return
        end_x, end_y = self.get_canvas_coords(event)
        
        # Calculate coordinates
        x0 = min(self.start_x, end_x)
        y0 = min(self.start_y, end_y)
        x1 = max(self.start_x, end_x)
        y1 = max(self.start_y, end_y)
        
        # If too small, ignore
        if (x1 - x0) < 10 or (y1 - y0) < 10:
            self.canvas.delete(self.rect_id)
            self.rect_id = None
            return
            
        self.crop_and_save(x0, y0, x1, y1)
        
    def crop_and_save(self, x0, y0, x1, y1):
        # Convert canvas coordinates to original PDF coordinates
        pdf_x0 = x0 / self.zoom_factor
        pdf_y0 = y0 / self.zoom_factor
        pdf_x1 = x1 / self.zoom_factor
        pdf_y1 = y1 / self.zoom_factor
        
        # Get target directory based on chapter
        filename = os.path.basename(self.current_pdf_path)
        chapter_prefix = filename.split('_')[0] + "_" + filename.split('_')[1] # e.g. Ch_01
        
        save_dir = os.path.join(FIGURES_DIR, chapter_prefix)
        os.makedirs(save_dir, exist_ok=True)
        
        # Extract at high resolution (300 DPI -> roughly scale 4.0)
        page = self.doc.load_page(self.current_page)
        clip_rect = fitz.Rect(pdf_x0, pdf_y0, pdf_x1, pdf_y1)
        matrix = fitz.Matrix(4.0, 4.0)
        
        try:
            pix = page.get_pixmap(matrix=matrix, clip=clip_rect)
            
            img_type = self.combo_type.get().strip()
            img_chap = self.entry_chapter.get().strip()
            img_seq = self.entry_seq.get().strip()
            
            custom_name = ""
            if img_type or img_chap or img_seq:
                if img_chap and img_seq:
                    custom_name = f"{img_type} {img_chap}.{img_seq}".strip()
                elif img_chap:
                    custom_name = f"{img_type} {img_chap}".strip()
                elif img_seq:
                    custom_name = f"{img_type} {img_seq}".strip()
                else:
                    custom_name = img_type

            if custom_name:
                import re
                safe_name = re.sub(r'[\\/*?:"<>|]', "", custom_name).strip()
                out_filename = os.path.join(save_dir, f"{safe_name}.png")
                counter = 1
                while os.path.exists(out_filename):
                    out_filename = os.path.join(save_dir, f"{safe_name}_{counter}.png")
                    counter += 1
                
                # Auto increment sequence if it's a number
                if img_seq.isdigit():
                    self.entry_seq.delete(0, tk.END)
                    self.entry_seq.insert(0, str(int(img_seq) + 1))
            else:
                timestamp = int(time.time() * 1000)
                out_filename = os.path.join(save_dir, f"page_{self.current_page + 1}_{timestamp}.png")
                
            pix.save(out_filename)
            
            # Flash the rectangle to indicate success
            self.canvas.itemconfig(self.rect_id, outline="green", width=3)
            self.root.after(500, lambda: self.canvas.delete(self.rect_id))
            
            print(f"Saved: {out_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to crop image:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFCropperApp(root)
    root.mainloop()
