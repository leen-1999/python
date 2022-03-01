if True:
    if True:
        print("I Love Python")
        print("I Love Programming")
if True:
    print("I Love Python")
    print("I Love Programming")
# eğer birden fazla statement yanyane yazmak istersek aralarına ; koymak şart ama
# formatter çalışıyorsa  dosyayı kaydıderken bunu düzeltir yani yanyana olan satırları
# altalta sıralar. Formatter'ın çalışıp çalışmadığını kontrol etmek için file/preferrences/format on save den kontrol edebiliriz

# indentation koymak için, bir şeyin büyük bir şeye tabi olması gerkiyor(child)
# block of code yaparken bütün ifadelerin aynı indentation'de olması lazım yoksa synatax error alırız
# örenk:
# if True:
#     print("I Love Python")
#     print("I Love Programming")
# if True:
#     print("I Love Python")
#     print("I Love Programming")

#  Hata vermez ama,

#  if True:
#     print("I Love Python")
#        print("I Love Programming")
# if True:
#     print("I Love Python")
#     print("I Love Programming")

# hata verir   print("I Love Programming") buradaki indentaion farkı yüzünden

# her altalta olan block of code'lardan önce mesafe olması lazım
