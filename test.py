from yolo_opencv import objectDetect

#Create instance of class containing object detection methods
image = objectDetect()


#Process image and return new picture with objects labeled
imagePath = "images/cat.jpg"
image.processImage(imagePath)


#Process and image and print out the text contained in that image
#imagePath = "breaking_news.png"
#image.readText(imagePath)
