import sqlite3 as sql
import time

vt = sql.connect('okulotomasyon3.sqlite')
imlec = vt.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS ogrenci_tablosu(ogrenci_id INTEGER PRIMARY KEY AUTOINCREMENT,isim,soyisim,bolum,sinif)")
imlec.execute("CREATE TABLE IF NOT EXISTS ogrencimat_tablosu(ogrenci_id INTEGER PRIMARY KEY AUTOINCREMENT,isim,soyisim,bolum,sinif,vize,kisasinav1,kisasinav2,odev,final)")
imlec.execute("CREATE TABLE IF NOT EXISTS ogrencifizik_tablosu(ogrenci_id INTEGER PRIMARY KEY AUTOINCREMENT,isim,soyisim,bolum,sinif,vize,kisasinav1,kisasinav2,odev,final)")
imlec.execute("CREATE TABLE IF NOT EXISTS ogrencibilisim_tablosu(ogrenci_id INTEGER PRIMARY KEY AUTOINCREMENT,isim,soyisim,bolum,sinif,vize,kisasinav1,kisasinav2,odev,final)")
imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciprogramlama_tablosu(ogrenci_id INTEGER PRIMARY KEY AUTOINCREMENT,isim,soyisim,bolum,sinif,vize,odev1,odev2,odev3,odev4,odev5,odev6,final)")
imlec.execute("CREATE TABLE IF NOT EXISTS ogrencibsmgiris_tablosu(ogrenci_id INTEGER PRIMARY KEY AUTOINCREMENT,isim,soyisim,bolum,sinif,vize,kisasinav1,kisasinav2,final)")
imlec.execute("CREATE TABLE IF NOT EXISTS ogretmen_tablosu(ogretmen_id INTEGER PRIMARY KEY AUTOINCREMENT ,ad,soyadi,bolumu,unvan)")
imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik (kitap_id INTEGER PRIMARY KEY AUTOINCREMENT,kitap_adi,kitap_yayinevi,kitap_adedi,kitap_yazari,kitap_durumu)")
vt.commit()

def asel_bilgi_iletişim():
    print("""
    
    ***** ASEL ÜNİVERSİTESİ ***** 
                
                GELECEĞE ŞEKİL VERİR...
                
    İLETİŞİM;
    
    OKUL REKTÖRÜ : 0538 041 0744
    ÖĞRENCİ İŞLERİ : 0216 592 4587 
    
    SALLAMA MAHALLESİ , ORASI CADDESİ , SULTANBEYLİ / İSTANBUL
    
    """)

def kitap_ekle():
    kitap = input("Kitap adını giriniz : ")
    yazar = input("Kitabın yazarını giriniz : ")
    yayinevi = input("Kitabın yayınevini giriniz : ")
    adet = input("Kitap adedini giriniz : ")
    durum = input("Kitabın durumunu giriniz (stokta var/yok): ")
    kitap_girisi = "INSERT INTO kitaplik (kitap_adi,kitap_yayinevi,kitap_yazari,kitap_adedi,kitap_durumu) VALUES ('" + kitap + "','" + yayinevi + "','" + yazar + "','" + adet + "','" + durum + "')"
    print("KİTAP KAYDI YAPILIYOR...")
    time.sleep(1)
    print("KAYIT İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ.")
    imlec.execute(kitap_girisi)

    vt.commit()

def kitap_sil():
    silinecek = input("Slinecek kitabın İD numarasını giriniz : ")

    imlec.execute("DELETE FROM kitaplik WHERE kitap_id = '" + silinecek + "'")
    print("İŞLEM YAPILIYOR.")
    print("")
    print("")
    time.sleep(1)
    print("İŞLEM BAŞARIYLA GERÇEKLEŞMİŞTİR.")

    vt.commit()

def kitap_listele():
    # eğer kullanıcıdan alacaksan yıldız yerine input ile al ve oraya yukardaki gibi artı tırnak karışık olanı koy.
    imlec.execute("SELECT * FROM kitaplik")
    kitaplar = imlec.fetchall()
    print("İŞLEM YAPILIYOR...")
    print("")
    print("")
    time.sleep(1)

    for i in kitaplar:
        for k in i:
            print(k, end=" ")
        print("")

def kitap_guncelle_durum():
    yenidurum = input("yeni durumu girin : ")
    kitapid = input("fiyatını değiştirmek istedğin id : ")
    imlec.execute("UPDATE kitaplik SET fiyati = '" + yenidurum + "' WHERE kitap_id = '" + kitapid + "'")
    print("İŞLEMİNİZ YAPILIYOR...")
    print("")
    time.sleep(2)
    print("GÜNCELLEME BAŞARIYLA GERÇEKLEŞMİŞTİR.")
    vt.commit()

def ogrencimat_kayit():
    ogrenci_adi = input("Öğrenci adı : ")
    ogrenci_soyadi = input("Ögrenci soyadı : ")
    ogrenci_bolumu = input("Öğreci bölümü : ")
    ogrenci_sinif = input("Öğrencinin sınıfı : ")

    yeniAd_sorgu="SELECT DISTINCT isim FROM ogrenci_tablosu WHERE isim='"+ogrenci_adi+"'"
    imlec.execute(yeniAd_sorgu)
    yeniAd =imlec.fetchall()
    yeniSoyad_sorgu = "SELECT DISTINCT soyisim FROM ogrenci_tablosu WHERE soyisim='"+ogrenci_soyadi+"'"
    imlec.execute(yeniSoyad_sorgu)
    yeniSoyad =imlec.fetchall()
    yenibolum_sorgu = "SELECT DISTINCT bolum FROM ogrenci_tablosu WHERE bolum='"+ogrenci_bolumu+"'"
    imlec.execute(yenibolum_sorgu)
    yenibolum =imlec.fetchall()
    yenisinif_sorgu = "SELECT DISTINCT sinif FROM ogrenci_tablosu WHERE sinif='"+ogrenci_sinif+"'"
    imlec.execute(yenisinif_sorgu)
    yenisinif =imlec.fetchall()

    if(len(yeniAd)==0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif(len(yeniSoyad)==0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif(len(yenibolum)==0) :
        imlec.execute( "INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif(len(yenisinif)==0):
        imlec.execute( "INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    else:
        print(" Kişi okulda kayıtlı.")

    yeniAdi_sorgu = "SELECT DISTINCT isim FROM ogrencimat_tablosu WHERE isim='" + ogrenci_adi + "'"
    imlec.execute(yeniAdi_sorgu)
    yeniAdi = imlec.fetchall()
    yeniSoyadi_sorgu = "SELECT DISTINCT soyisim FROM ogrencimat_tablosu WHERE soyisim='" + ogrenci_soyadi + "'"
    imlec.execute(yeniSoyadi_sorgu)
    yeniSoyadi = imlec.fetchall()
    yenibolumu_sorgu = "SELECT DISTINCT  bolum FROM ogrencimat_tablosu WHERE bolum='" + ogrenci_bolumu + "'"
    imlec.execute(yenibolumu_sorgu)
    yenibolumu = imlec.fetchall()
    yenisinifi_sorgu = "SELECT DISTINCT sinif FROM ogrencimat_tablosu WHERE sinif='" + ogrenci_sinif + "'"
    imlec.execute(yenisinifi_sorgu)
    yenisinifi = imlec.fetchall()

    if (len(yeniAdi) == 0):
        imlec.execute( "INSERT INTO ogrencimat_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yeniSoyadi) == 0):
        imlec.execute("INSERT INTO ogrencimat_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenibolumu) == 0):
        imlec.execute("INSERT INTO ogrencimat_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenisinifi) == 0):
        imlec.execute( "INSERT INTO ogrencimat_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    else:
        print(" kisi mevcut")

def ogrencifizik_kayit():
    ogrenci_adi = input("Öğrenci adı : ")
    ogrenci_soyadi = input("Ögrenci soyadı : ")
    ogrenci_bolumu = input("Öğreci bölümü : ")
    ogrenci_sinif = input("Öğrencinin sınıfı : ")

    yeniAd_sorgu = "SELECT DISTINCT isim FROM ogrenci_tablosu WHERE isim='" + ogrenci_adi + "'"
    imlec.execute(yeniAd_sorgu)
    yeniAd = imlec.fetchall()
    yeniSoyad_sorgu = "SELECT DISTINCT soyisim FROM ogrenci_tablosu WHERE soyisim='" + ogrenci_soyadi + "'"
    imlec.execute(yeniSoyad_sorgu)
    yeniSoyad = imlec.fetchall()
    yenibolum_sorgu = "SELECT DISTINCT bolum FROM ogrenci_tablosu WHERE bolum='" + ogrenci_bolumu + "'"
    imlec.execute(yenibolum_sorgu)
    yenibolum = imlec.fetchall()
    yenisinif_sorgu = "SELECT DISTINCT sinif FROM ogrenci_tablosu WHERE sinif='" + ogrenci_sinif + "'"
    imlec.execute(yenisinif_sorgu)
    yenisinif = imlec.fetchall()

    if (len(yeniAd) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yeniSoyad) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yenibolum) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yenisinif) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    else:
        print(" Kişi okulda kayıtlı.")

    yeniAdi_sorgu = "SELECT DISTINCT isim FROM ogrencifizik_tablosu WHERE isim='" + ogrenci_adi + "'"
    imlec.execute(yeniAdi_sorgu)
    yeniAdi = imlec.fetchall()
    yeniSoyadi_sorgu = "SELECT DISTINCT soyisim FROM ogrencifizik_tablosu WHERE soyisim='" + ogrenci_soyadi + "'"
    imlec.execute(yeniSoyadi_sorgu)
    yeniSoyadi = imlec.fetchall()
    yenibolumu_sorgu = "SELECT DISTINCT  bolum FROM ogrencifizik_tablosu WHERE bolum='" + ogrenci_bolumu + "'"
    imlec.execute(yenibolumu_sorgu)
    yenibolumu = imlec.fetchall()
    yenisinifi_sorgu = "SELECT DISTINCT sinif FROM ogrencifizik_tablosu WHERE sinif='" + ogrenci_sinif + "'"
    imlec.execute(yenisinifi_sorgu)
    yenisinifi = imlec.fetchall()

    if (len(yeniAdi) == 0):
        imlec.execute("INSERT INTO ogrencifizik_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yeniSoyadi) == 0):
        imlec.execute("INSERT INTO ogrencifizik_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenibolumu) == 0):
        imlec.execute("INSERT INTO ogrencifizik_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenisinifi) == 0):
        imlec.execute("INSERT INTO ogrencifizik_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    else:
        print(" kisi mevcut")

def ogrencibilisim_kayit():
    ogrenci_adi = input("Öğrenci adı : ")
    ogrenci_soyadi = input("Ögrenci soyadı : ")
    ogrenci_bolumu = input("Öğreci bölümü : ")
    ogrenci_sinif = input("Öğrencinin sınıfı : ")

    yeniAd_sorgu = "SELECT DISTINCT isim FROM ogrenci_tablosu WHERE isim='" + ogrenci_adi + "'"
    imlec.execute(yeniAd_sorgu)
    yeniAd = imlec.fetchall()
    yeniSoyad_sorgu = "SELECT DISTINCT soyisim FROM ogrenci_tablosu WHERE soyisim='" + ogrenci_soyadi + "'"
    imlec.execute(yeniSoyad_sorgu)
    yeniSoyad = imlec.fetchall()
    yenibolum_sorgu = "SELECT DISTINCT bolum FROM ogrenci_tablosu WHERE bolum='" + ogrenci_bolumu + "'"
    imlec.execute(yenibolum_sorgu)
    yenibolum = imlec.fetchall()
    yenisinif_sorgu = "SELECT DISTINCT sinif FROM ogrenci_tablosu WHERE sinif='" + ogrenci_sinif + "'"
    imlec.execute(yenisinif_sorgu)
    yenisinif = imlec.fetchall()

    if (len(yeniAd) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yeniSoyad) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yenibolum) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yenisinif) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    else:
        print(" Kişi okulda kayıtlı.")

    yeniAdi_sorgu = "SELECT DISTINCT isim FROM ogrencibilisim_tablosu WHERE isim='" + ogrenci_adi + "'"
    imlec.execute(yeniAdi_sorgu)
    yeniAdi = imlec.fetchall()
    yeniSoyadi_sorgu = "SELECT DISTINCT soyisim FROM ogrencibilisim_tablosu WHERE soyisim='" + ogrenci_soyadi + "'"
    imlec.execute(yeniSoyadi_sorgu)
    yeniSoyadi = imlec.fetchall()
    yenibolumu_sorgu = "SELECT DISTINCT  bolum FROM ogrencibilisim_tablosu WHERE bolum='" + ogrenci_bolumu + "'"
    imlec.execute(yenibolumu_sorgu)
    yenibolumu = imlec.fetchall()
    yenisinifi_sorgu = "SELECT DISTINCT sinif FROM ogrencibilisim_tablosu WHERE sinif='" + ogrenci_sinif + "'"
    imlec.execute(yenisinifi_sorgu)
    yenisinifi = imlec.fetchall()

    if (len(yeniAdi) == 0):
        imlec.execute("INSERT INTO ogrencibilisim_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yeniSoyadi) == 0):
        imlec.execute("INSERT INTO ogrencibilisim_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenibolumu) == 0):
        imlec.execute("INSERT INTO ogrencibilisim_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenisinifi) == 0):
        imlec.execute("INSERT INTO ogrencibilisim_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    else:
        print(" kisi mevcut")

def ogrenciprogramlama_kayit():
    ogrenci_adi = input("Öğrenci adı : ")
    ogrenci_soyadi = input("Ögrenci soyadı : ")
    ogrenci_bolumu = input("Öğreci bölümü : ")
    ogrenci_sinif = input("Öğrencinin sınıfı : ")

    yeniAd_sorgu = "SELECT DISTINCT isim FROM ogrenci_tablosu WHERE isim='" + ogrenci_adi + "'"
    imlec.execute(yeniAd_sorgu)
    yeniAd = imlec.fetchall()
    yeniSoyad_sorgu = "SELECT DISTINCT soyisim FROM ogrenci_tablosu WHERE soyisim='" + ogrenci_soyadi + "'"
    imlec.execute(yeniSoyad_sorgu)
    yeniSoyad = imlec.fetchall()
    yenibolum_sorgu = "SELECT DISTINCT bolum FROM ogrenci_tablosu WHERE bolum='" + ogrenci_bolumu + "'"
    imlec.execute(yenibolum_sorgu)
    yenibolum = imlec.fetchall()
    yenisinif_sorgu = "SELECT DISTINCT sinif FROM ogrenci_tablosu WHERE sinif='" + ogrenci_sinif + "'"
    imlec.execute(yenisinif_sorgu)
    yenisinif = imlec.fetchall()

    if (len(yeniAd) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yeniSoyad) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yenibolum) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yenisinif) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    else:
        print(" Kişi okulda kayıtlı.")

    yeniAdi_sorgu = "SELECT DISTINCT isim FROM ogrenciprogramlama_tablosu WHERE isim='" + ogrenci_adi + "'"
    imlec.execute(yeniAdi_sorgu)
    yeniAdi = imlec.fetchall()
    yeniSoyadi_sorgu = "SELECT DISTINCT soyisim FROM ogrenciprogramlama_tablosu WHERE soyisim='" + ogrenci_soyadi + "'"
    imlec.execute(yeniSoyadi_sorgu)
    yeniSoyadi = imlec.fetchall()
    yenibolumu_sorgu = "SELECT DISTINCT  bolum FROM ogrenciprogramlama_tablosu WHERE bolum='" + ogrenci_bolumu + "'"
    imlec.execute(yenibolumu_sorgu)
    yenibolumu = imlec.fetchall()
    yenisinifi_sorgu = "SELECT DISTINCT sinif FROM ogrenciprogramlama_tablosu WHERE sinif='" + ogrenci_sinif + "'"
    imlec.execute(yenisinifi_sorgu)
    yenisinifi = imlec.fetchall()

    if (len(yeniAdi) == 0):
        imlec.execute("INSERT INTO ogrenciprogramlama_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yeniSoyadi) == 0):
        imlec.execute("INSERT INTO ogrenciprogramlama_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenibolumu) == 0):
        imlec.execute("INSERT INTO ogrenciprogramlama_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenisinifi) == 0):
        imlec.execute("INSERT INTO ogrenciprogramlama_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    else:
        print(" kisi mevcut")

def ogrencibsmgiris_kayit():
    ogrenci_adi = input("Öğrenci adı : ")
    ogrenci_soyadi = input("Ögrenci soyadı : ")
    ogrenci_bolumu = input("Öğreci bölümü : ")
    ogrenci_sinif = input("Öğrencinin sınıfı : ")

    yeniAd_sorgu = "SELECT DISTINCT isim FROM ogrenci_tablosu WHERE isim='" + ogrenci_adi + "'"
    imlec.execute(yeniAd_sorgu)
    yeniAd = imlec.fetchall()
    yeniSoyad_sorgu = "SELECT DISTINCT soyisim FROM ogrenci_tablosu WHERE soyisim='" + ogrenci_soyadi + "'"
    imlec.execute(yeniSoyad_sorgu)
    yeniSoyad = imlec.fetchall()
    yenibolum_sorgu = "SELECT DISTINCT bolum FROM ogrenci_tablosu WHERE bolum='" + ogrenci_bolumu + "'"
    imlec.execute(yenibolum_sorgu)
    yenibolum = imlec.fetchall()
    yenisinif_sorgu = "SELECT DISTINCT sinif FROM ogrenci_tablosu WHERE sinif='" + ogrenci_sinif + "'"
    imlec.execute(yenisinif_sorgu)
    yenisinif = imlec.fetchall()

    if (len(yeniAd) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yeniSoyad) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yenibolum) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    elif (len(yenisinif) == 0):
        imlec.execute("INSERT INTO ogrenci_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ ÜNİVERSİTEYE KAYIT EDİLDİ.")

    else:
        print(" Kişi okulda kayıtlı.")

    yeniAdi_sorgu = "SELECT DISTINCT isim FROM ogrencibsmgiris_tablosu WHERE isim='" + ogrenci_adi + "'"
    imlec.execute(yeniAdi_sorgu)
    yeniAdi = imlec.fetchall()
    yeniSoyadi_sorgu = "SELECT DISTINCT soyisim FROM ogrencibsmgiris_tablosu WHERE soyisim='" + ogrenci_soyadi + "'"
    imlec.execute(yeniSoyadi_sorgu)
    yeniSoyadi = imlec.fetchall()
    yenibolumu_sorgu = "SELECT DISTINCT  bolum FROM ogrencibsmgiris_tablosu WHERE bolum='" + ogrenci_bolumu + "'"
    imlec.execute(yenibolumu_sorgu)
    yenibolumu = imlec.fetchall()
    yenisinifi_sorgu = "SELECT DISTINCT sinif FROM ogrencibsmgiris_tablosu WHERE sinif='" + ogrenci_sinif + "'"
    imlec.execute(yenisinifi_sorgu)
    yenisinifi = imlec.fetchall()

    if (len(yeniAdi) == 0):
        imlec.execute("INSERT INTO ogrencibsmgiris_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yeniSoyadi) == 0):
        imlec.execute("INSERT INTO ogrencibsmgiris_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenibolumu) == 0):
        imlec.execute("INSERT INTO ogrencibsmgiris_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    elif (len(yenisinifi) == 0):
        imlec.execute("INSERT INTO ogrencibsmgiris_tablosu (isim,soyisim,bolum,sinif) VALUES ('" + ogrenci_adi + "','" + ogrenci_soyadi + "','" + ogrenci_bolumu + "','" + ogrenci_sinif + "')")
        vt.commit()
        print("ÖĞRENCİ MATEMATİK DERSİNE KAYIT EDİLDİ.")

    else:
        print(" kisi mevcut")

def ogrenci_sil():
    silinecek_id = input("KAYDI SİLİNECEK ÖĞRENCİNİN İD NO : ")
    imlec.execute("DELETE FROM ogrenci_tablosu WHERE ogrenci_id = '" + silinecek_id + "'")
    vt.commit()

def ogrencilerimat_listele():
    imlec.execute("SELECT * FROM ogrencimat_tablosu")
    liste = imlec.fetchall()

    for i in liste:
        for k in i:
            print(k, end=" ")
        print("")

def ogrencilerifizik_listele():
    imlec.execute("SELECT * FROM ogrencifizik_tablosu")
    liste = imlec.fetchall()

    for i in liste:
        for k in i:
            print(k, end=" ")
        print("")

def ogrencileribilisim_listele():
    imlec.execute("SELECT * FROM ogrencibilisim_tablosu")
    liste = imlec.fetchall()

    for i in liste:
        for k in i:
            print(k, end=" ")
        print("")

def ogrencileriprogramlama_listele():
    imlec.execute("SELECT * FROM ogrenciprogramlama_tablosu")
    liste = imlec.fetchall()

    for i in liste:
        for k in i:
            print(k, end=" ")
        print("")

def ogrencileribsmgiris_listele():
    imlec.execute("SELECT * FROM ogrencibsmgiris_tablosu")
    liste = imlec.fetchall()

    for i in liste:
        for k in i:
            print(k, end=" ")
        print("")

def ogretmen_kayit():
    ogretmen_adi = input("Öğretmen adı : ")
    ogretmen_soyadi = input("Öğretmen soyadı : ")
    ogretmen_bolumu = input("Öğretmenin bölümü : ")
    ogretmen_unvan = input("Öğretmenin ünvanı : ")
    ogretmen_ekle = "INSERT INTO ogretmen_tablosu(ad,soyadi,bolumu,unvan) VALUES ('" + ogretmen_adi + "','" + ogretmen_soyadi + "','" + ogretmen_bolumu + "','" + ogretmen_unvan + "')"
    imlec.execute(ogretmen_ekle)
    vt.commit()

def ogretmen_sil():
    silinecek_id = input("Kaydı silinecek öğretmen id no : ")
    imlec.execute("DELETE FROM ogretmen_tablosu WHERE ogretmen_id ='" + silinecek_id + "'")
    vt.commit()

def ogretmenleri_listele():
    imlec.execute("SELECT * FROM ogretmen_tablosu")
    liste = imlec.fetchall()

    for i in liste:
        for k in i:
            print(k, end=" ")
        print("")

def ogretmenmat_not_girisi():

    ogrenci_id = input("Not girmek istediğiniz öğrenci id : ")
    vize = input("Vize notu : ")
    kisa1 = input("Kısa 1 : ")
    kisa2 = input("Kısa 2 : ")
    odev = input("Ödev : ")
    final = input("Final : ")
    #ort = float(vize*35/100+kisa1*5/100+kisa2*5/100+odev*5/100+final*50/100)
    #print(ort)
    imlec.execute("UPDATE ogrencimat_tablosu SET (vize,kisasinav1,kisasinav2,odev,final) = ('"+vize+"','"+kisa1+"','"+kisa2+"','"+odev+"','"+final+"') WHERE ogrenci_id = '"+ogrenci_id+"'")
    vt.commit()

def ogretmenfizik_not_girisi():
    ogrencilerifizik_listele()
    ogrenci_id = input("Not girmek istediğiniz öğrenci id : ")
    vize = input("Vize notu : ")
    kisa1 = input("Kısa 1 : ")
    kisa2 = input("Kısa 2 : ")
    odev = input("Ödev : ")
    final = input("Final : ")
    imlec.execute("UPDATE ogrencifizik_tablosu SET (vize,kisasinav1,kisasinav2,odev,final) = ('"+vize+"','"+kisa1+"','"+kisa2+"','"+odev+"','"+final+"') WHERE ogrenci_id = '"+ogrenci_id+"'")
    vt.commit()

def ogretmenbilisim_not_girisi():
    ogrencileribilisim_listele()
    ogrenci_id = input("Not girmek istediğiniz öğrenci id : ")
    vize = input("Vize notu : ")
    kisa1 = input("Kısa 1 : ")
    kisa2 = input("Kısa 2 : ")
    odev = input("Ödev : ")
    final = input("Final : ")
    imlec.execute("UPDATE ogrencibilisim_tablosu SET (vize,kisasinav1,kisasinav2,odev,final) = ('" + vize + "','" + kisa1 + "','" + kisa2 + "','" + odev + "','" + final + "') WHERE ogrenci_id = '" + ogrenci_id + "'")
    vt.commit()

def ogretmenprogramlama_not_girisi():
    ogrencileriprogramlama_listele()
    ogrenci_id = input("Not girmek istediğiniz öğrenci id : ")
    vize = input("Vize notu : ")
    odev1 = input("1. Ödev notu : ")
    odev2 = input("2. Ödev notu : ")
    odev3 = input("3. Ödev notu : ")
    odev4 = input("4. Ödev notu : ")
    odev5 = input("5. Ödev notu : ")
    odev6 = input("6. Ödev notu : ")
    final = input("Final : ")
    imlec.execute("UPDATE ogrenciprogramlama_tablosu SET (vize,odev1,odev2,odev3,odev4,odev5,odev6,final) = ('"+vize+"','"+odev1+"','"+odev2+"','"+odev3+"','"+odev4+"','"+odev5+"','"+odev6+"','"+final+"') WHERE ogrenci_id = '"+ogrenci_id+"'")
    vt.commit()

def ogretmenbsmgiris_not_girisi():
    ogrencileribsmgiris_listele()
    ogrenci_id = input("Not girmek istediğiniz öğrenci id : ")
    vize = input("Vize notu : ")
    kisa1 = input("Kısa 1 : ")
    kisa2 = input("Kısa 2 : ")
    final = input("Final : ")
    imlec.execute("UPDATE ogrencibsmgiris_tablosu SET (vize,kisasinav1,kisasinav2,final) = ('" + vize + "','" + kisa1 + "','" + kisa2 + "','" + final + "') WHERE ogrenci_id = '" + ogrenci_id + "'")
    vt.commit()

while True:

    print("")
    print("SİSTEME HOŞGELDİNİZ..")
    print("")
    print("""
    ÖZEL ASEL ÜNİVERSİTESİ
    BİLİŞİM SİSTEMLERİ MÜHENDİSLİĞİ BÖLÜMÜ
    
    1 - ÖĞRETMEN
    2 - GÖREVLİ
    3 - ÖĞRENCİ
    q - ÇIKIŞ
    
    """)

    tercih = input("Lütfen kullanıcı tipinizi seçiniz : ")

    if(tercih == "1"):
        ograd = input("Merhaba Hocam, Lütfen adınızı giriniz :  ")
        print("")
        print("HOŞGELDİNİZ {} HOCAM".format(ograd))

        while True:

            print("-------------")
            print("""
            1 - MATEMATİK
            2 - FİZİK 
            3 - BİLİŞİM VE İLETİŞİM TEKNOLOJİLERİ
            4 - PROGRAMLAMAYA GİRİŞ
            5 - BİLİŞİM SİSTEMLERİ MÜHENDİSLİĞİNE GİRİŞ
            6 - KÜTÜPHANE
            7 - ASEL ÜNİVERSİTESİ HAKKINDA
            q - ÜST MENÜ 
            """)
            derssecimi = input("Lütfen dersinizi seçiniz : ")

            if(derssecimi == "1"):
                print("")
                print("""
                
                1 - NOT GİR 
                2 - NOT GÜNCELLE
                3 - ÖGRENCİLERİ LİSTELE
                4 - DERS PROGRAMIMI LİSTELE
                q - ÜST MENÜ
                """)
                issecimi = input("Yapmak istediğiniz işlemi seçiniz : ")
                print("")
                print("İşleminiz yapılıyor...")
                time.sleep(1)

                if(issecimi == "1"):
                    ogrencilerimat_listele()
                    print("--------------------")
                    print("")
                    ogretmenmat_not_girisi()
                    print("Not girişi başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif(issecimi == "2"):
                    ogrencilerimat_listele()
                    print("---------------------")
                    print("")
                    ogretmenmat_not_girisi()
                    print("Not güncelleme başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif(issecimi == "3"):
                    print("")
                    ogrencilerimat_listele()

                elif(issecimi == "q" or issecimi == "Q"):
                    print("")
                    print("VERİLER KAYDEDİLİYOR...")
                    time.sleep(1)
                    print("")
                    print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                    break

                else:
                    print("")
                    print("GEÇERSİZ İŞLEM GİRDİNİZ...")

            elif(derssecimi == "2"):
                print("")
                print("""
        
                1 - NOT GİR 
                2 - NOT GÜNCELLE
                3 - ÖGRENCİLERİ LİSTELE
                4 - DERS PROGRAMIMI LİSTELE
                q - ÜST MENÜ
                
                """)
                issecimi = input("Yapmak istediğiniz işlemi seçiniz : ")
                print("")
                print("işleminiz yapılıyor...")
                print("")
                time.sleep(1)

                if (issecimi == "1"):
                    ogrencilerifizik_listele()
                    print("--------------------")
                    print("")
                    ogretmenfizik_not_girisi()
                    print("Not girişi başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif (issecimi == "2"):
                    ogrencilerifizik_listele()
                    print("---------------------")
                    print("")
                    ogretmenfizik_not_girisi()
                    print("Not güncelleme başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif (issecimi == "3"):
                    print("")
                    ogrencilerifizik_listele()

                elif(issecimi == "q" or issecimi == "Q"):
                    print("")
                    print("VERİLER KAYDEDİLİYOR...")
                    time.sleep(1)
                    print("")
                    print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                    break

                else:
                    print("")
                    print("GEÇERSİZ İŞLEM GİRDİNİZ...")

            elif(derssecimi == "3"):
                print("")
                print("""
        
                1 - NOT GİR 
                2 - NOT GÜNCELLE
                3 - ÖGRENCİLERİ LİSTELE
                4 - DERS PROGRAMIMI LİSTELE
                q - ÜST MENÜ
                
                """)
                print("")
                issecimi = input("Yapmak istediğiniz işlemi seçiniz : ")
                print("")
                print("İşleminiz yapılıyor...")
                time.sleep(1)

                if (issecimi == "1"):
                    ogrencileribilisim_listele()
                    print("--------------------")
                    print("")
                    ogretmenbilisim_not_girisi()
                    print("Not girişi başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif (issecimi == "2"):
                    ogrencileribilisim_listele()
                    print("---------------------")
                    print("")
                    ogretmenbilisim_not_girisi()
                    print("Not güncelleme başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif (issecimi == "3"):
                    print("")
                    ogrencileribilisim_listele()

                elif(issecimi == "q" or issecimi == "Q"):
                    print("")
                    print("VERİLER KAYDEDİLİYOR...")
                    time.sleep(1)
                    print("")
                    print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                    break

                else:
                    print("")
                    print("GEÇERSİZ İŞLEM GİRDİNİZ...")

            elif(derssecimi == "4"):
                print("""
        
                1 - NOT GİR 
                2 - NOT GÜNCELLE
                3 - ÖGRENCİLERİ LİSTELE
                4 - DERS PROGRAMIMI LİSTELE
        
                """)
                print("")
                issecimi = input("Yapmak istediğiniz işlemi seçiniz : ")
                print("")
                print("İşleminiz yapılıyor...")
                time.sleep(1)

                if (issecimi == "1"):
                    ogrencileriprogramlama_listele()
                    print("--------------------")
                    print("")
                    ogretmenprogramlama_not_girisi()
                    print("Not girişi başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif (issecimi == "2"):
                    ogrencileriprogramlama_listele()
                    print("---------------------")
                    print("")
                    ogretmenprogramlama_not_girisi()
                    print("Not güncelleme başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif (issecimi == "3"):
                    print("")
                    ogrencileriprogramlama_listele()

                elif (issecimi == "q" or issecimi == "Q"):
                    print("")
                    print("VERİLER KAYDEDİLİYOR...")
                    time.sleep(1)
                    print("")
                    print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                    break

                else:
                    print("")
                    print("GEÇERSİZ İŞLEM GİRDİNİZ...")

            elif(derssecimi == "5"):
                print("""
        
                1 - NOT GİR 
                2 - NOT GÜNCELLE
                3 - ÖGRENCİLERİ LİSTELE
                4 - DERS PROGRAMIMI LİSTELE
                q - ÜST MENÜ
                
                """)
                issecimi = input("Yapmak istediğiniz işlemi seçiniz : ")
                print("")
                print("İşleminiz yapılıyor...")
                time.sleep(1)

                if (issecimi == "1"):
                    print("")
                    ogrencileribsmgiris_listele()
                    print("--------------------")
                    print("")
                    ogretmenbsmgiris_not_girisi()
                    print("Not girişi başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif (issecimi == "2"):
                    print("")
                    ogrencileribsmgiris_listele()
                    print("---------------------")
                    print("")
                    ogretmenbsmgiris_not_girisi()
                    print("Not güncelleme başarıyla gerçekleşti...")
                    time.sleep(0.5)

                elif (issecimi == "3"):
                    print("")
                    ogrencileribsmgiris_listele()

                elif (issecimi == "q" or issecimi == "Q"):
                    print("")
                    print("VERİLER KAYDEDİLİYOR...")
                    time.sleep(1)
                    print("")
                    print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                    break

                else:
                    print("")
                    print("GEÇERSİZ İŞLEM GİRDİNİZ...")

            elif (derssecimi == "6"):
                print("""
                
                ASEL ÜNİVERSİTESİ KÜTÜPHANESİ
                
                KİTAPLAR LİSTELENİYOR...
                
                """)
                time.sleep(1)

                kitap_listele()
                print("")

            elif(derssecimi == "7"):
                print("")
                asel_bilgi_iletişim()
                print("")

            elif(derssecimi == "q" or derssecimi == "Q"):
                print("")
                print("VERİLER KAYDEDİLİYOR...")
                print("")
                time.sleep(1)
                print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                print("")
                break

            else:
                print("")
                print("GEÇERSİZ İŞLEM GİRDİNİZ...")

    elif(tercih == "2"):
        print("")
        grv = input("Merhaba Hocam, Lütfen adınızı giriniz :  ")
        print("")
        print("HOŞGELDİNİZ {} HOCAM".format(grv))
        print("")

        while True:

            print("")
            print("""
            
            1 - ÖĞRETMEN İŞLEMLERİ 
            2 - ÖĞRENCİ İŞLEMLERİ 
            3 - KÜTÜPHANE İŞLEMLERİ
            4 - ASEL ÜNİVERSİTESİ HAKKINDA
            q - ÜST MENÜ
            
            """)
            gorev = input("Yapmak istediğiniz işlemi seçiniz : ")

            if(gorev == "1"):
                while True:
                    print("""
                    
                    1 - ÖĞRETMEN KAYIT
                    2 - ÖĞRETMEN KAYDI SİL
                    3 - ÖĞRETMENLERİ LİSTELE
                    q - ÜST MENÜ 
                    
                    """)
                    yanıt = input("Yapmak istediğiniz işlem : ")

                    if(yanıt == "1"):
                        print("")
                        ogretmen_kayit()

                    elif(yanıt == "2"):
                        print("")
                        ogretmen_sil()

                    elif(yanıt == "3"):
                        print("")
                        ogretmenleri_listele()

                    elif(yanıt == "q" or yanıt == "Q"):
                        print("")
                        print("VERİLER KAYDEDİLİYOR...")
                        time.sleep(1)
                        print("")
                        print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                        print("")
                        break

                    else:
                        print("GEÇERSİZ İŞLEM GİRDİNİZ...")

            elif(gorev == "2"):
                while True:
                    print("""       
                    1 - ÖĞRENCİ KAYIT 
                    2 - ÖĞRENCİ KAYDI SİL
                    3 - ÖĞRENCİLERİ LİSTELE         
                    q - ÜST MENÜ
                    
                    """)
                    yanıt = input("Yapmak istediğiniz işlem : ")
                    print("İşleminiz yapılıyor...")
                    print("")
                    time.sleep(1)

                    if(yanıt == "1"):
                        while True:
                            print("""
                            DERS SEÇİMİ
                            
                            1 - MATEMATİK KAYDI
                            2 - FİZİK KAYDI
                            3 - BİLİŞİM VE İLETİŞİM TEKNOLOJİLERİ KAYDI
                            4 - PROGRAMLAMAYA GİRİŞ KAYDI
                            5 - BİLİŞİM SİSTEMLERİ MÜHENDİSLİĞİNE GİRİŞ KAYDI
                            q - ÜST MENÜ
                                       
                            """)
                            ders = input("Öğrenciyi kayıt etmek istediğiniz ders : ")

                            if(ders == "1"):
                                print("")
                                ogrencimat_kayit()

                            elif(ders == "2"):
                                print("")
                                ogrencifizik_kayit()

                            elif(ders == "3"):
                                print("")
                                ogrencibilisim_kayit()

                            elif(ders == "4"):
                                print("")
                                ogrenciprogramlama_kayit()

                            elif(ders == "5"):
                                print("")
                                ogrencibsmgiris_kayit()

                            elif(ders == "q" or ders == "Q"):
                                print("")
                                print("VERİLER KAYDEDİLİYOR...")
                                print("")
                                time.sleep(1)
                                print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                                print("")
                                break

                            else:
                                print("")
                                print("GEÇERSİZ İŞLEM GİRDİNİZ...")
                                print("")

                    elif(yanıt == "2"):
                        while True:
                            print("""
                            DERSLER
                
                            1 - MATEMATİK 
                            2 - FİZİK 
                            3 - BİLİŞİM VE İLETİŞİM TEKNOLOJİLERİ 
                            4 - PROGRAMLAMAYA GİRİŞ 
                            5 - BİLİŞİM SİSTEMLERİ MÜHENDİSLİĞİNE GİRİŞ 
                            q - ÜST MENÜ
                            
                            """)
                            ders = input("Kaydını silmek istediğiniz öğrencinin dersini seçiniz : ")
                            print("İşleminiz yapılıyor...")
                            time.sleep(1)

                            if(ders == "1"):
                                ogrencilerimat_listele()
                                ogrenci_sil()

                            elif(ders == "2"):
                                ogrencilerifizik_listele()
                                ogrenci_sil()

                            elif(ders == "3"):
                                ogrencileribilisim_listele()
                                ogrenci_sil()

                            elif(ders == "4"):
                                ogrencileriprogramlama_listele()
                                ogrenci_sil()

                            elif(ders == "5"):
                                ogrencileribsmgiris_listele()
                                ogrenci_sil()

                            elif(ders == "q" or ders == "Q"):
                                print("")
                                print("VERİLER KAYDEDİLİYOR...")
                                time.sleep(1)
                                print("")
                                print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                                break

                            else:
                                print("")
                                print("GEÇERSİZ İŞLEM GİRDİNİZ...")
                                print("")

                    elif(yanıt == "3"):
                        while True:
                            print("""
                            1 - MATEMATİK DERSİ ÖĞRENCİLERİ 
                            2 - FİZİK DERSİ ÖĞRENCİLERİ
                            3 - BİLİŞİM VE İLETİŞİM TEKNOLOJİLERİ DERSİ ÖĞRENCİLERİ
                            4 - PROGRAMLAMAYA GİRİŞ DERSİ ÖĞRENCİLERİ 
                            5 - BİLİŞİM SİSTEMLERİNE GİRİŞ DERSİ ÖĞRENCİLERİ
                            q - ÜST MENÜ
                            
                            """)
                            ders = input("Listelemek istediğiniz dersi seçiniz : ")

                            print("İşleminiz yapılıyor...")
                            print("")
                            time.sleep(1)

                            if(ders == "1"):
                                print("")
                                ogrencilerimat_listele()

                            elif(ders == "2"):
                                print("")
                                ogrencilerifizik_listele()

                            elif(ders == "3"):
                                print("")
                                ogrencileribilisim_listele()

                            elif(ders == "4"):
                                print("")
                                ogrencileriprogramlama_listele()

                            elif(ders == "5"):
                                print("")
                                ogrencileribsmgiris_listele()

                            elif(ders == "q" or ders == "Q"):
                                print("")
                                print("VERİLER KAYDEDİLİYOR...")
                                print("")
                                time.sleep(1)
                                print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                                print("")
                                break

                            else:
                                print("")
                                print("GEÇERSİZ İŞLEM GİRDİNİZ...")
                                print("")

                    elif(yanıt == "q" or yanıt == "Q"):
                        print("")
                        print("VERİLER KAYDEDİLİYOR...")
                        print("")
                        time.sleep(1)
                        print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                        print("")
                        break

                    else:
                        print("")
                        print("GEÇERSİZ İŞLEM GİRDİNİZ...")
                        print("")


            elif(gorev == "3"):
                while True:
                    print("""
                    
                    1 - KİTAP KAYIT
                    2 - KİTAP SİL
                    3 - KİTAPLARI LİSTELE
                    4 - KİTAP DURUMUNU GÜNCELLE
                    q - ÜST MENÜ
                    
                    """)
                    kitapsec = input("YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ : ")
                    print("")

                    if(kitapsec == "1"):
                        print("")
                        kitap_listele()
                        print("-------------")
                        kitap_ekle()

                    elif(kitapsec == "2"):
                        print("")
                        kitap_listele()
                        print("-------------")
                        kitap_sil()

                    elif(kitapsec == "3"):
                        print("")
                        kitap_listele()

                    elif(kitapsec == "4"):
                        print("")
                        kitap_listele()
                        print("-------------")
                        print("")
                        kitap_guncelle_durum()

                    elif(kitapsec == "q" or kitapsec == "Q"):
                        print("")
                        print("Üst menüye geçiliyor..")
                        print("")
                        time.sleep(1)
                        break

            elif (gorev == "4"):
                print("")
                asel_bilgi_iletişim()
                print("")

            elif (gorev == "q" or gorev == "Q"):
                print("")
                print("VERİLER KAYDEDİLİYOR...")
                print("")
                time.sleep(1)
                print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                break

            else:
                print("GEÇERSİZ İŞLEM GİRDİNİZ...")
                print("")

    elif (tercih == "3"):
        while True:
            print("""
            
            1 - KÜTÜPHANE 
            2 - ASEL ÜNİVERSİTESİ HAKKINDA
            q - ÜST MENÜ
            
            """)

            ogr = input("İŞLEMİNİZİ SEÇİNİZ : ")

            if (ogr == "1"):
                print("""
        
                ASEL ÜNİVERSİTESİ KÜTÜPHANESİ
        
                KİTAPLAR LİSTELENİYOR...
                """)
                time.sleep(1)
                kitap_listele()
                print("")

            elif (ogr == "2"):
                print("")
                asel_bilgi_iletişim()
                print("")

            elif (ogr == "q" or ogr == "Q"):
                print("")
                print("VERİLER KAYDEDİLİYOR...")
                print("")
                time.sleep(1)
                print("BAŞARIYLA ÇIKIŞ YAPILDI...")
                break

            else:
                print("GEÇERSİZ İŞLEM...")
                time.sleep(1)

    elif(tercih == "q" or tercih == "Q"):
        print("VERİLER KAYDEDİLİYOR...")
        time.sleep(1)
        print("BAŞARIYLA ÇIKIŞ YAPILDI...")
        break

    else:
        print("GEÇERSİZ İŞLEM GİRDİNİZ...")
        time.sleep(1)
