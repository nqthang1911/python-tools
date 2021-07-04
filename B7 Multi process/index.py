from multiprocessing import Pool
import time
#work = (['A',5],['B',2],['C',1],['D',3])
'''
def cube(x):
    print(x)
    time.sleep(3)
    return x**3
    
def pool_handler():  
    p = Pool(4)
    kq = p.map_async(cube, (1,2,3,4,5))
    #kq = p.map(cube, range(1,7))
    print('please')
    print(kq.get())
    p.close()
    p.join()
    print('Task ended. Pool join.')
'''
    
def sum(param):
    x = param[0]
    y = param[1]
    print(x)
    #time.sleep(3)
    return x+y

def pool_handler():  
    p = Pool(2)
    kq = p.map_async(sum, ([1,2],[3,4],[4,5]))
    #kq = p.map(cube, range(1,7))
    print('please...')
    print(kq.get())
    p.close()
    p.join()
    print('Task ended. Pool join.')

if __name__== '__main__':
    pool_handler()