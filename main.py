import requests
import json

BASE_API = 'http://api.turinglabs.net/api/v1/jd/'


CATOGORY =  ['jxfactory','bean','farm','pet','ddfactory']

def parse_json(s):
    begin = s.find('{')
    end = s.rfind('}') + 1
    return json.loads(s[begin:end])

def submitCode(code,catogory):
  url = f'{BASE_API+catogory}/create/{code}'
  try:
    res= requests.request('GET',url,headers = {
      "Content-Type":"application/x-www-form-urlencoded"
    })
    if res and res.text:
      if(parse_json(res.text)['code']== 200):
        print(code+':提交成功')
      else:
        print(code+':提交失败:'+parse_json(res.text)['message'])
    else: 
      print(code+':提交失败')
      pass
  except requests.exceptions.Timeout:
      print('超时(%ss)')
  except requests.exceptions.RequestException as request_exception:
    print('发生网络请求异常：%s', request_exception)
  except Exception as e:
    print('发生异常, resp: %s, exception: %s', e)

for cat in CATOGORY:
  try:
    file = open(f'{cat}.txt','r')
    codes = file.read()
    codeList = codes.split('@')
    print(cat+':开始提交')
    for code in codeList:
      if code:
        submitCode(code,cat)
    file.close()
  except Exception as e:
    print(e)
