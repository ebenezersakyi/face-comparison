import base64
import requests
from flask import Flask, jsonify, request
from os.path import join, dirname
from deepface import DeepFace

# import request

app = Flask(__name__)

DeepFace.build_model('VGG-Face')

# Get the directory of the current script
current_dir = dirname(__file__)


@app.route('/verify/', methods=['POST'])
def verify_images():
    try:
        img1_file = request.files.get('img1')
        img2_link = request.form.get('img2')

        # Read the file content
        img1 = img1_file.read()

        # Check if img2 is a link and get its content
        if img2_link.startswith('http'):
            img2 = requests.get(img2_link).content
        else:
            return jsonify({'error': 'img2 is not a valid link', "success": False}), 400

        # Convert images to base64
        img1_base64 = r"data:image/jpeg;base64," + base64.b64encode(img1).decode('utf-8')
        img2_base64 = r"data:image/jpeg;base64,"+ base64.b64encode(img2).decode('utf-8')

        # Debugging statements
        # print("img1_base64:", img1_base64)
        # print("img2_base64:", img2_base64)

        # Verify images using DeepFace
        result = DeepFace.verify(img1_path=img1_base64, img2_path=img2_base64, model_name='VGG-Face')

        return jsonify({'data': result, "success": True}), 200
    except Exception as e:
        return jsonify({'error': str(e), "success": False}), 500


    
@app.route('/test', methods=['GET'])
def test():
    try:        
        return jsonify({'data': "Success", "success": True}), 200
    except Exception as e:
        return jsonify({'error': str(e), "success": False}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
