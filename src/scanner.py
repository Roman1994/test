from urllib.request import urlopen
from urllib.error   import HTTPError
from bs4            import BeautifulSoup



class Scanner :

  def __init__(self, url) :
    self.page                = self.__getHTML(url)
    self.content             = BeautifulSoup(self.page, "xml")
    self.firstName           = self.__firstName()
    self.lastName            = self.__lastName()
    self.handle              = self.__handle()
    self.company             = self.__company()
    self.street              = self.__street()
    self.city                = self.__city()
    self.state               = self.__state()
    self.postalCode          = self.__postalCode()
    self.country             = self.__country()
    self.registrationDate    = self.__registrationDate()
    self.lastUpdate          = self.__lastUpdate()
    self.comments            = self.__comments()
    self.phoneOffice         = self.__phoneOfiice()
    self.phoneMobile         = self.__phoneMobile()
    self.phoneOther          = self.__phoneOther()
    self.email               = self.__email()
    self.organizationsName   = None
    self.organizationsHandle = None
    self.__relatedOrg(url)

  def __getHTML(self, url) :
    try :
      page = urlopen(url)
      return page.read()
    except HTTPError :
      return None

  def __firstName(self) :
    temp = (self.content).find('firstName')
    if temp :
      temp = temp.contents
      return str(temp[0])
    else :
      return None

  def __lastName(self) :
    temp = (self.content).find('lastName')
    if temp :
      temp = temp.contents
      return str(temp[0])
    else :
      return None

  def __handle(self) :
    temp = (self.content).find('handle')
    if temp :
      temp = temp.contents
      return str(temp[0])
    else :
      return None

  def __company(self) :
    temp = (self.content).find('companyName')
    if temp :
      temp = temp.contents
      return str(temp[0])
    else :
      return None

  def __street(self) :
    temp = (self.content).find('streetAddress')
    if temp :
      temp = temp.children
      s = ''
      for child in temp :
        s += str(child.contents[0])
      return s
    else :
      return None

  def __city(self) :
    temp = (self.content).find('city')
    if temp :
      temp = temp.contents
      return str(temp[0])
    else :
      return None

  def __state(self) :
    temp = (self.content).find('iso3166-2')
    if temp :
      temp = temp.contents
      return str(temp[0])
    else :
      return None

  def __postalCode(self) :
    temp = (self.content).find('postalCode')
    if temp :
      temp = temp.contents
      return str(temp[0])
    else :
      return None

  def __country(self) :
    temp = (self.content).find('iso3166-1')
    if temp :
      temp = temp.find('code2')
      if temp :
        temp = temp.contents
        return str(temp[0])
      else :
        return None
    else :
      return None

  def __registrationDate(self) :
    temp = (self.content).find('registrationDate')
    if temp :
      temp = temp.contents
      return str(temp[0])
    else :
      return None

  def __lastUpdate(self) :
    temp = (self.content).find('updateDate')
    if temp :
      temp = temp.contents
      return str(temp[0])
    else :
      return None

  def __comments(self) :
    temp = (self.content).find('comment')
    if temp :
      s = ''
      temp = temp.children
      for child in temp :
        s += str(child.contents[0])
      return s
    else :
      return None

  def __phoneOfiice(self) :
    temp = (self.content).find('phones')
    if temp :
      for child in temp.children :
        if str(child.type.description.contents[0]) == 'Office' :
          return str(child.number.contents[0])
    else :
      return None

  def __phoneMobile(self) :
    temp = (self.content).find('phones')
    if temp :
      for child in temp.children :
        if str(child.type.description.contents[0]) == 'Mobile' :
          return str(child.number.contents[0])
    else :
      return None

  def __phoneOther(self) :
    temp = (self.content).find('phones')
    if temp :
      for child in temp.children :
        if str(child.type.description.contents[0]) != 'Office' \
           and                                                 \
           str(child.type.description.contents[0]) != 'Mobile' :
          return str(child.number.contents[0])
    else :
      return None

  def __email(self) :
    temp = (self.content).find('emails')
    if temp :
      s = ''
      for child in temp.children :
        s += str(child.contents[0])
      return s
    else :
      return None

  def __relatedOrg(self, url) :
    urlOrgs = url + '/orgs'
    orgsXML = self.__getHTML(urlOrgs)
    if orgsXML != None :
      content = BeautifulSoup(orgsXML, "xml")
      string  = str(content.orgPocLinkRef)
      if string :
        self.organizationsName   = self.__name(string)
        self.organizationsHandle = self.__relOrgHandle(string)
    else :
      self.organizationsHandle = None
      self.organizationsName   = None

  def __name(self, string) :
    string = string.partition('name')
    temp   = string[2].partition('relPocDescription')
    return temp[0]
  def __relOrgHandle(self, string) :
    string = string.partition('handle')
    temp   = string[2].partition('name')
    return temp[0]