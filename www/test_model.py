import orm
import asyncio
from models import User, Comment, Blog


@asyncio.coroutine
def test():
    yield from orm.create_pool(loop=loop, user='root', password='sunhao884082105', database='awesome')
    print('create pool DONE!!')
    user = User(name='Hulk', email='hulk@126.com', passwd='123654', image='about:blank')
    yield from user.save()
    print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(test())

loop.close()