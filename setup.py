from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES_SETUP = [
    "setuptools",
    "wheel",
]

REQUIRED_PACKAGES = [
    "numpy",
    "opencv-python",
]

setup(
    name="video-filter",
    description="Enhance your video with filters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.4",
    url="https://github.com/merijnvanes/video-filter.git",
    author="Merijn van Es",
    author_email="merijnvanes@gmail.com",
    keywords=[
        "video", "filter", "color", "colour", "color filter", "colour filter",
        "video filter", "brightness", "brightness filter", "video brightness",
        "mp4", "video processing", "video editor tools", "short", "shorts",
        "reel", "reels", "social", "social post", "social posts",
        "social media", "social media post", "social media posts",
        "cool filter", "warm filter", "grayscale", "grayscale filter"
    ],
    packages=find_packages(exclude=["tests*"]),
    python_requires=">=3.7",
    install_requires=REQUIRED_PACKAGES,
    setup_requires=REQUIRED_PACKAGES_SETUP,
)