import xml.etree.ElementTree as etree 
import requests

url = 'http://95.79.53.147:9080/bit_nn123/odata/standard.odata/'
 
service = odata.service(url=url, login='admin', password='')
 
service.Languages
 
languages = service.execute()
 
print languages





# r = requests.get('http://95.79.53.147:9080/bit_nn123/odata/standard.odata/Document_Order', auth=('admin', ''))
# print r.status_code


# print r.headers['content-type']
# print r.encoding
# #rint r.text

# root = etree.fromstring(r.text.encode('utf-8'))

# entrys = root.findall('{http://www.w3.org/2005/Atom}entry')


# for tag in entrys[0]:
# 	print tag.tag

# contents = entrys[0].findall('{http://www.w3.org/2005/Atom}content')
# print 'Amount of entryes: ', len(contents)


# properties = contents[0].findall('{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties')

# for prop in properties[0]:
# 	print prop.tag


#if element.find('...') is not None. 