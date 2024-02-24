from flask import Flask, request, jsonify, render_template
from algo import result_func

app = Flask(
    __name__,
    template_folder="template",
    static_url_path="/assets",
    static_folder="static",
)


@app.route("/", methods=["GET"])
def home():
    return render_template("Calculator.html")


@app.route("/result", methods=["POST"])
def Result():
    # Get the JavaScript string from the request
    js_string = request.json["js_string"]

    output = result_func(js_string)
    # Return the result as a JSON response
    return jsonify({"python_string": output})


if __name__ == "__main__":
    app.run(debug=True)
