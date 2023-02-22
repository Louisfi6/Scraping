class Lawyer:
    def __init__(self, name, phoneNumber, email, address, cases, swornDate):
        self.setName(name)
        self.setPhone(phoneNumber)
        self.setEmail(email)
        self.setAddress(address)
        self.setCases(cases)
        self.setSwornDate(swornDate)

    def setName(self, name):
        self.name = name

    def setPhone(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def setEmail(self, email):
        self.email = email

    def setAddress(self, address):
        self.address = address

    def setCases(self, cases):
        self.cases = cases

    def setSwornDate(self, swornDate):
        self.swornDate = swornDate

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phoneNumber

    def getEmail(self):
        return self.email

    def getAddress(self):
        return self.address

    def getCases(self):
        return self.cases

    def getSwornDate(self):
        return self.swornDate
