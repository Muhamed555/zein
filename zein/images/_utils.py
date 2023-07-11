# Import the required libraries
import tempfile
from PIL import Image
import os
import sys
import cv2
import requests
import tensorflow as tf
import pkg_resources



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# Define a helper function that converts an array to a temporary image file
def array_to_temp_file(array):
    # Create a temporary file with the .png extension
    temp_file = tempfile.NamedTemporaryFile(suffix=".png")
    # Convert the array to an image using PIL
    image = Image.fromarray(array)
    # Save the image to the temporary file
    image.save(temp_file.name)
    # Return the temporary file object
    return temp_file


def check_safety_helper(image_path):
    # Read in the image_data
    url = "https://github.com/minto5050/NSFW-detection/blob/master/retrained_graph.pb?raw=true"
    r = requests.get(url)
    
    temp_dir = tempfile.TemporaryDirectory()
    with open(f"{temp_dir.name}/retrained_graph.pb", "wb") as f:
        f.write(r.content)

    image_data = tf.io.gfile.GFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    graph_path = pkg_resources.resource_filename('zein', 'retrained_labels.txt')
    label_lines = [line.rstrip() for line in tf.io.gfile.GFile(graph_path)]

    # Unpersists graph from file
    with open(f"{temp_dir.name}/retrained_graph.pb", "wb") as f:      
        f.write(r.content)

    model_path = os.path.join(temp_dir.name, 'retrained_graph.pb')
    with tf.io.gfile.GFile(model_path, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    results = dict()
    with tf.compat.v1.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            results[human_string] = score

    return results
