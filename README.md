# いくよさん
#### Video Demo: https://youtu.be/TkhGPPXWBkg
#### Description: 簡単な旅行の見積もりを出します！

Using Python, Flask, HTML, CSS, Bootstrap, Jquery

Rakuten RapidAPIに公開されているNAVITIMEさんのAPIを利用しました。

これはデモのURLです。是非試してみてください。

[Ikuyosan](https://ikuyosan.herokuapp.com/)

## 仕様

出発地と目的地、そして人数と宿泊数を入力することで旅行にいくらかかるか簡単な見積もりを出してくれます。

地名はオートコンプリートを使って補完していますが、APIの仕様枠を超えると利用できなくなります。そうなったらなるべく都道府県名から入力してください。思っていたのとは違う場所の同じ名前の地名で見積もりがされてしまいます。