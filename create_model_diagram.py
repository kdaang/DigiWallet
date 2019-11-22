import os


def main():
    os.system('python3 manage.py graph_models -a -g -o model_diagram.png')
    print('~~MODEL DIAGRAM CREATED~~')


if __name__ == '__main__':
    main()
