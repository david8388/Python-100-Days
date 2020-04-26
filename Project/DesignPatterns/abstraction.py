class MailServer:
    def sendEmail(self):
        self.__connect()
        self.__authenticate()
        self.__disconnect()

    # All we should know is how to send email, we can ignore connect, disconnect, authenticate func(Hidden
    # unnecessary details).
    def __connect(self):
        print('Connect')

    def __disconnect(self):
        print('Disconnect')

    def __authenticate(self):
        print('Authenticate')


serverA = MailServer()

serverA.sendEmail()