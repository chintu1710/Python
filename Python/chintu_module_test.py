name = 'chintu'
surname = 'chaure'
college = 'BMCT'
age = 18

def table(x):
    for i in range(1,11):
        print(f'{x}x{i} = {x*i}')


def greet(x):
    print(f'Good Morning Mr. {x.upper()}')

def area_circle(r):
    print(f'Area of Circle is = {3.14*r*r}')
    print(f'Circumeferrence of Circle is = {3.14*r*2}')