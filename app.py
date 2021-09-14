import locale

from flask import Flask, render_template, request

from api import carPrices, getPoint

app = Flask(__name__)

# 車以外の移動、検索結果の保存、ホテルの値段（最安値などの選択肢）、予算の詳細、FlaskFormを使う、csrfトークン、selectのリストを別ファイルに、ロード画面の変化

locale.setlocale(locale.LC_NUMERIC, 'ja_JP')
hotel = 8000


@app.context_processor
def utility_processor():
  def format_currency(amount):
    return locale.format('%d', amount, True)

  return dict(format_currency=format_currency)


@app.route('/', methods=["GET", "POST"])
def home():  # put application's code here
  global hotel

  if request.method == "POST":
    # 出発地
    start = request.form.get('start')
    # 到着地
    goal = request.form.get('goal')
    # 人数
    people = int(request.form.get('people'))
    # 日数
    days = int(request.form.get('days'))

    # 緯度・経度の取得
    startCoord = getPoint(start)
    goalCoord = getPoint(goal)

    # 移動にかかる料金
    fare = carPrices(startCoord, goalCoord)

    # 宿代を足す
    hotel *= days
    hotel *= people
    fare += hotel

    info = {'start': start, 'goal': goal, 'people': people, 'days': days, 'result': fare}
    return render_template('result.html', info=info)

  return render_template('form.html')


if __name__ == '__main__':
  app.run()
