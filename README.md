# Face Detection with OpenCV

This Python project detects faces using either your **webcam** or a **static image** and draws rectangles around them in real-time or in the image.

## Features

* Detect faces in real-time from your webcam.
* Detect faces in a static image.
* Draws colored rectangles around detected faces.
* Automatically scales large images so they fit your screen.
* Press **Q** to exit webcam mode or any key to close image mode.

## Requirements

* Python 3.x
* OpenCV (`cv2` module)

Install OpenCV using pip:

```bash
pip install opencv-python
```

## Usage

1. Save the script as `face_detection.py`.
2. Run the script in your terminal or VS Code:

```bash
python face_detection.py
```

3. Enter the mode when prompted:

```
Enter 'webcam' to use webcam or 'image' to detect in an image:
```

* Type `webcam` for real-time detection.
* Type `image` to detect faces in a static image.

4. If you choose **image mode**, enter the **full path** to the image (Windows paths are supported, both with `\` or `/`). You can include quotes or not—the script will handle it automatically:

```
C:\Users\anvit\OneDrive\Documents\Pictures\Camera Roll 1\myphoto.jpg
```

5. The program will display the image with rectangles around detected faces.

6. For webcam mode, press **Q** to exit.
   For image mode, press any key to close the window.

## Author

Anvita Manne

## License

This project is licensed under the MIT License.
