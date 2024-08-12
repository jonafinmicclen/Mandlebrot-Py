import numpy as np
from PIL import Image


def mandlebrot_function(z : complex, c : complex) -> complex:
    return z*z + c


SIZE = (1000,1000)
mandlebrot_image = np.empty(SIZE, dtype=np.uint8)


for (x, y), _ in np.ndenumerate(mandlebrot_image):

    # The following "magic" numbers determine resolution and which part of the set which will be shown
    c = complex((x - 500)/500 - 0.5, (y - 500)/500)

    # Initialise Zn = 0 for Zn+1 = Zn^2 + C
    n_iteration = 0

    iterations = 0
    while True:
        iterations+=1

        n_iteration = mandlebrot_function(n_iteration, c)

        if abs(n_iteration) >= 2:
            mandlebrot_image[x, y] = 0
            break

        if iterations > 50:
            mandlebrot_image[x, y] = 255
            break

# Save as image
Image.fromarray(mandlebrot_image).save('output.png')