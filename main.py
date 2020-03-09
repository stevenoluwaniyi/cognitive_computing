from flask import Flask,jsonify,request,render_template
from textgenrnn import textgenrnn
import os


application = Flask(__name__)

def load_model(prefix):
	value = textgenrnn(weights_path='output_weights.hdf5',
               vocab_path='output_vocab.json',
               config_path='output_config.json')

	gen_text = value.generate(n=1,prefix=prefix, temperature=1.5,return_as_list=True)
	return gen_text

@application.route("/")
def index():
	return render_template("gen_text.html")

@application.route("/generate-news/",methods=['GET'])
def generate_news():
	headline = request.args.get("headline")

	# Implement function to take in headline text and out predicitive text
	

	return render_template('display_text.html',data=str(load_model(headline)))

if __name__ == "__main__":
	application.debug = True
	application.run()
