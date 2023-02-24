import PyPtt
import line_notify

ptt_bot = PyPtt.API()

token = '' #line notify的token
ptt_id='' #換成自己的ptt帳號
ptt_pw='' #換成自己的ptt密碼
try:
    ptt_bot.login(
        ptt_id, ptt_pw, kick_other_session=False)
    user_info=ptt_bot.get_user(ptt_id) #用戶資訊
    user_name = ptt_bot.get_user(ptt_id)[PyPtt.UserField.ptt_id]  #用戶名稱
    user_logindays = ptt_bot.get_user(ptt_id)[PyPtt.UserField.login_count] #登入天數
    message = f"{user_name}已登入 {user_logindays} 天" 
    line_notify.lineNotifyMessage(token, message) #傳送line notify通知
    # print(user_info)
except PyPtt.LoginError:
    print('登入失敗')
except PyPtt.WrongIDorPassword:
    print('帳號密碼錯誤')
except PyPtt.LoginTooOften:
    print('請稍等一下再登入')
finally:
     ptt_bot.logout()

