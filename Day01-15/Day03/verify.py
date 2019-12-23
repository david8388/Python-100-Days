username = input('請輸入帳號：')
password = input('請輸入密碼：')

if username == 'admin' and password == '123456':
    print('身份驗證成功')
else:
    print('身份驗證失敗')