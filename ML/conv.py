#%%
import numpy as np

#%%
def Custom_Convolve2D(image, kernel, padding=0, strides=1):
    # Cross Correlation
    # kernel = np.flipud(np.fliplr(kernel))
    ## Put your code here.
    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((xImgShape + padding * 2, yImgShape + padding * 2))
        imagePadded[
            int(padding) : int(-1 * padding), int(padding) : int(-1 * padding)
        ] = image
    else:
        imagePadded = image

    # Iterate through image
    for y in range(imagePadded.shape[1]):
        # Exit Convolution
        if y > imagePadded.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(imagePadded.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > imagePadded.shape[0] - xKernShape:
                    break
                # Only Convolve if x has gone down by the specified Strides
                if x % strides == 0:
                    output[x // strides, y // strides] = (
                        kernel * imagePadded[x : x + xKernShape, y : y + yKernShape]
                    ).sum()

    return output


def Custom_MaxPlooling(image, pool_size=(2, 2), padding=0, strides=None):
    ## Put your code here.
    # Gather Shapes of pool + Image + Padding
    xPoolShape = pool_size[0]
    yPoolShape = pool_size[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]
    # Stride
    if strides is None:
        strides = max(yPoolShape, xPoolShape)

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xPoolShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yPoolShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((xImgShape + padding * 2, yImgShape + padding * 2))
        imagePadded[
            int(padding) : int(-1 * padding), int(padding) : int(-1 * padding)
        ] = image
    else:
        imagePadded = image

    # Iterate through image
    for y in range(imagePadded.shape[1]):
        # Exit Convolution
        if y > imagePadded.shape[1] - yPoolShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(imagePadded.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > imagePadded.shape[0] - xPoolShape:
                    break
                # Only Convolve if x has gone down by the specified Strides
                if x % strides == 0:
                    output[x // strides, y // strides] = (
                        imagePadded[x : x + xPoolShape, y : y + yPoolShape]
                    ).max()

    return output


def Custom_Flatten(img):
    img = (img - img.min()) / (img.max() - img.min())
    return img.flatten()


def Custom_Dense(data, units=10):
    n = data.shape[0]
    data = np.reshape(data, (n, 1))

    # Setting the range from 0 to 0.04 to stop exponent explotion
    w = np.random.uniform(0, 0.04, [units, n])
    b = np.random.uniform(0, 0.04, [units, 1])

    return 1 / (1 + np.exp(-1 * (w @ data + b)))


def Custom_softmax(data):
    data = np.exp(data)
    data = data / data.sum()

    return data


#%%
im = np.array(
    [
        [4, 9, 2, 5, 8, 3],
        [5, 6, 2, 4, 0, 3],
        [2, 4, 5, 4, 5, 2],
        [5, 6, 5, 4, 7, 8],
        [5, 7, 7, 9, 2, 1],
        [5, 8, 5, 3, 8, 4],
    ]
)

kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
ss = np.array([[3.1, 0.3, 1.2]])
# %%
print(Custom_Convolve2D(im, kernel, 1, 1))
print(Custom_softmax(ss))
# %%
