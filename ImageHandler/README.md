# [How to Perform YOLO Object Detection using OpenCV and PyTorch in Python](https://www.thepythoncode.com/article/yolo-object-detection-with-opencv-and-pytorch-in-python)

This code relies heavily on the article supplied in the link above. The object detection libraries are a product of [thepythoncode.com](https://www.thepythoncode.com/)

To run this:
-  `git lfs clone https://github.com/MessiahiSeek/ImageHandler.git`
- `pip3 install -r requirements.txt`
- Download the model weights and put them in `weights` folder.
- To generate a object detection image on `images/dog.jpg` and read the text on the image `breaking_news.png` 
    ```
    python test.py
    ```
    A new image `dog_yolo3.jpg` will appear which has the bounding boxes of different objects in the image.
    This will start detecting objects in that video, in the end, it'll save the resulting video to `output.avi`

- If you wish to use PyTorch for GPU acceleration, please install PyTorch CUDA [here](https://pytorch.org/get-started) and use `yolo.py` file.
- Feel free to edit the codes for your needs!
