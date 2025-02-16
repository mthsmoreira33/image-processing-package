import matplotlib.pyplot as plt

def plot_images(images):
    plt.figure(figsize=(20, 10))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    number_images = len(args)
    fig, axes = plt.subplots(nrows = 1, ncols = number_images, figsize = (20, 10))
    names_lst = [f"Image {i}"for i in range(1, number_images)]
    for ax, name, image in zip(axes, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plot_histogram(image):
    fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (12, 4), sharex = True, sharey = True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axes.ravel(), color_lst)):
        ax.set_title(f'{color.title()} Histogram')
        ax.hist(image[:, :, index].ravel(), bins = 256, color = color, alpha = 0.8)
    fig.tight_layout()
    plt.show()
