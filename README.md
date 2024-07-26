# Video Filter

Enhance your video (output: mp4) with color filters. This Python project helps
you to apply a color filter to your Instagram reel or any other social platforms
like TikTok, YouTube, Facebook, etc. All formats are supported (reels, shorts,
4k, etc.).

## Installation

Fork the repository.

## Usage examples

### Example 1: Brightness

Original      |  Filtered (brightness increase)      |  Filtered (brightness increase)
:-------------------------:|:-------------------------:|:-------------------------:
![](examples/video_1.gif) |  ![](examples/video_1_brightness_increase.gif) |  ![](examples/video_1_brightness_increase.gif)

```
from video_filter import VideoFilter

input_video_path = "examples/video_1.mp4"
output_video_path = "examples/video_1_brightness_increase.mp4"

video_filter = VideoFilter(filter_name="brightness_increase")
video_filter.process_video(input_video_path, output_video_path)
```

### Example 2: Sepia

Original      |  Filtered (sepia at 50%)
:-------------------------:|:-------------------------:
![](examples/video_2.gif) |  ![](examples/video_2_sepia.gif)

```
from video_filter import VideoFilter

input_video_path = "examples/video_2.mp4"
output_video_path = "examples/video_2_sepia.mp4"

video_filter = VideoFilter(filter_name="sepia", filter_strength=0.5)
video_filter.process_video(input_video_path, output_video_path)
```

### Example 3: Custom filter

Original      |  Filtered (custom filter)
:-------------------------:|:-------------------------:
![](examples/video_2.gif) |  ![](examples/video_2_custom.gif)

```
from video_filter import VideoFilter
import numpy as np

input_video_path = "examples/video_2.mp4"
output_video_path = "examples/video_2_custom2.mp4"

# Matrix (3x3) vector (3x1) [b, g, r]) multiplication
filter_matrix = np.array([
    [0.8, 0.0, 0.0],  # Blue
    [0.0, 1.0, 0.1],  # Green
    [0.0, 0.2, 1.2]   # Red
])

video_filter = VideoFilter(custom_matrix=filter_matrix, filter_strength=0.5)
video_filter.process_video(input_video_path, output_video_path)
```
