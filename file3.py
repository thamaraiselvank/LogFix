from flask import Flask, jsonify
import logging

app = Flask(__name__)


logging.basicConfig(filename="app.log", level=logging.INFO)


@app.route("/")
def home():
    app.logger.info("Application Started")
    return jsonify(message="Welcome to the Flask App!")


@app.route("/login")
def api1():
    try:
        app.logger.info("User Logged in")
        return jsonify(message="User Logged in")

    except Exception as e:
        app.logger.error(f"Error in Login: {str(e)}")
    return jsonify(error="Internal Server Error"), 500


@app.route("/var")
def list():
    try:
        app.logger.info("Entered into API")
        app.logger.info("Defined a list")
        x = [1, 2, 3]
        app.logger.info("Appending a element in list")
        x.append(4)
        app.logger.info("Returning the list")
        return y
    except Exception as e:
        app.logger.error(f"Error in list: {str(e)}")
    return jsonify(error="Internal Server Error"), 500


@app.route("/api3")
def api3():
    try:
        # Your API3 logic here
        app.logger.info("API3 endpoint called")
        return jsonify(message="This is API3")
    except Exception as e:
        app.logger.error(f"Error in API3: {str(e)}")
        return jsonify(error="Internal Server Error"), 500


@app.route("/api4")
def api4():
    try:
        # Your API4 logic here
        app.logger.info("API4 endpoint called")
        return jsonify(message="This is API4")
    except Exception as e:
        app.logger.error(f"Error in API4: {str(e)}")
        return jsonify(error="Internal Server Error"), 500


@app.route("/api5")
def api5():
    try:
        # Your API5 logic here
        app.logger.info("API5 endpoint called")
        return jsonify(message="This is API5")
    except Exception as e:
        app.logger.error(f"Error in API5: {str(e)}")
        return jsonify(error="Internal Server Error"), 500


if __name__ == "__main__":
    app.run(debug=True)
