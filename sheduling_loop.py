import sched, time

iteration = 1
s = sched.scheduler(time.time, time.sleep)

def user_function(arg):
    #time.sleep(round(random.random()*10, 1))
    print(iteration, ') ', "From print_time", 'timestamp_now = ', round(time.time(), 1), 'delay = ', arg['delay'], ', runtime = ', round(time.time() - arg['arg'], 1))

def sched_recursive(arg='default'):
    global iteration
    start_time = arg['arg']
    delay = arg['delay']
    user_function(arg)   #   USER-FUNC
    iteration = iteration + 1
    if iteration < arg['iterations']:
        s.enter(delay, 0, sched_recursive, kwargs={'arg': arg})
        s.run()

def sched_init():
    start_time = round(time.time(), 1)
    arg = {'arg': start_time, 'delay': 3, 'iterations': 6}
    s.enter(arg['delay'], 0, sched_recursive, kwargs={'arg': arg})
    s.run()
    print('runtime = ', round(time.time() - start_time, 1))

sched_init()
