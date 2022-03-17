from selenium import webdriver
from Product_Details import ProductDetails
class pages:
    browser = webdriver.Chrome("C:\Program Files\driver\chromedriver.exe")
    ana_sayfa_list = []
    Urun_Listesi=[]

    def __init__(self):
        self.browser.get("https://www.zimmer-rohde.com/en/product-finder?tx_snsproducts_products%5Bpage%5D=1&cHash=942ea42b4fe1dde9828097e144048111")
        self.browser.find_element_by_class_name("select-all").click()

    def sayfa_sayisi_bulma(self):
        #bu metodda ana olan tüm sayfaları gezerek sayfa linkini sayfa_liste ekler.
        sayfa_sayisi = ""
        sayfa_sayisi = self.browser.find_element_by_xpath("//*[@id='product-listing']/div[3]/nav/ul/li[5]").find_element_by_tag_name("a").text
        for i in range(0, int(sayfa_sayisi) - 1):
            sonraki_sayfa = self.browser.find_element_by_class_name("next").get_attribute("href")
            self.ana_sayfa_list.append(sonraki_sayfa)
            self.browser.get(sonraki_sayfa)
        self.browser.get("https://www.zimmer-rohde.com/en/product-finder?tx_snsproducts_products%5Bpage%5D=1&cHash=942ea42b4fe1dde9828097e144048111")
        return sayfa_sayisi


    def urun_sayisi_ve_linki_bulma(self,sayfa_sayisi):
        # bu metodda tüm sayfalardaki ürün sayisi ve o ürünlerin linkleri alınır.
        y = 0
        urun_sayfa_linki = []
        urun_sayisi = 0
        for i in range(0, int(sayfa_sayisi) + 1):
            #bulunduğun sayfadaki ürün sayısı
            href_sayisi = self.browser.find_elements_by_class_name("product-detail")
            for i in href_sayisi:
                urun_sayisi+=1
            x = 1
            for i in range(1, urun_sayisi + 1):
                # bulunduğun sayfadaki ürünlerin linki
                  urun_sayfa_linki.append(self.browser.find_element_by_xpath("//*[@id='product-listing']/div[3]/div[" + str(x) + "]/div/div[2]/a").get_attribute("href"))
                  x += 1
            self.ust_urun_sayfalarini_gezinme(urun_sayfa_linki)
            urun_sayisi = 0
            urun_sayfa_linki.clear()
            if y < 14:
                self.browser.get(self.ana_sayfa_list[y])
                y += 1

    def ust_urun_sayfalarini_gezinme(self,urun_sayfa_linki):
        #bu metodda anlık sayfadaki ürünler gezilir
        for urun_sayfa in urun_sayfa_linki:
            urun_adi = ""
            self.browser.get(urun_sayfa)
            srcler = self.browser.find_element_by_class_name("thumbnails")
            tooltips = srcler.find_elements_by_class_name("tooltip")
            urun_adi = self.browser.find_element_by_class_name("product-infos").find_element_by_tag_name("h2").text
            return tooltips,urun_adi

    def alt_sayfalari_listeye_alma(self,tooltips,urun_adi):
        #bulunduğun sayfadaki ürünün diğer alt ürünlerini diziye ekleme
        alt_sayfa_src = []
        for t in tooltips:
            alt_sayfa_src.append(t.find_element_by_tag_name("a").get_attribute("href"))
        self.alt_sayfa_gezinme_ve_bilgileri_alma(urun_adi,alt_sayfa_src)

    def alt_sayfa_gezinme_ve_bilgileri_alma(self,urun_adi,alt_sayfa_src):
        for alt_sayfa in alt_sayfa_src:
            manufacturing = ""
            rapport = ""
            martindale = ""
            brand = ""
            articlenumber = ""
            collection = ""
            category = ""
            fabric = ""
            material = ""
            property = ""
            care_instructions = []
            urun_resmi = ""
            self.browser.get(alt_sayfa)
            p_properties = self.browser.find_element_by_class_name("product-properties")
            liler = p_properties.find_elements_by_tag_name("li")
            propertysayisi = 0
            for i in liler:

                #toplam özellik sayısı alma liyi kullanarak
                propertysayisi += 1
            for i in range(1, propertysayisi, 2):
                #propertleri xpatlerine göre çekme
                texti = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i) + "]").text
                if texti == "BRAND":
                    brand = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "ARTICLENUMBER":
                    articlenumber = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "COLLECTION":
                    collection = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "CATEGORY":
                    category = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "FABRIC WIDTH":
                    fabric = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "MATERIAL":
                    material = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "MANUFACTURING METHOD":
                    manufacturing = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "RAPPORTWIDTH / RAPPORTHEIGHT":
                    rapport = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "MARTINDALE":
                    martindale = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "PROPERTIES":
                    property = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]").text
                elif texti == "CARE INSTRUCTIONS":
                    care_instruction = self.browser.find_element_by_xpath("//*[@id='c44']/div/div[1]/div[3]/div/div[2]/ul/li[" + str(i + 1) + "]")
                    care_tooltips = care_instruction.find_elements_by_class_name("tooltip")
                    for care in care_tooltips:
                        care_instructions.append(care.find_element_by_tag_name("img").get_attribute("src"))
            self.product_image()
            product = ProductDetails(urun_adi, urun_resmi, brand, articlenumber, collection, category, fabric, material, manufacturing, rapport, martindale, property, care_instructions)
            self.Urun_Listesi.append(product)
           # print(self.urun_adi)
            #print("----------------------------------")
            care_instructions.clear()
        alt_sayfa_src.clear()


    def product_image(self):
        #urunlerin fotosunu alma
        items = self.browser.find_elements_by_class_name("item")
        k = 0
        for item in items:
            index = item.get_attribute("data-index")
            if k == 0:
                if index == "0":
                    self.urun_resmi = item.find_element_by_tag_name("img").get_attribute("src")
                    k += 1
