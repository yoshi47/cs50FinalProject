from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():  # put application's code here
  if request.method == "POST":
    return redirect('/result')

  return render_template('form.html')


@app.route('/result', methods=["GET", "POST"])
def result():
  return render_template('result.html')


if __name__ == '__main__':
  app.run()
