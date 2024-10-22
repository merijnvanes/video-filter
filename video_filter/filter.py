import cv2
import numpy as np

from video_filter.stock_filters import color_filters


class VideoFilter:
    def __init__(
            self,
            filter_name: str = "none",
            custom_matrix: np.ndarray = None,
            filter_strength: float = 1.0,
            brightness: float = 0.0,
            saturation: float = 0.0,
        ):
        self.filter_name = filter_name
        self.custom_matrix = custom_matrix
        self.brightness = self.get_brightness(brightness)
        self.saturation = self.get_saturation(saturation)
        self.filter_strength = self.get_filter_strength(filter_strength)
        self.filter_matrix = self.get_filter_matrix()
    
    @staticmethod
    def get_brightness(brightness):
        if (brightness < -2.0) or (brightness > 2.0):
            raise ValueError(
                "Brightness must be between -2.0 and 2.0."
            )
        return brightness
    
    @staticmethod
    def get_saturation(saturation):
        if (saturation < -2.0) or (saturation > 2.0):
            raise ValueError(
                "Saturation must be between -2.0 and 2.0."
            )
        return saturation
    
    @staticmethod
    def get_filter_strength(filter_strength):
        if filter_strength < 0.0 or filter_strength > 1.0:
            raise ValueError(
                "Filter strength must be between 0.0 and 1.0."
            )
        return filter_strength
    
    def get_filter_matrix(self):
        if self.custom_matrix is not None:
            if self.custom_matrix.shape != (3, 3):
                raise ValueError(
                    "Custom filter matrix must have shape (3, 3), but got "
                    f"{self.custom_matrix.shape}."
                )
            return self.custom_matrix
        elif self.filter_name is not None:
            filter_matrix = color_filters.get(self.filter_name, None)
            if filter_matrix is None:
                raise ValueError(
                    f"Filter with name {self.filter_name} not found."
                )
            return filter_matrix
        else:
            raise ValueError(
                "Either filter_name or custom_matrix must be provided."
            )

    def apply_strength(self, matrix):
        return (
            self.filter_strength * matrix 
            + (1 - self.filter_strength) * np.identity(3)
        )

    def get_color_transform_matrix(self):
        return self.apply_strength(self.filter_matrix)
    
    def apply_color_transform(self, frame):
        return cv2.transform(frame, self.get_color_transform_matrix())
    
    def apply_brightness(self, frame):
        return 2**self.brightness * frame
    
    def apply_saturation(self, frame):
        return (
            self.saturation 
            * ((np.sin(frame / (255 / np.pi) - (np.pi / 2)) + 1) / 2) * 255
            + (1-self.saturation) * frame
        )
    
    def apply_filter(self, frame):
        frame = frame.astype(np.float32)
        filtered_frame = self.apply_color_transform(frame)
        filtered_frame = self.apply_saturation(filtered_frame)
        filtered_frame = self.apply_brightness(filtered_frame)
        filtered_frame = np.clip(filtered_frame, 0, 255).astype(np.uint8)
        return filtered_frame

    def process_video(
            self,
            input_video_path,
            output_video_path,
            show_frames=False,
        ):
        cap = cv2.VideoCapture(input_video_path)
        if not cap.isOpened():
            raise Exception("Error: Could not open video.")
        
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        out = cv2.VideoWriter(
            output_video_path,
            fourcc,
            fps,
            (frame_width, frame_height)
        )
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            filtered_frame = self.apply_filter(frame)
            out.write(filtered_frame)
            
            if show_frames:
                cv2.imshow("Filtered Video", filtered_frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        
        cap.release()
        out.release()
        cv2.destroyAllWindows()
