# 🖼️ Image Processing Toolkit (Python + OpenCV + NumPy)

This project is a **comprehensive image processing toolkit** developed in **Python**, built to explore and compare the performance of various **image transformation, enhancement, and filtering algorithms**.  
Each task demonstrates both **manual (NumPy-based)** and **OpenCV-based** implementations to analyze differences in efficiency, image quality, and algorithmic behavior.

---

## 🧩 Implementations Explained

### **Task 1 – Image Interpolation**
- **Nearest Neighbor & Bilinear (manual):** Implemented pixel-by-pixel scaling using NumPy and nested loops.  
- **Bicubic (OpenCV):** Used `cv2.resize()` for comparison.  
- Evaluated quality and computation time between methods on grayscale test images.

### **Task 2 – Intensity Transformations**
- **Negative Image:** Inverts pixel intensities (`255 - pixel_value`).  
- **Power-Law / Gamma Correction:** Adjusts image brightness and contrast using \( s = c \times r^\gamma \).  
- **Bit-Plane Slicing:** Extracted all 8 bit-planes to visualize each significance level of pixel data.  

### **Task 3 – Histogram Processing**
- **Histogram Equalization (manual):** Computed image histogram, CDF, and intensity remapping with NumPy.  
- Improved contrast and brightness distribution without relying on OpenCV’s built-in equalizer.

### **Task 4 – Spatial Filtering**
- **Custom Convolution:** Implemented 2D convolution manually with zero padding and kernel flipping.  
- **Smoothing Filters:** Applied 11×11 average filter (manual) and compared with OpenCV’s `cv2.blur()` and `cv2.GaussianBlur()`.  
- **Edge Detection:** Used Sobel operator (OpenCV) to highlight intensity gradients and edges.  

---

## ⚙️ Technologies Used
- **Python 3.x**  
- **NumPy** – efficient numerical computation and array manipulation  
- **OpenCV** – image I/O and advanced image processing  
- **Matplotlib** *(optional)* – visualization of results  

---

📊 Results & Observations

NumPy-based implementations provide clear insight into algorithm logic but are slower than OpenCV equivalents.

OpenCV functions leverage C-based optimization, achieving up to 3× faster performance on large images.

Gamma correction and histogram equalization significantly improved image contrast.

The custom convolution filter successfully replicated smoothing and edge detection effects observed using OpenCV filters.

