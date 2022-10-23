from flask import Flask
import jsonReader

app = Flask(__name__)

@app.route('/')
def encodingToGB():
    targetText = jsonReader.leadingIndex()[0]
    encoText = targetText.encode("gb18030").hex()
    encoTextLen = int(len(encoText))
    encoTextResult = ""

    i = 0
    for i in range(i, encoTextLen, 2):
        encoTextResult += encoText[i : i + 2 ] + " "

    return encoTextResult

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
