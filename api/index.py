from flask import Flask, request, Response, send_from_directory
import os

app = Flask(__name__)

# Directory to save received images
UPLOAD_FOLDER = 'received_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create folder if it doesn't exist

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        # Receive the binary image data from the request
        image_data = request.data
        
        # Save the image to a file with a unique name
        image_path = os.path.join(UPLOAD_FOLDER, 'received_image.jpg')
        with open(image_path, 'wb') as f:
            f.write(image_data)
        
        print(f"Image saved as {image_path}")
        return Response("Image received successfully", status=200)
    except Exception as e:
        print(f"Error receiving image: {str(e)}")
        return Response("Error receiving image", status=500)

# Route to serve the saved image
@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='192.168.179.60', port=3000)
