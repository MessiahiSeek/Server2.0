
FILE=./weights/yolov3.weights
if [ -f "$FILE" ]; then
echo "$FILE exists- requirement met."
else
curl https://pjreddie.com/media/files/yolov3.weights -output ./ImageHandler/yolov3.weights
fi
