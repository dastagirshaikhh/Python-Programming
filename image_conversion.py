import cv2
import numpy as np

def apply_hdr_effect(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error loading the image.")
        return

    # Convert the image to float32 format
    image_float = image.astype(np.float32) / 255.0

    # Apply tone mapping for HDR-like effect using TonemapReinhard
    tonemap = cv2.createTonemapReinhard()
    tone_mapped_image = tonemap.process(image_float)

    # Convert the tone-mapped image back to 8-bit format
    tone_mapped_image_8bit = (tone_mapped_image * 255).astype(np.uint8)

    # Display or save the HDR-like effect image
    cv2.imshow('HDR-like Effect', tone_mapped_image_8bit)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(output_path, tone_mapped_image_8bit)

if __name__ == "__main__":
    input_image_path = '1690868473201.jpg'
    output_image_path = 'output_image_hdr_effect.jpg'

    apply_hdr_effect(input_image_path, output_image_path)
