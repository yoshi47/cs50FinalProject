# Ikuyosan

#### Video Demo: https://youtu.be/TkhGPPXWBkg

You can try the app on [Heroku](https://ikuyosan.herokuapp.com/)

![img.png](https://user-images.githubusercontent.com/64204237/133374267-207abf51-f3e2-4d65-a49c-a0afdf0c3c3d.png)

## About

This app allows you to get a quick estimate of your trip. You can easily see how much you need for your trip.

Place names are complemented using autocomplete, but will not be available if the API limit is exceeded. If this
happens, please try to enter the name of the prefecture first. If this happens, please try to enter the name of the
prefecture first, or the name of a place with the same name in a different place than you expected will be used.

## Technologies used

- Flask
- jQuery
- NAVITIME API for Rakuten RapidAPI
- Bootstrap
- Heroku
- Gunicorn

## How to get an estimate

This app calculates your total spending every time!

1. user enters information
2. get the address of the starting point and destination
3. get travel route and highway fare
4. add the highway fee and gasoline fee
5. add the cost of accommodation
6. Estimate completed!

## Possible improvements

As all applications this one can also be improved. Possible improvements:

- Make it optional to add things to do on the trip. Theme parks, camping, hot springs, skiing/snowboarding, snorkeling,
  car rental, etc.
- Hotel prices are flat, so get the price for each search and calculate it.
- Traveling by public transportation
- Change the load screen.
- Support overseas travel
- Use FastAPI for the backend to speed up the process.
- Adding a Database

# いくよさん

#### Video Demo: https://youtu.be/TkhGPPXWBkg

Herokuを使ってこのアプリを公開しています。是非試してみてください。

**[Ikuyosan](https://ikuyosan.herokuapp.com/)**

## 仕様

出発地と目的地、そして人数と宿泊数を入力することで旅行にいくらかかるか簡単な見積もりを出してくれます。

地名はオートコンプリートを使って補完していますが、APIの仕様枠を超えると利用できなくなります。そうなったらなるべく都道府県名から入力してください。思っていたのとは違う場所の同じ名前の地名で見積もりがされてしまいます。

## Technologies used

- Flask
- jQuery
- NAVITIME API for Rakuten RapidAPI
- Bootstrap
- Heroku
- Gunicorn

## 見積もりの出し方

1. ユーザーが情報を入力
2. 出発地の目的地の住所の取得
3. 移動経路をだして高速料金を出す
4. 高速料金とガソリン代を足す
5. 宿代を足す
6. 見積もり完成！！

## 改善したいところ

- オプションで旅行先でやることを追加できるようにする。テーマパーク、キャンプ、温泉、スキー・スノーボード、シュノーケリング、レンタカーなど
- ホテルの値段が一律なので検索ごとに値段をを取得して計算する。
- ロード画面を変える
- 海外旅行対応
- 処理を早くするためにバックエンドにFastAPIを使う
- データベースの追加

