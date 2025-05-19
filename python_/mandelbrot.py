

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from numba import cuda

# Bildeparametere
width, height = 600, 600
max_iter = 256
xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0

# CUDA-kjerne for Mandelbrot
@cuda.jit
def mandelbrot_kernel(img, xmin, xmax, ymin, ymax, width, height, max_iter):
    x, y = cuda.grid(2)
    if x >= width or y >= height:
        return
    real = xmin + x * (xmax - xmin) / width
    imag = ymin + y * (ymax - ymin) / height
    c = complex(real, imag)
    z = 0.0j
    count = 0
    while abs(z) <= 2 and count < max_iter:
        z = z*z + c
        count += 1
    img[y, x] = count

# CUDA-kjerne for Julia
@cuda.jit
def julia_kernel(img, xmin, xmax, ymin, ymax, width, height, max_iter, creal, cimag):
    x, y = cuda.grid(2)
    if x >= width or y >= height:
        return
    real = xmin + x * (xmax - xmin) / width
    imag = ymin + y * (ymax - ymin) / height
    z = complex(real, imag)
    c = complex(creal, cimag)
    count = 0
    while abs(z) <= 2 and count < max_iter:
        z = z*z + c
        count += 1
    img[y, x] = count

def run_kernel(kernel_func, *args):
    img = np.zeros((height, width), dtype=np.uint16)
    d_img = cuda.to_device(img)
    threadsperblock = (16, 16)
    blockspergrid_x = (width + threadsperblock[0] - 1) // threadsperblock[0]
    blockspergrid_y = (height + threadsperblock[1] - 1) // threadsperblock[1]
    blockspergrid = (blockspergrid_x, blockspergrid_y)
    
    kernel_func[blockspergrid, threadsperblock](d_img, *args)
    return d_img.copy_to_host()

# Startvisning
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plt.subplots_adjust(bottom=0.25)

# Tegn Mandelbrot
mb_img = run_kernel(mandelbrot_kernel, xmin, xmax, ymin, ymax, width, height, max_iter)
mandelbrot_display = ax1.imshow(mb_img, extent=[xmin, xmax, ymin, ymax], cmap='inferno')
ax1.set_title("Mandelbrot Set")

# Startverdier for Julia
initial_c = complex(-0.8, 0.156)
jl_img = run_kernel(julia_kernel, xmin, xmax, ymin, ymax, width, height, max_iter, initial_c.real, initial_c.imag)
julia_display = ax2.imshow(jl_img, extent=[xmin, xmax, ymin, ymax], cmap='twilight_shifted')
ax2.set_title("Julia Set")

# Sliders
axcolor = 'lightgoldenrodyellow'
ax_real = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_imag = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor=axcolor)
s_real = Slider(ax_real, 'Re(c)', -1.5, 1.5, valinit=initial_c.real)
s_imag = Slider(ax_imag, 'Im(c)', -1.5, 1.5, valinit=initial_c.imag)

def update(val):
    c = complex(s_real.val, s_imag.val)
    new_julia = run_kernel(julia_kernel, xmin, xmax, ymin, ymax, width, height, max_iter, c.real, c.imag)
    julia_display.set_data(new_julia)
    fig.canvas.draw_idle()

s_real.on_changed(update)
s_imag.on_changed(update)

plt.show()