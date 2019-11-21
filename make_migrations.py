import os


def main():
    os.system('python3 manage.py makemigrations users')
    os.system('python3 manage.py makemigrations cards')
    os.system('python3 manage.py makemigrations point_systems')
    os.system('python3 manage.py makemigrations merchants')
    os.system('python3 manage.py makemigrations customers')
    os.system('python3 manage.py makemigrations employees')
    os.system('python3 manage.py makemigrations company_customers')
    os.system('python3 manage.py makemigrations stores')
    os.system('python3 manage.py makemigrations transactions')
    os.system('python3 manage.py makemigrations')
    print('~~MAKEMIGRATIONS COMPLETE~~')


if __name__ == '__main__':
    main()
