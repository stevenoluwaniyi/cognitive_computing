from flask import Flask,jsonify,request,render_template
import textgenrnn


application = Flask(__name__)

@application.route("/")
def index():
	return render_template("gen_text.html")

@application.route("/generate-news/",methods=['GET'])
def generate_news():
	headline = request.args.get("headline")

	# Implement function to take in headline text and out predicitive text
	return jsonify({"Success": "Outputed model goes here"})

if __name__ == "__main__":
	application.debug = True
	application.run()
