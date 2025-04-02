import matplotlib.pyplot as plt
import numpy as np
import argparse


def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def draw(max_iter):
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    width, height = 1000, 1000
    r1, r2, n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    plt.show()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Draw a fractal')
    parser.add_argument('--max_iter', type=int, required=True, help='Number of iteration')
    args = parser.parse_args()

    draw(args.max_iter)




