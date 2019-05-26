import os
import re
import argparse
import imageio

def imgs2gif(image_path, gif_path='', gif_name='gif_image', gif_duration=0.035):
    ''' Creats .gif images from bunch of images.

    Args:
        image_path (str): Directory that contains the images.
        gif_path (str): Directory that the output .gif will be saved.
        gif_name (str): Name of the output .gif.
        gif_duration (float): The duration (in sec) between images.

    Returns:
        An image type '.gif' of inputed images.
    '''
    # Get the image folder path
    image_folder = os.fsencode(image_path)

    # Read files
    filenames = []
    for file in os.listdir(image_folder):
        filename = os.fsdecode(file)
        if filename.endswith(('.jpeg', '.png', '.gif')):
            filenames.append(image_path+filename)

    # Sort the files
    # -- Because the names are str with char and numbers,
    #    we need to construct the sort function.
    def atoi(text):
        return int(text) if text.isdigit() else text
    def natural_keys(text):
        return [atoi(c) for c in re.split('(\d+)', text)]
    filenames.sort(key=natural_keys)

    # Get the images
    images = list(map(lambda filename: imageio.imread(filename), filenames))

    # Build the .gif image and save it
    imageio.mimsave(os.path.join(gif_path+gif_name+'.gif'), images, duration=gif_duration)

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument('--image_path', type=str, default="", required=True,
                        help='Path of images.')
    PARSER.add_argument('--gif_path', type=str, default="",
                        help='Output path for .gif image.')
    PARSER.add_argument('--gif_name', type=str, default="gif_image",
                        help='Name of the output .gif image.')
    PARSER.add_argument('--gif_duration', type=float, default=0.035,
                        help='Duration between images of .gif.')

    ARGS = PARSER.parse_args()

    imgs2gif(image_path=ARGS.image_path,
             gif_path=ARGS.gif_path,
             gif_name=ARGS.gif_name,
             gif_duration=ARGS.gif_duration)
