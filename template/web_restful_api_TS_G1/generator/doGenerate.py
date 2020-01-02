from lib import Utils

content = Utils.template('BaseFullService', 'web_restful_api_TS_G1').render(name='info', alias='资讯')
with open('../dist/' + 'InfoService' + '.ts', 'w') as fp:
    fp.write(content)

content = Utils.template('BasePartService', 'web_restful_api_TS_G1').render(name='info', alias='资讯')
with open('../dist/' + 'userInfoService' + '.ts', 'w') as fp:
    fp.write(content)

content = Utils.template('route', 'web_restful_api_TS_G1').render(name='info', alias='资讯')
with open('../dist/' + 'route_info' + '.ts', 'w') as fp:
    fp.write(content)
