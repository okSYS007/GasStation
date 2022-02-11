
from authorization import autorizate

USER_AUTORIZATE = False

def main():
    USER_AUTORIZATE = autorizate()


if __name__ == '__main__':
    main()