from lib import Utils


content = Utils.template('route', 'web_restful_api_TS_G1').render(name='test', alias='资讯')
with open('../dist/' + 'route' + '.js', 'w') as fp:
    fp.write(content)
