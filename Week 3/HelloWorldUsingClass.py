class helloWorld():

    def getHello(self):
        print("Hello World")

    def getStringMessage(self, message):
        print("Hello, you provided - ", message)


def main():
    objectHW = helloWorld()
    objectHW.getHello()
    objectHW.getStringMessage("Param")


if __name__ == "__main__":
    main()