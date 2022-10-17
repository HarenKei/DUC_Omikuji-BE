from flask import Flask
import jsonReader

app = Flask(__name__)

@app.route('/')
def encodingToGB():
    targetText = jsonReader.leadingIndex(30)
    encoText =





if __name__ == '__main__':
    app.run()
