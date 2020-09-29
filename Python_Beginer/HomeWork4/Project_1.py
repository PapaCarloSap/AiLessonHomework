import sys


def get_salary(time_work, hourly_rate, prize):
    return (time_work*hourly_rate)+prize

def main():
    print(get_salary(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])))

if __name__ == '__main__':
    main()
