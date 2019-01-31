#coding:utf-8

#大学生協のプリペイドカード利用履歴をhttps://mp.seikyou.jpから取得し、表示する。
#今月の履歴しか表示しない（できない）。

from bs4 import BeautifulSoup
import requests

payload={
    'loginId':'AAAAAAAAAAAA', #各自のログインID
    'password':'AAAAAAAAAAAA' #各自のパスワード
}

session=requests.session()

#ログイン
res=session.post('https://mp.seikyou.jp/mypage/Auth.login.do', data=payload)

#食の履歴へ
payload2={'id':'MEAL_HISTORY'}
url_mypage="https://mp.seikyou.jp/mypage/Menu.change.do?pageNm=MEAL_HISTORY"
res_my = session.post(url_mypage,data=payload2)
soup = BeautifulSoup(res_my.text, "html.parser")

message='\n'

#残高等を表示
es=soup.find_all("td", class_="align_right")
message+=("{}\n".format(es[4].getText()))
message+=("プリペイド残高: {}\n".format(es[2].getText()))

#購入した商品を表示
message+="------\n購入履歴\n"
elems2=soup.select("td")
s=21
while(s<len(elems2)-1):
    if(elems2[s].getText()[-1]==")"):
        message+="------\n"
        message+=("{} は {}を使用\n".format(elems2[s].getText().strip(),elems2[s+1].getText().strip()[3:7]))
        message+=("{}\n".format(elems2[s+1].getText().strip()[8:]))
        
        s+=4
    if(elems2[s].getText().strip()[:2]=="阪大"):
        message+=("{} で {} に\n".format(elems2[s].getText().strip(),elems2[s-1].getText().strip())) #場所,時間
        message+=("{} を食べる\n".format(elems2[s+1].getText().strip()))
    s+=1

print(message) #結果表示

#LINEに結果を送信する(適宜)
"""
line_notify_token='' #各自の発行したトークン
line_notify_api='https://notify-api.line.me/api/notify'

payload={'message':message}
headers={'Authorization': 'Bearer ' + line_notify_token} 
line_notify=requests.post(line_notify_api,data=payload,headers=headers)
print("送信成功")

"""
