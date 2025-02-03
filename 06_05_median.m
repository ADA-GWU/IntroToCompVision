pkg load image

im = imread('images/inchi2.png');
im_crop = im(80:200,80:200);
imshow(im_crop);

h = 1/4 * ones(4,1);
H = h*h';

mean_filt = filter2(H,im_crop);       % mean filter   - 5x5 shows better result
medi_filt = medfilt2(im_crop,[2 2]);  % median filter - 2x2 is the best

subplot(1,3,1);
imshow(im_crop);
subplot(1,3,2);
imshow(mean_filt);
subplot(1,3,3);
imshow(medi_filt);

waitforbuttonpress();
