from flask import Flask

from werkzeug.routing import BaseConverter

from flask import jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 自定义路由规则类
class MyConverter(BaseConverter):
    # 正则
    regex = "my[0-9]{3}"

# 注册到app
app.url_map.converters['aaa'] = MyConverter

# 测试
@app.route('/<aaa:name>')
def re_name(name):
    return name


# 返回json格式
@app.route('/a_json')
def abc():
    d = {
        'name':'隔好远',
        'age':'134',
        'address':'donglu'
    }
    return jsonify(d)
    # return d


@app.route('/')
def hello_world():
    return "Welcome Flask!"

@app.route("/conany/<any(red,blue,green):color>")
def test_color(color):
    return color


if __name__ == '__main__':
    app.run(debug=True)