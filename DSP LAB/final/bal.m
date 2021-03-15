% Apply a Gaussian filter to remove noise
img = imread('saturn.png');
imshow(img);

% TODO: Add noise to the image
noise_sigma = 25;
noise = randn(size(img)).* noise_sigma;
noisy_img = img + noise;
imshow(noisy_img);
% TODO: Now apply a Gaussian filter to smooth out the noise
% Note: You may need to pkg load image;
filter_size = 11;
filter_sigma = 2;
pkg load image;
filter = fspecial('gaussian',filter_size,filter_sigma);

smoothed = imfilter(noisy_img,filter);
imshow(filter);