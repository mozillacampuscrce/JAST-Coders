
import base64
import numpy as np
import io
import keras
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from flask import request
from flask import jsonify
from flask import Flask
import pickle
from PIL import Image
#from flask_cors import CORS





app=Flask(__name__)
#CORS(app)
def get_model():
	global model
	model= load_model('model.h5')
	print("Model Loaded")
print("Loading Model")
get_model()

def preprocess_image(image , target_size):
	if image.mode != "RGB":
		image = image.convert("RGB")
	image = image.resize(target_size)
	image = img_to_array(image)
	image = np.expand_dims(image,axis = 0)

	return image

@app.route("/predict",methods=['POST'])
def predict():
	print("In pytthonnn")
	message = request.get_json(force = True)
	encoded = message['image']
	decoded = base64.b64decode(encoded)
	image = Image.open(io.BytesIO(decoded))
	processed_img = preprocess_image(image , target_size = (224 , 224))

	prediction = model.predict(processed_img).tolist()
	prediction = prediction*100

	response = {

		'prediction' : {
				'akiec' : prediction[0][0],
				'bcc': prediction[0][1] ,
				'bkl': prediction[0][2] ,
				'df': prediction[0][3] ,
				'mel': prediction[0][4] ,
				'nv': prediction[0][5] ,
				'vasc': prediction[0][6] 
		}
	}


	print(jsonify(response))	
	return jsonify(response)

		

print("Loading Keras Model...")



