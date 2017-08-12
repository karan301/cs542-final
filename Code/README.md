# README

This is the folder that contains the code to run our CNN model.

To run the model, just run `python cnn.py`. It might take couple hours to run on a 
personal computer, but you can significantly reduce the time by running it on a server.

[`train_img_generator.py`](./train_img_generator.py) is used to create new partly-blurred images to the `tarpath` folder.
It returns a 3D list labels which indicates the blurred parts in each image.

Our training model is saved in [`motionblur.h5`](./motionblur.h5). 
