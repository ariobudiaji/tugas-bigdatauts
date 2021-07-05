Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class biodata():
    def __init__(saya,bangga,jadi,warga,nahdatul,ulama):
 
        print "saya bangga jadi warga nahdatul ulama:"
 
    def input(self):
        self.saya = raw_input("saya           ")
        self.bangga = raw_input("bangga        ")
        self.jadi = raw_input("jadi      ")
        self.warga = raw_input("warga      ")
        self.nahdatul = raw_input("nahdatul       ")
        self.julama = raw_input("ulama       ")

class mahasiswa(biodata):
    def cetak(self):
        print "saya bangga jadi warga nahdatul ulama:"
        print "saya:            ",self.saya
        print "bangga:             ",bangga
        print "jadi:          ",self.jadi
        print "warga:          ",self.warga
        print "nahdatul:          ",self.nahdatul
        print "ulama:          ",self.ulama
 
dataMhs = mahasiswa("saya","bangga","jadi","warga","nahdatul","ulama")
dataMhs.input()
dataMhs.cetak()
