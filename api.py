import requests

# 燃費：リッター１５ｋｍ、ガソリン価格１５８円
nenpi = 15
gaso = 158


# 地点の緯度・経度の取得
def getPoint(place: str):
  url = "https://navitime-geocoding.p.rapidapi.com/address"

  headers = {
    'x-rapidapi-key': "1a474a5630msh42c5ec5a2ecc003p138341jsn244a05255fac",
    'x-rapidapi-host': "navitime-geocoding.p.rapidapi.com"
  }

  querystring = {
    "offset": "0",
    "sort": "code_asc",
    "word": place,
    "level_from": "3",
    "limit": "1",
    "datum": "wgs84",
    "coord_unit": "degree"
  }

  response = requests.request("GET", url, headers=headers, params=querystring).json()

  # 緯度・経度を文字列として結合
  point = str(response['items'][0]['coord']['lat']) + ',' + str(response['items'][0]['coord']['lon'])
  return point


def calculateCostOfMove(start: str, goal: str) -> int:
  url = "https://navitime-route-car.p.rapidapi.com/route_car"

  headers = {
    'x-rapidapi-key': "1a474a5630msh42c5ec5a2ecc003p138341jsn244a05255fac",
    'x-rapidapi-host': "navitime-route-car.p.rapidapi.com"
  }

  querystring = {
    "goal": goal,
    "start": start,
    "coord_unit": "degree",
    "smart_ic": "use",
    "datum": "wgs84"
  }

  response = requests.request("GET", url, headers=headers, params=querystring).json()

  # 高速料金
  fare = response['items'][0]['summary']['move']['fare']['unit_1025_2']
  # 走行距離
  distance = response['items'][0]['sections'][1]['distance']

  # ガソリン料金
  gasoFare = nenpi / distance * gaso

  return int(fare + gasoFare)
