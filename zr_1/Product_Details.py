import time

class ProductDetails:
    urun_adi=""
    martindale=""
    rapport=""
    manufacturing=""
    urun_resmi=""
    category=""
    fabric=""
    collection=""
    property=""
    articlenumber=""
    brand=""
    material=""
    care_instructions=[]
    def __init__(self,urun_adi, urun_resmi, brand, articlenumber, collection, category, fabric, material, manufacturing, rapport, martindale, property, care_instructions):
       self.urun_adi=urun_adi
       self.urun_resmi=urun_resmi
       self.brand=brand
       self.articlenumber=articlenumber
       self.collection=collection
       self.category=category
       self.fabric=fabric
       self.material=material
       self.manufacturing=manufacturing
       self.rapport=rapport
       self.martindale=martindale
       self.property=property
       self.care_instructions=care_instructions
