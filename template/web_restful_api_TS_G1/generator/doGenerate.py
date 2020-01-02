from lib import Utils, Data

target = [
    Data.Target('info', '资讯'),
    Data.Target('project', '项目'),
    Data.Target('activity', '活动'),
    Data.Target('dynamics', '动态'),
    Data.Target('collect', '收藏'),
    Data.Target('focus', '关注'),
    Data.Target('claim', '认领'),
    Data.Target('requirement', '需求'),
    Data.Target('message', '消息'),
    Data.Target('feedback', '反馈'),
    Data.Target('score', '评分'),
    Data.Target('like', '点赞'),
    Data.Target('pay', '支付'),
]
for group in target:
    content = Utils.template('BaseFullService', 'web_restful_api_TS_G1').render(name=group.name, alias=group.alias)
    with open('../dist/' + group.name + 'ervice' + '.ts', 'w') as fp:
        fp.write(content)

    content = Utils.template('BasePartService', 'web_restful_api_TS_G1').render(name=group.name, alias=group.alias)
    with open('../dist/' + 'user_' + group.name + 'Service' + '.ts', 'w') as fp:
        fp.write(content)

    content = Utils.template('route', 'web_restful_api_TS_G1').render(name=group.name, alias=group.alias)
    with open('../dist/' + 'route_' + group.name + '.ts', 'w') as fp:
        fp.write(content)
