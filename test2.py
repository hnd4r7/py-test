def func_kwargs(farg, **dddd):
    print("formal arg:", farg)
    for key in dddd:
        print("keyword arg: %s: %s" % (key, dddd[key]))
func_kwargs(1 ,id=1, name='youzan', city='hangzhou',age ='20',四块五的妞是 = '来日方长的')
