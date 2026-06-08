from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/track-results', methods=['GET'])
def authorize():
    token=request.cookies.get('token')
    if token == "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwidXNlcm5hbWUiOiIiLCJlbWFpbCI6ImFkbWluQGp1aWNlLXNoLm9wIiwicGFzc3dvcmQiOiIwMTkyMDIzYTdiYmQ3MzI1MDUxNmYwNjlkZjE4YjUwMCIsInJvbGUiOiJhZG1pbiIsImRlbHV4ZVRva2VuIjoiIiwibGFzdExvZ2luSXAiOiIiLCJwcm9maWxlSW1hZ2UiOiJhc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHRBZG1pbi5wbmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjUtMDUtMjIgMTY6Mjc6MjUuMDg3ICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjUtMDUtMjIgMTY6Mjc6MjUuMDg3ICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTc0ODg5MzQ1OX0.GEMtJLoQ3VMW5Tf17_PhYAzA-L-I46L8NGDGpChX7pMIqzMmZRaxqkQtgEXi_388wr13_0_t_62aDZDjl_oocHfZ7dlmDNOFWH5seNvLxahnEADuaGMKNuwUhxosvAkb2dwaXreIftx1fWlAHHACK1CmLJoVa82PnoTvjDTiCec":
      return make_response("{ 'SSN': '123-45-6789', 'Password': 'ABC123!' }", 200)
    else:
      return make_response("Unauthorized request", 401)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
