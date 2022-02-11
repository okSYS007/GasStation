
from authorization import autorizate

USER_AUTORIZATE = False

def main():
    USER_AUTORIZATE = autorizate()
    print(USER_AUTORIZATE)

if __name__ == '__main__':
    main()