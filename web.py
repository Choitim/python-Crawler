###flask 모듈의 Flask 웹 프레임워크와 클라이언트 요청에 대한 객체 request
###미리 임포트 함


from flask import Flask, request
app = Flask(__name__)

@app.route("/kisia", methods=["GET", "POST"])
# 실제 동작하는 함수
def kisia():

    # 클라이언트의 요청 객체
    # print(request.headers)
    # print(request.data)

    params = json.loads(request.get_data())
    print(params["1"])
    
    # 리턴값은 kisia 200 ok
    return "kisia", 200


if __name__ == "__main__":
    # app.run 통해 웹을 구동
    # debug 디버깅 메시지 출력
    # host = 192.168.0.0
    # port = 
    app.run(debug=True, host="0.0.0.0", port=8000)