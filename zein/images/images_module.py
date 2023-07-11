# Import the required libraries
import numpy as np
from ._utils import check_safety_helper, array_to_temp_file, cv2

# Define your class
class ImageHandler:
    # Define the constructor method
    def __init__(self):
        # No parameters or attributes needed
        pass

    # Define a method to check the safety of an image
    def check_safety(self, path=None, array=None):
        # Check if the path or the array is given
        if path is not None:
            # Pass the path to your function
            return check_safety_helper(path)
        elif array is not None:
            # Convert the array to a temporary image file using the imported function
            temp_file = array_to_temp_file(array)
            # Pass the path of the temporary file to your function
            result = check_safety_helper(temp_file.name)
            # Close and delete the temporary file
            temp_file.close()
            # Return the result
            return result
        else:
            # Raise an exception if neither the path nor the array is given
            raise ValueError("You must provide either a path or an array")
    
    def filter_image(self, path = None, array = None, nsfw = None, size = None, blur = (51, 51)):
      if path is not None:
        results = check_safety_helper(path)
        if results['nsfw'] > nsfw:
          # Read the image from the path using cv2.imread
          image = cv2.imread(path)
          # Blur the image using cv2.GaussianBlur with a large kernel size and a small sigma value
          blurred_image = cv2.GaussianBlur(image, blur, 0)
          # Add some noise to the image using cv2.randn with a small standard deviation
          noise = np.zeros_like(blurred_image)
          cv2.randn(noise, 0, 10)
          blurred_image += noise
          # Check if the size parameter is given
          if size is not None:
              # Resize the image using cv2.resize with the given size
              resized_image = cv2.resize(blurred_image, size)
              # Return the resized image as an array
              return resized_image
          else:
              # Return the blurred image as an array without resizing
              return blurred_image
        else:
          image = cv2.imread(path)
          if size is not None:
              # Resize the image using cv2.resize with the given size
              resized_image = cv2.resize(image, size)
              # Return the resized image as an array
              return resized_image
          else:
              # Return the blurred image as an array without resizing
              return image
          # Return the original image as an array if it is not too nsfw

          return cv2.imread(path)
      elif array is not None:
        results = self.check_safety(array=array)
        if results['nsfw'] > nsfw:
          # Blur the array using cv2.GaussianBlur with a large kernel size and a small sigma value
          blurred_array = cv2.GaussianBlur(array, blur, 0)
          # Add some noise to the array using cv2.randn with a small standard deviation
          noise = np.zeros_like(blurred_array)
          cv2.randn(noise, 0, 10)
          blurred_array += noise
          # Check if the size parameter is given
          if size is not None:
              # Resize the array using cv2.resize with the given size
              resized_array = cv2.resize(blurred_array, size)
              # Return the resized array
              return resized_array
          else:
              # Return the blurred array without resizing
              return blurred_array
        else:
          if size is not None:
              # Resize the image using cv2.resize with the given size
              resized_image = cv2.resize(array, size)
              # Return the resized image as an array
              return resized_image
          else:
              # Return the blurred image as an array without resizing
              return array
      else:
        # Return None if no image is given
        return None