import os


def main():
    os.system('rm -rf cards/migrations/')
    os.system('rm -rf company_customers/migrations/')
    os.system('rm -rf customers/migrations/')
    os.system('rm -rf employees/migrations/')
    os.system('rm -rf merchants/migrations/')
    os.system('rm -rf point_systems/migrations/')
    os.system('rm -rf stores/migrations/')
    os.system('rm -rf transactions/migrations/')
    os.system('rm -rf users/migrations/')
    print('~~CLEARED MIGRATION FILES~~')


if __name__ == '__main__':
    main()
