# video-reactive-lifx

<img src="https://img.shields.io/badge/python-3.7.3-3776AB?style=flat&logo=python" alt="python-3.7.3 logo">

Controlling LIFX light bulb based on average colour of each video frame.

## What does this do?

[Find demo video of the project here.](https://youtu.be/V_pxCcSp9Xs)

[![Demo Video Link](media/demo.gif)](https://youtu.be/V_pxCcSp9Xs "Video reactive LIFX light")

## Idea

Wanting to enhance the Video/TV Show/Movie viewing experience on a screen which is under a [LIFX](https://www.lifx.com/) Light Bulb.

## Methodology

### Step 1: Capturing video screen frame by frame

### Step 2: Processing image

- resize
- convert BGR to RGB colorspace
- applying Gaussian Blur

### Step 3: Calculating average colour of all pixels of the frame

### Step 4: Converting RGB to HSBK/HSVK colour space and setting bulb colour using LifxLAN

## Running script locally

```cmd
python3 main.py
```

## Credits

### Capturing and processing video screen

https://github.com/Sentdex/pygta5

### LifxLAN - High Level LIFX LAN Protocol Implementation

https://github.com/mclarkk/lifxlan

Other minor credits have been mentioned in the respective script files.
