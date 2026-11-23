# print("*** Astrum mehmonxonasiga xush kelibsiz!")
# mehmonlar =[]
# sigim =10
# while True:
#
#     print("1 - mehmon qoshish")
#
#     print("2 - mehmonni royxatdan chiqarish")
#
#     print("3 - mehmonlar royxati")
#
#     print("0 - chiqish")
#     tanlov = input("Nima buyurasiz: ")
#
#     if  tanlov == "1":
#         if len(mehmonlar)>=sigim:
#             print("Joy yoq")
#         else:
#             ism = input("ism kiriting: ")
#             xona = input("xona raqamini kiriting: ")
#             tur = input("turini kiriting: ")
#             mehmon = {"ism": ism, "xona": xona, "tur": tur}
#
#             mehmonlar.append(mehmon)
#             print("Xush kelibsiz ruyxatga kiritildingiz")
#     elif tanlov =="2":
#         if len(mehmonlar) == 0:
#             print("xozirsha mehmon yoq")
#         else:
#             m = input("qaysi xonani boshatay: ")
#             topildi = False
#
#             for mehmon in mehmonlar:
#                 if m == mehmon['xona']:
#
#                     mehmonlar.remove(mehmon)
#                     print("mehmon ochirildi")
#                     topildi =True
#                     break
#             if topildi == False:
#                 print('topilmadi')
#
#     elif tanlov =="3":
#         if len(mehmonlar)==0:
#             print("xozirsha mehmon yoq")
#         else:
#             print(f"{'ism':<20}{'xona':<20}{'tur':<20}")
#             for mehmon in mehmonlar:
#                 print(f"{mehmon['ism']:<20}{mehmon['xona']:<20}{mehmon['tur']:<20}")
#             print(f"jami mehmonlar{len(mehmonlar)}")
#     elif tanlov =="0":
#         print('xayr')
#         break
#     else:
#         print("Notugri buyruq")

# print("*** Astrum mehmonxonasiga xush kelibsiz!")
# mehmonlar =[]
# sigim =10
# while True:
#
#     print("1 - mehmon qoshish")
#
#     print("2 - mehmonni royxatdan chiqarish")
#
#     print("3 - mehmonlar royxati")
#
#     print("0 - chiqish")
#     tanlov = input("Nima buyurasiz: ")
#
#     if  tanlov == "1":
#         if len(mehmonlar)>=sigim:
#             print("Joy yoq")
#         else:
#             ism = input("ism kiriting: ")
#             xona = input("xona raqamini kiriting: ")
#             tur = input("turini kiriting: ")
#             mehmon = {"ism": ism, "xona": xona, "tur": tur}
#
#             mehmonlar.append(mehmon)
#             print("Xush kelibsiz ruyxatga kiritildingiz")
#     elif tanlov =="2":
#         if len(mehmonlar) == 0:
#             print("xozirsha mehmon yoq")
#         else:
#             m = input("qaysi xonani boshatay: ")
#             topildi = False
#
#             for mehmon in mehmonlar:
#                 if m == mehmon['xona']:
#
#                     mehmonlar.remove(mehmon)
#                     print("mehmon ochirildi")
#                     topildi =True
#                     break
#             if topildi == False:
#                 print('topilmadi')
#
#     elif tanlov =="3":
#         if len(mehmonlar)==0:
#             print("xozirsha mehmon yoq")
#         else:
#             print(f"{'ism':<20}{'xona':<20}{'tur':<20}")
#             for mehmon in mehmonlar:
#                 print(f"{mehmon['ism']:<20}{mehmon['xona']:<20}{mehmon['tur']:<20}")
#             print(f"jami mehmonlar{len(mehmonlar)}")
#     elif tanlov =="0":
#         print('xayr')
#         break
#     else:
#         print("Notugri buyruq")


