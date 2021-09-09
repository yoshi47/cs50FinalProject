from flask import Flask, render_template, request
import requests

from navitime import getPoint, route

app = Flask(__name__)

# 車以外の移動、検索結果の保存、ホテルの値段（最安値などの選択肢）、予算の詳細、FlaskFormを使う、csrfトークン、selectのリストを別ファイルに

@app.route('/', methods=["GET", "POST"])
def home():  # put application's code here
  if request.method == "POST":
    # 出発地
    start = request.form.get('start')
    # 到着地
    goal = request.form.get('goal')
    # 人数
    people = request.form.get('people')
    # 日数
    days = request.form.get('days')

    # 緯度・経度の取得
    startCoord = getPoint(start)
    goalCoord = getPoint(goal)

    # 移動にかかる料金
    fare = route(startCoord, goalCoord)

    info = {'start': start, 'goal': goal, 'people': people, 'days': days, 'result': fare}
    return render_template('result.html', info=info)

  return render_template('form.html')


if __name__ == '__main__':
  app.run()
