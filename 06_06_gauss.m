pkg load image

im = imread('images/flower.png');

blur1 = imsmooth(im,"Gaussian",1);
blur2 = imsmooth(im,"Gaussian",3);
blur3 = imsmooth(im,"Gaussian",5);

subplot(1,4,1);
imshow(im);
subplot(1,4,2);
imshow(blur1);
subplot(1,4,3);
imshow(blur2);
subplot(1,4,4);
imshow(blur3);


waitforbuttonpress();
