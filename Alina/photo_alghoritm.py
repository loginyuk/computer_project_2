from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class Photo:
    """Alghoritm, that copress images files."""
    def __init__(self):
        self.bit_matrix_int = None
        self.result_image = ''
    def convert(self, path):
        """_summary_
        """
        image = Image.open(path)
        image = image.convert('1')
        bit_matrix = np.array(image)
        self.bit_matrix_int = bit_matrix.astype(int)
        res = self.bit_matrix_int.tolist()
        for row in res:
            row_str = ''.join(str(row))
            result = ''.join(row_str)
            self.result_image += ''.join(str(result))
            assert isinstance(self.result_image, str)
        return self.result_image

    def show(self):
        plt.imshow(self.bit_matrix_int, cmap='gray')
        plt.axis('off')
        plt.show()

photo = Photo()
print(photo.convert('image2.png'))
photo.show()


