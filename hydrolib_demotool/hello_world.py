from faker import Faker
import hydrolib.core

def hello_world():
    print('==========================================================================')
    print('HELLO WORLD for ' + __name__)

    faker = Faker()

    print('')
    print('..........................................................................')
    print('Test demo dependency on Faker package:')
    print(f'faker.text(): {faker.text()}')

    print('')
    print('..........................................................................')
    print('Test demo dependency on hydrolib-core package:')
    print(f'hydrolib.core.__version__: {hydrolib.core.__version__}')
