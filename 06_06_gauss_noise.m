im = imread('images/parrot.jpeg');

sigma = 2;
noise = randn(size(im)).*sigma;

subplot(1,3,1);
imshow(im);

subplot(1,3,2);
imshow(noise);

subplot(1,3,3);
imshow(im+noise);

waitforbuttonpress();
