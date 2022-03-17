import pandas as pd
from selenium import webdriver
import time
from Pages import pages
if __name__ == '__main__':
    Urun_Adi=[]
    Urun_Resmi=[]
    Brand=[]
    ArticleNumber=[]
    Collection=[]
    Category=[]
    Fabric=[]
    Material=[]
    Manufacturing=[]
    Rapport=[]
    Martindale=[]
    Properties=[]
    Care_instructions=[]
    textler = ""

    Pages1=pages()
    sayfa_sayisi=Pages1.sayfa_sayisi_bulma()
    Pages1.urun_sayisi_ve_linki_bulma(sayfa_sayisi)
    tolltips,urun_adi=Pages1.ust_urun_sayfalarini_gezinme()

    for i in Pages1.Urun_Listesi:
        Urun_Adi.append(i.urun_adi)
        Urun_Resmi.append(i.urun_resmi)
        Brand.append(i.brand)
        ArticleNumber.append(i.articlenumber)
        Collection.append(i.collection)
        Category.append(i.category)
        Fabric.append(i.fabric)
        Material.append(i.material)
        Manufacturing.append(i.manufacturing)
        Rapport.append(i.rapport)
        Martindale.append(i.martindale)
        Properties.append(i.property)
        for text in i.care_instructions:
            textler=textler+text+","

    df_list = {"urun_adi": Urun_Adi,
               "urun_resmi": Urun_Resmi,
               "brand": Brand,
               "article_number": ArticleNumber,
               "collection": Collection,
               "category": Category,
               "fabric": Fabric,
               "material": Material,
               "manufacturing": Manufacturing,
               "rapport": Rapport,
               "martindale": Martindale,
               "property": Properties,
               "care_instructions": Care_instructions,}
    dataframe = pd.DataFrame(df_list)
    print(dataframe)

