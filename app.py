from flask import Flask

app = Flask(__name__)

# 注册一个处理函数，这个函数是处理某个请求的处理函数，
# Flask 官方把它叫做视图函数（view funciton），
# 可以理解为“请求处理函数”
# 所谓“注册”，就是给这个函数戴上一个装饰器帽子
# 装饰器为这个函数绑定对应的 URL，当用户在浏览器访问这个 URL的时候，
# 就会触发这个函数，获取返回值，并把返回值显示到浏览器窗口：
# 装饰器的第一个参数是 URL 规则字符串，这里的 /指的是根地址。

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

if __name__ == '__main__':
    app.debug = True
    app.run()

