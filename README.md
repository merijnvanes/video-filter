# Video Filter

Enhance your video with color filters. This Python project helps
you to apply a color filter to your Instagram reel or any other social platforms
like TikTok, YouTube, Facebook, etc. All formats are supported (reels, shorts,
4k, etc.). The output video is in mp4 format.

## Filter gallery selection

original | grayscale | warm |
:---:|:---:|:---:
![](examples/video_2.gif) | ![](examples/video_2_grayscale.gif) | ![](examples/video_2_warm.gif)

cool | red_only | invert_red_green
:---:|:---:|:---:
![](examples/video_2_cool.gif) | ![](examples/video_2_red_only.gif) | ![](examples/video_2_invert_red_green.gif)

## Installation

Fork the repository.

## Usage examples

### Example 1: Brightness

Brightness -50% | Original | Brightness +50% | Brightness +100%
:---:|:---:|:---:|:---:
![](examples/video_1_brightness_50.gif) | ![](examples/video_1.gif) | ![](examples/video_1_brightness_150.gif) | ![](examples/video_1_brightness_200.gif)

```
from video_filter import VideoFilter

vf = VideoFilter(brightness=1.5)
vf.process_video("examples/video_1.mp4", "output.mp4")
```

### Example 2: Color filters

Original | Sepia filter at 50% strength | Sepia filter at 100% strength
:---:|:---:|:---:
![](examples/video_2.gif) |  ![](examples/video_2_sepia_50.gif) | ![](examples/video_2_sepia_100.gif)

```
from video_filter import VideoFilter

vf = VideoFilter(filter_name="sepia", filter_strength=0.5)
vf.process_video("examples/video_2.mp4", "output.mp4")
```

### Example 3: Custom filter

Original      |  Custom filter
:-------------------------:|:-------------------------:
![](examples/video_1.gif) |  ![](examples/video_1_custom.gif)

```
from video_filter import VideoFilter
import numpy as np

# Matrix (3x3) vector (3x1) [b, g, r]) multiplication
filter_matrix = np.array([
    [0.7, 0.0, 0.1],  # Blue
    [0.2, 1.0, 0.3],  # Green
    [0.4, 0.2, 1.2]   # Red
])

vf = VideoFilter(
    custom_matrix=filter_matrix,
    filter_strength=0.6,
    brightness=0.8
)
vf.process_video("examples/video_1.mp4", "output.mp4")
```
