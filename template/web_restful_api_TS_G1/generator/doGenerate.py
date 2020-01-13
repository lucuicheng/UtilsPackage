from lib import Utils, Data

targets = [
    Data.Target('info', '资讯'),
    Data.Target('project', '项目'),
    Data.Target('activity', '活动'),
    Data.Target('dynamic', '动态'),
    Data.Target('collect', '收藏'),
    Data.Target('focus', '关注'),
    Data.Target('claim', '认领'),
    Data.Target('requirement', '需求'),
    Data.Target('message', '消息'),
    Data.Target('feedback', '反馈'),
    Data.Target('score', '评分'),
    Data.Target('like', '点赞'),
    Data.Target('pay', '支付'),
    Data.Target('identity', '认证'),
    Data.Target('comment', '评论'),
]
for group in targets:
    # content = Utils.template('BaseFullService', 'web_restful_api_TS_G1').render(name=group.name, alias=group.alias)
    # with open('../dist/' + group.name.capitalize() + 'Service' + '.ts', 'w') as fp:
    #     fp.write(content)
    #
    # content = Utils.template('BaseFullTestCase', 'web_restful_api_TS_G1').render(name=group.name, alias=group.alias)
    # with open('../dist/test/' + group.name.capitalize() + 'ServiceTest' + '.ts', 'w') as fp:
    #     fp.write(content)
    #

    print('export { default as %sService } from \'./data/%sService\';' % (group.name, group.name.capitalize()))
    # print("import { %s, %sExtraDoc } from '@model/%s';" % (group.name.capitalize(), group.name.capitalize(), group.name.capitalize()))
    # print(group.name + 'Service,')

content = Utils.template('BasePartService', 'web_restful_api_TS_G1').render(group=targets)
with open('../dist/UserService.ts', 'w') as fp:
    fp.write(content)
#
# content = Utils.template('route', 'web_restful_api_TS_G1').render(group=targets)
# with open('../dist/Routes.ts', 'w') as fp:
#     fp.write(content)
#
# content = Utils.template('UsedService', 'web_restful_api_TS_G1').render(group=targets)
# with open('../dist/UsedRoutes.ts', 'w') as fp:
#     fp.write(content)
#
# content = Utils.template('UsedUserService', 'web_restful_api_TS_G1').render(group=targets)
# with open('../dist/UsedUserRoutes.ts', 'w') as fp:
#     fp.write(content)

# content = Utils.template('BasePartTestCase', 'web_restful_api_TS_G1').render(group=targets)
# with open('../dist/test/UserServiceTest.ts', 'w') as fp:
#     fp.write(content)
