from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/authorize', methods=['POST'])
def authorize():
    path = request.headers.get('x-envoy-original-path', '')
    user = request.headers.get('x-user', '')

    # Simple logic: allow if path != /forbidden and user != "baduser"
    if path == "/forbidden" or user == "baduser":
        return make_response("Forbidden", 403)

    return make_response("OK", 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
