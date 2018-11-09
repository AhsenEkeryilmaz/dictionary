string="QUERY_STRING='adi=can&soyadi=aydın&yas=35&il=izmir'"
a=string[string.find("\'")+1: string.find("\"")]
sozluk=dict(n.split('=') for n in a.split('&'))
print(sozluk)

