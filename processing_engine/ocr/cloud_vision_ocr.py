from google.cloud import vision
import base64
import os
import re
import PIL.Image
from typing import List, Optional, Union, Tuple, Dict, Any, Callable


class CloudVisionOCR:
    def __init__(self, imgs_dir_path: str) -> None:
        self.client: vision.ImageAnnotatorClient = vision.ImageAnnotatorClient()
        self.images_dir_path: str = imgs_dir_path
        self.base64_images_dir_path: str = os.path.join(imgs_dir_path, "base64_images")
        self.file_formats: dict[str, str] = {"jpg": "jpeg", "JPG": "jpeg", "png": "png"}

        
    def make_base64_images_dir(self) -> None:
        try:
            os.mkdir(self.base64_images_dir_path)
        except FileExistsError:
            pass
    
    def encode_image(self, image_path: str) -> None:
        for img_path in os.listdir(self.images_dir_path):
            # Read the image file
            with open(img_path, 'rb') as image_file:
                encoded_string: str = base64.b64encode(image_file.read()).decode('utf-8')

            base64_img_str: str = os.path.join(self.base64_images_dir_path, img_path)
            # Write the encoded string to a new file
            with open(base64_img_str, 'w') as output_file:
                output_file.write(encoded_string)
            return encoded_string
    
    def convert_image_format(self, file: str) -> str:
        """Converts an image file to a format that is readable by Cloud Vision."""

        file_type: str = file.split(".")[-1]

        # Create a dictionary mapping of file formats that are not readable by Cloud Vision
        # to the format that they should be converted to.
        
        # If the file format is not readable by Cloud Vision, convert it to the
        # format specified in the dictionary.
        if file_type not in self.file_formats:
            return file

        new_file_name: str = file.replace(file_type, self.file_formats[file_type])

        # Check if the file already exists in the new format.
        if os.path.exists(new_file_name):
            return new_file_name

        # Convert the file to the new format.
        os.rename(file, new_file_name)

        return new_file_name


    def detect_document(self) -> None:
        """Detects document features in an image."""
        all_files: List[str] = []
        for file in os.listdir(self.image_dir):  # <-- Fix 'self.image_dir' typo
            all_files.append(self.convert_image_format(file))  # <-- Add self. prefix

        for file in all_files:

            
            base64_content: str = self.encode_image(file)
            
            image: vision.Image = vision.Image(content=base64_content)

            try:
                response: vision.AnnotateImageResponse = self.client.document_text_detection(image=image)
            except Exception as e:
                if "Unknown field for AnnotateImageResponse: error_message" in str(e):
                    raise Exception(
                        "The Cloud Vision API was unable to process the image file. "
                        "Please check the image file to make sure that it is not corrupted. "
                        "Verify that the image file is in a supported format. The Cloud Vision API "
                        "supports the following image formats: JPEG, PNG, GIF, BMP, TIFF, and WEBP. "
                        "Try running the OCR on a different image file to see if the issue is with "
                        "the specific image file or with the Cloud Vision API."
                    )
                else:
                    raise e

            output_dir: str = os.path.join(os.getcwd(), "OcrTextResults")
            try:
                os.mkdir(output_dir)
            except FileExistsError:
                pass

            with open(os.path.join(output_dir, f"ocrResult_{os.path.basename(file)}.txt"), "w") as txt_file:
                for page in response.full_text_annotation.pages:
                    for block in page.blocks:
                        for paragraph in block.paragraphs:
                            words: List[str] = []
                            for word in paragraph.words:
                                word_text: str = "".join([symbol.text for symbol in word.symbols])

                                # Remove extra spaces
                                word_text = word_text.strip()

                                # Add two spaces after periods
                                if word_text.endswith("."):
                                    word_text += "  "

                                words.append(word_text)

                            txt_file.write(" ".join(words))

            if response.error.message:
                raise Exception(
                    "{}\nFor more info on error messages, check: "
                    "https://cloud.google.com/apis/design/errors".format(response.error.message)
                )
