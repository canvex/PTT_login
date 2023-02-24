#基本功能測試
import requests

def lineNotifyMessage(token, msg):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code


if __name__ == "__main__":
  token = 'v9mWGP0fj3nHpBZivQV5BjlpcwhaWY5BFSyjW7SJ1yR'
  message = '基本功能測試'
  lineNotifyMessage(token, message)