# Video Filter

Applies a color filter to a video.

## Installation

Fork the repository.

## Usage examples

### Example 1: Brightness

Original      |  Filtered (brightness increase)
:-------------------------:|:-------------------------:
![](examples/video_1.gif) |  ![](examples/video_1_brightness_increase.gif)

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
