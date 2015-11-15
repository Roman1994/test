class Export :

  def __init__(self, scanner) :
    self.firstName        = self.__firstName(scanner.firstName)
    self.lastName         = self.__lastName(scanner.lastName)
    self.fullName         = self.__fullName()
    self.handle           = scanner.handle
    self.company          = scanner.company
    self.street           = scanner.street
    self.city             = scanner.city
    self.state            = scanner.state
    self.postalCode       = scanner.postalCode
    self.country          = scanner.country
    self.registrationDate = scanner.registrationDate
    self.lastUpdate       = scanner.lastUpdate
    self.comments         = self.__comments(scanner.comments)
    self.officePhone      = self.__phone(scanner.phoneOffice)
    self.mobilePhone      = self.__phone(scanner.phoneMobile)
    self.otherPhone       = self.__phone(scanner.phoneOther)
    self.email            = scanner.email
    self.relOrgName       = self.__relOrgName(scanner.organizationsName)
    self.relOrgHandle     = self.__relOrgHandle(scanner.organizationsHandle)
    self.output()

  def __firstName(self, firstName) :
    firstName = firstName.split()
    return firstName[0].capitalize()

  def __lastName(self, lastName) :
    lastName = lastName.split()
    return ' '.join(lastName)

  def __fullName(self) :
    if type(self.firstName) == type(None) and type(self.lastName) == str :
      return self.lastName
    elif type(self.firstName) == str and type(self.lastName) == type(None) :
      return self.firstName
    else :
      return self.lastName+', '+self.firstName

  def __comments(self, comments) :
    if comments :
      return comments.splitlines(True)
    else :
      return '_'

  def __phone(self, phone) :
    if phone == None :
      return '_'
    elif phone[0] == '+' :
      return phone[1:]

  def __relOrgName(self, orgName) :
    if orgName :
      return orgName[2:len(orgName)-2]
    else :
      return '_'

  def __relOrgHandle(self, orgHandle) :
    if orgHandle :
      return orgHandle[2:len(orgHandle)-2]
    else :
      return '_'

  def output(self) :
    fileOut = open('output.txt', 'a')
    fileOut.write('%20s: %s\n' % ('First Name', self.firstName))
    fileOut.write('%20s: %s\n' % ('Last Name', self.lastName))
    fileOut.write('%20s: %s\n' % ('Full Name', self.fullName))
    fileOut.write('%20s: %s\n' % ('Handle', self.handle))
    fileOut.write('%20s: %s\n' % ('Company', self.company))
    fileOut.write('%20s: %s\n' % ('City', self.city))
    fileOut.write('%20s: %s\n' % ('State', self.state))
    fileOut.write('%20s: %s\n' % ('Postal Code', self.postalCode))
    fileOut.write('%20s: %s\n' % ('Country', self.country))
    fileOut.write('%20s: %s\n' % ('Registartion Date', self.registrationDate))
    fileOut.write('%20s: %s\n' % ('Last Update', self.lastUpdate))
    fileOut.write('%20s: %s\n' % ('Comments', '\n'.join(self.comments)))
    fileOut.write('%20s: %s\n' % ('Office Phone', self.officePhone))
    fileOut.write('%20s: %s\n' % ('Mobile Phone', self.mobilePhone))
    fileOut.write('%20s: %s\n' % ('Other Phone', self.otherPhone))
    fileOut.write('%20s: %s\n' % ('Email', self.email))
    fileOut.write('%20s: %s\n' % ('Related Org Name', self.relOrgName))
    fileOut.write('%20s: %s\n' % ('Related Org Handle', self.relOrgHandle))
    fileOut.write('\n\n')
