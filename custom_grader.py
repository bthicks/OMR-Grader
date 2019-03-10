class CustomGrader:

    def find_page(self, im):
        """
        Finds and returns the test box within a given image.

        Args:
            im (numpy.ndarray): An ndarray representing the entire test image.

        Returns:
            numpy.ndarray: An ndarray representing the test box in the image.

        """
        return

    def decode_qr(self, im): 
        """
        Finds and decodes the QR code inside of a test image.

        Args:
            im (numpy.ndarray): An ndarray representing the entire test image.

        Returns:
            pyzbar.Decoded: A decoded QR code object.

        """
        return

    def rotate_image(self, im, angle):
        """
        Rotates an image by a specified angle.

        Args:
            im (numpy.ndarray): An ndarray representing the entire test image.
            angle (int): The angle, in degrees, by which the image should be 
                rotated.

        Returns:
            numpy.ndarray: An ndarray representing the rotated test image.

        """
        return

    def image_is_upright(self, page):
        """
        Checks if an image is upright, based on the coordinates of the QR code
        in the image

        Args:
            page (numpy.ndarray): An ndarray representing the test image.

        Returns:
            bool: True if image is upright, False otherwise.

        """
        return

    def upright_image(self, page):
        """
        Rotates an image by 90 degree increments until it is upright.

        Args:
            page (numpy.ndarray): An ndarray representing the test image.

        Returns:
            page (numpy.ndarray): An ndarray representing the upright test 
                image.

        """
        return

    def scale_config(self, config, width, height):
        """
        Scales the values in the config dictionary based on the width and height
        of the image being graded.

        Args:
            config (dict): An unscaled coordinate mapping read from the 
                configuration file.
            width (int): Width of the actual test image.
            height (int): Height of the actual test image.

        Returns:
            config (dict): A scaled coordinate mapping read from the 
                configuration file. 

        """
        return

    def encode_image(self, image):
        """
        Encodes a .png image into a base64 string.

        Args:
            image (numpy.ndarray): An ndarray representing an image.

        Returns:
            str: A base64 string encoding of the image.

        """
        return

    def grade(self, image_name, verbose_mode, debug_mode):
        """
        Grades a test image and outputs the result to stdout as a JSON object.

        Args:
            image_name (str): Filepath to the test image to be graded.

        """
        return


def main():
    """
    Parses command line arguments and grades the specified test.

    """
    # Parse the arguments.
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required=True, help='path to the input image')
    ap.add_argument('-v', action='store_true', required=False, help='enable verbose mode')
    ap.add_argument('-d', action='store_true', required=False, help='enable debug mode')
    args = vars(ap.parse_args())

    # Grade test.
    grader = CustomGrader()
    return grader.grade(args['image'], args['v'], args['d'])

if (__name__ == '__main__'):
    main()
