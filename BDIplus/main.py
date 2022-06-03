from flask import Flask,render_template,request,jsonify
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8003, debug=True)
	#app.run()
