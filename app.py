from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():  # put application's code here
  if request.method == "POST":
    # 出発地
    origin = request.form.get('from')
    # 到着地
    destination = request.form.get('to')
    # 人数
    people = request.form.get('people')
    # 日数
    days = request.form.get('days')

    info = {'origin': origin, 'destination': destination, 'people': people, 'days': days}
    return render_template('result.html', info=info)

  return render_template('form.html')


if __name__ == '__main__':
  app.run()
