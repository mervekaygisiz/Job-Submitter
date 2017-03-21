import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
from PyQt5.QtGui import *
import subprocess





#btn5, btn6, bt7 icin mouse uzerine geldiginde renk degisimi saglayip gorsellik katmak icin yeni bir sinif olusturuldu HoverButton adinda
class HoverButton(QToolButton):

    def __init__(self, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setMouseTracking(True)

    def enterEvent(self,event): # mouse ile butonun uzerine geldigimizde olacaklar bir fonksiyon icerisine alindi ve icine style ozellikleri girildi
        self.setStyleSheet("background-color:lightgrey; color:rgb(0,197,158); border: 1px solid lightgrey; font-size:15px;")

    def leaveEvent(self,event): # mouse uzerinden ayrildiginda butonun ozelliklerinin ayni kalmasi icin style'a ozellikler verildi.
        #  bu ozellikler btn5,bt6,btn7 ile aynidirlar, boylece eski halleriyle ayni duruma gelmektedirler
        self.setStyleSheet("background-color:white; color:rgb(0,197,158); border: 1px solid lightgrey; font-size:15px;")



class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):


        self.setStyleSheet("background-color: white;")
        #os.makedirs('new_jobs2', exist_ok=True)  # new_jobs adinda yeni bir package oluturduk

        self.btn1 = QPushButton('Clear', self) #buton olusturuldu
        self.btn1.setGeometry(1000, 590,140,40) #butonun yeri ve buyuklugu belirlendi
        self.btn1.setStyleSheet("background-color: #A4A4A4; color:white") #butona renk verildi
        self.btn1.clicked.connect(self.clear)

        self.btn2 = QPushButton('Save', self)
        self.btn2.setGeometry(1130, 590,140,40)
        self.btn2.setStyleSheet("background-color: #0B0B61; color:white")
        self.btn2.clicked.connect(self.save)


        self.btn3 = QPushButton('Prepare Job File', self)
        self.btn3.setGeometry(1260, 590,140,40)
        self.btn3.setStyleSheet("background-color: #2E9AFE; color:white")
        self.btn3.clicked.connect(self.showDialog)


        self.btn4 = QPushButton('Submit', self)
        self.btn4.setGeometry(1000,630,400,50)
        self.btn4.setStyleSheet("background-color: #04B404; color:white")

        #input file butonu
        # buton HoverButton sınıfının adı ile oluşturulmuştur bu sayede sınıfın içerisindeki mouse event değişikliklerini yapabilmektedir
        #self.btn5 = HoverButton(self)
        #self.btn5.setText('Input File') #butona isim verildi
        #self.btn5.setGeometry(490,320,127,40)
        #self.btn5.setStyleSheet("background-color:white; color:rgb(0,197,158); border: 1px solid lightgrey; font-size:15px;")


        #output dir butonu
        # buton HoverButton sınıfının adı ile oluşturulmuştur bu sayede sınıfın içerisindeki mouse event değişikliklerini yapabilmektedir
        #self.btn6 = HoverButton(self)
        #self.btn6.setText('Output Dir.') #butona isim verildi
        #self.btn6.setGeometry(617, 320, 127, 40)
        #self.btn6.setStyleSheet("background-color:white; color:rgb(0,197,158);border: 1px solid lightgrey; font-size:15px;")

        #working dir butonu
        # buton HoverButton sınıfının adı ile oluşturulmuştur bu sayede sınıfın içerisindeki mouse event değişikliklerini yapabilmektedir
        #self.btn7 = HoverButton(self)
        #self.btn7.setText('Working Dir.') #butona isim verildi
        #self.btn7.setGeometry(744, 320, 126, 40)
        #self.btn7.setStyleSheet("background-color:white; color:rgb(0,197,158); border: 1px solid lightgrey; font-size:15px;")


        self.combo = QComboBox(self) #comboBox olusturuldu
        self.combo.addItem("abinit_mpi") #comboBox'in icine secenekler eklendi
        self.combo.addItem("fluent")
        self.combo.addItem("gromacs_mpi")
        self.combo.addItem("lammps_gnu")
        self.combo.addItem("mpi")
        self.combo.addItem("openfoam")
        self.combo.addItem("quantum_espresso_intel_openmpi")
        self.combo.addItem("starccm_plus")
        self.combo.addItem("starccm_plus_java")
        self.combo.addItem("vasp")
        self.combo.setStyleSheet("border:1px solid lightgrey; color:black; selection-background-color:rgb(0,197,158); background-color:rgb(248,248,248);") # renkleri ayarlandı

        self.combo2 = QComboBox(self)
        self.combo2.addItem("svr_test")
        self.combo2.setStyleSheet("border:1px solid lightgrey; color:black; selection-background-color:rgb(0,197,158); background-color:rgb(248,248,248);")

        self.combo3 = QComboBox(self)
        self.combo3.addItem("debug")
        self.combo3.setStyleSheet("border:1px solid lightgrey; color:black; selection-background-color:rgb(0,197,158); background-color:rgb(248,248,248);")


        label1=  QLabel("Job Name:", self)
        label2 = QLabel("Job Type:", self)
        label3 = QLabel("Cores:", self)
        label4 = QLabel("Task/Node:", self)
        label5 = QLabel("Acount:", self)
        label6 = QLabel("Partition:", self)
        label7 = QLabel("Std. Output Name:", self)
        label8 = QLabel("Std. Error Name:",self)
        label9 = QLabel("Output File Name:", self)
        label_add_par= QLabel("Additional Parameters:", self)

        #baslik olarak sirketin logosu ile beraber job submitter yazisi kullanildi
        baslik = QLabel(self)   #logo eklenen kısım


        label_work_dir= QLabel("Working Directory:", self)
        label_inp_file= QLabel("Input File:",self)
        label_out_dir= QLabel("Output Directory:",self)

        pixmap = QPixmap('job-image.png')   #sirketin logosunun disarsdan cekilerek koda baglantili hale getirilmesi
        baslik.setPixmap(pixmap)    #ilk olusturulan baslik adli labela bu komut ile fotograf eklenmistir


        label1.setGeometry(30, 140, 130, 40) #labellarin yeri ve boyutu belirlendi
        label2.setGeometry(30, 200, 130, 40)
        label3.setGeometry(30, 260, 130, 40)
        label4.setGeometry(30, 320, 130, 40)
        label5.setGeometry(30, 380, 130, 40)
        label6.setGeometry(30, 440, 130, 40)
        label7.setGeometry(30, 500, 130, 40)
        label8.setGeometry(30, 560, 130, 40)
        label9.setGeometry(30, 620, 130, 40)
        label_add_par.setGeometry(1000,543,150,40)
        baslik.setGeometry(0,0,3000,80) # logo icin ayrilan yer


        label_work_dir.setGeometry(490, 140,130,40)
        label_inp_file.setGeometry(490, 200,130,40)
        label_out_dir.setGeometry(490,260,130,40)



        self.combo.setGeometry(155,200,194,40)
        self.combo2.setGeometry(155,380,194,40)
        self.combo3.setGeometry(155,440,194,40)



        label1.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label2.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label3.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label4.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label5.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label6.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label7.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label8.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label9.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label_add_par.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        baslik.setStyleSheet( "background-color:rgb(0,197,158);")

        label_work_dir.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label_inp_file.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")
        label_out_dir.setStyleSheet("border:1px solid lightgrey; background-color:rgb(235,240,241); border-radius:3%;")

        self.textbox1=QLineEdit(self) #Girdi yapilacak satir olusturuldu
        self.textbox1.setMinimumSize(QSize(188,40)) #buyuklugu belirlendi
        self.textbox1.move(160, 140) #penceredeki yeri belirlendi


        self.textbox2 = QLineEdit(self)
        self.textbox2.setMinimumSize(QSize(188, 40))
        self.textbox2.move(160, 260)

        self.textbox3 = QLineEdit(self)
        self.textbox3.setMinimumSize(QSize(188, 40))
        self.textbox3.move(160, 320)

        self.textbox4 = QLineEdit(self)
        self.textbox4.setMinimumSize(QSize(188, 40))
        self.textbox4.move(160, 500)

        self.textbox5 = QLineEdit(self)
        self.textbox5.setMinimumSize(QSize(188, 40))
        self.textbox5.move(160, 560)

        self.textbox6 = QLineEdit(self)
        self.textbox6.setMinimumSize(QSize(188, 40))
        self.textbox6.move(160, 620)


        self.text_add_par = QLineEdit(self)
        self.text_add_par.setMinimumSize(QSize(250,40))
        self.text_add_par.move(1150,543)


        self.text_work_dir= QLineEdit(self)
        self.text_work_dir.setMinimumSize(QSize(250,40))
        self.text_work_dir.move(620,140)
        self.text_work_dir.setReadOnly(True)
        self.text_work_dir.setStyleSheet("background-color:rgb(235,240,241); border:1px solid lightgrey;")

        self.text_inp_file = QLineEdit(self)
        self.text_inp_file.setMinimumSize(QSize(250,40))
        self.text_inp_file.move(620,200)
        self.text_inp_file.setReadOnly(True)
        self.text_inp_file.setStyleSheet("background-color:rgb(235,240,241);border:1px solid lightgrey;")

        self.text_out_dir = QLineEdit(self)
        self.text_out_dir.setMinimumSize(QSize(250,40))
        self.text_out_dir.move(620,260)
        self.text_out_dir.setReadOnly(True)
        self.text_out_dir.setStyleSheet("background-color:rgb(235,240,241);border:1px solid lightgrey;")

        self.screen = QTextEdit(self)
        self.screen.setMinimumSize(QSize(400, 400)) #buyukluk ayarlandi
        self.screen.move(1000, 135) #sayfadaki yeri belirlendi
        self.screen.setReadOnly(True) #uzerine yazi yazilmasi engelendi
        self.screen.setStyleSheet('border-radius:3%; border: 2px solid lightgrey; background-color: rgb(235,240,241);')  #gorunus ayarlari yapildi

        self.screen_dir = QListWidget(self) #yeni bir ekran olusturuldu
        self.screen_dir.setMinimumSize(QSize(380,340)) #ekranin buyuklugu ayarlandi
        self.screen_dir.move(490, 320) #sayfadaki yeri belirlendi
        self.screen_dir.setStyleSheet('border-radius:3%; border: 2px solid lightgrey; selection-background-color:rgb(0,197,158); ')



        self.screen_dir.itemActivated.connect(self.listele) #secmeli olan dosyalari tikladigimizda yeni bir fonksiyona yonlendiriliyoruz



        process = subprocess.Popen('whoami', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True) #whoami ile kullanıcı ismi alındı
        stdout, stderr = process.communicate() #process çalistirildi
        stdout = stdout.decode('utf-8') #sondan ve bastan eklenen gereksiz karakterlerden kurtulmamizi sagliyor
        self.std = stdout[0:-1] #stdout degiskenin son karakteri olan boslugu kesiyor

        os.chdir('/Users/' + self.std ) #kullanici isminin oldugu bolgeye giris yapiliyor. Linux isletim sistemi olsaydi users yerine home kullanilacakti.

        self.text_inp_file.setText(os.getcwd())  #secilen dosyanin yeri lineEdite yaziliyor
        self.text_out_dir.setText(os.getcwd())
        self.text_work_dir.setText(os.getcwd())
        self.inputfile=os.getcwd()

        self.komutlar() #komutlar isimli fonksiyon calıstiriliyor


        self.move(5,50)
        self.setFixedSize(1440,800)
        self.setWindowTitle('Sanal Havuz')
        self.show()


    def listele(self, item): # secilen klasorun ismini kullanabilmek icin item parametresini almaktadir
        if item.text()[-1]=='/' or item.text() == '..': #tiklanan klasorun son karakteri '/' ise veya geri tusu kullanildiysa
            os.chdir(item.text()) #tiklanan secenegin icine gir
            self.text_out_dir.setText(os.getcwd()) #bilgisayarin bulundugu dosyanin yerini lineEditlere yaz
            self.text_work_dir.setText(os.getcwd())
            self.text_inp_file.setText(os.getcwd())
        else:
            self.text_inp_file.setText(os.getcwd() + '/' + item.text()) #eger bu ikisinden biri degil ise yeni bir klasore gecis yapilmasini sagla


        self.inputfile=self.text_inp_file.text() #input ve output file a yazilan bilgileri yeni degiskenlerde islenmek uzere tutuyoruz
        self.outputfile=self.text_out_dir.text()
        self.komutlar()  #komutlar isimli fonksiyon kullaniliyor



    def komutlar(self):


        command = 'ls -l ' + os.getcwd()  #bulunulan yerdeki dosya bilgilerini bize basinda klasor olup olmadıgını gosteren bilgilerle beraber verir
        process = subprocess.Popen(command, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        stdout, stderr = process.communicate() #subprocess calistirildi
        stdout = stdout.decode('utf-8') #decode edildi
        lines = stdout.splitlines() #erisilen belge bilgileri satirlar haline getirilerek birbirinden ayrildi
        lines = lines[1:] #dosyaların ilk satirinda bulunan 'total 0' yazisini kesiyoruz
        self.screen_dir.clear() #bi sonraki girişde bi önceki belgedeki bilgilerin kalmaması adina temizlik yapiliyor
        if os.getcwd().count('/') != 2: #ilk acilan kulanici isminin oldugu dosyalari gösteren bolgede degilsek geri donusun saglanmasi icin
            self.screen_dir.addItem('..') #ilk satira '..' girdisi eklendi boylece geri dönüs saglandi


        for line in lines: #bulunulan yerdeki dosyalarin icinde dolasiliyor
            ilk = line[0] #ilk degiskeninde dosyanın tipi tutuluyor, d ile basliyorsa klasor
            line = line.split() #line degiskeninde bulunan tüm bilgiler satir haline getirililyor
            a = line[8] #8.sütun a degiskenine esitleniyor cunku linedan sadece dosyanin isminin oldugu bilgiye erisilmek isteniyor
            i = 9

            while i < len(line): #9dan büyük olan tüm yazılar dosyanın ismini vermektedir
                a += ' '  #9. sütundan sonra boşluklu bir dosya ismi varsa her sütun arasına boşluk ekleniyor
                a += line[i] #sütundaki yazılar ekleniyor
                i += 1 #döngünün artışı yapılıyor

            if ilk == 'd': #eger belge bir klasorse sonuna bunu belirten bir '/' isareti koyuluyor
                self.screen_dir.addItem(a + '/')


            else: #klasör degilse sadece kendi adi ekleniyor
                self.screen_dir.addItem(a)


    def showDialog(self):


        self.job_name = self.textbox1.text()
        self.job_type = self.combo.currentText()
        self.cores = self.textbox2.text()
        self.task_node = self.textbox3.text()
        self.acount = self.combo2.currentText()
        self.partition = self.combo3.currentText()
        self.out_name = self.textbox4.text()
        self.err_name = self.textbox5.text()
        self.file_name = self.textbox6.text()
        self.add_par = self.text_add_par.text()


        temp = os.listdir(directory + '/jobs/')  # os.listdir fonksiyonu ile jobs package içindekileri tempe attık
        templates = []

        for i in temp:  # dosya isimlerini '.' dan sonrasını almamak koşulu ile templates dizisine attık
            if i[0] != '.':
                i = i.split(".")[0]  # noktaya kadar ilk elemanları aldık çünkü dosya ismi splitle 2 parçaya ayrıldı
                templates.append(i)  # ekleme işlemi tamamlanıyor




        self.new_data = ''
        self.job_type = self.job_type + '.job'



        if self.job_type in temp:
            new_job_type = directory + '/jobs/' + self.job_type  # job_type yeni dosya package oluşturulduğan kullanılacağı için farklı isimli bir değişkende tuttuk
            #print(new_job_type)
            data = open(new_job_type, 'r')

            self.new_data = data.read()
            data.close()


        if '$jobName' in self.new_data:
            self.new_data = self.new_data.replace('$jobName', self.job_name)

        if '$numCores' in self.new_data:
            self.new_data = self.new_data.replace('$numCores', str(self.cores))

        if '$inputFile' in self.new_data:
            self.new_data = self.new_data.replace('$inputFile', str(self.inputfile))

        if '$outputFile' in self.new_data:
            self.new_data=self.new_data.replace('$outputFile', str(self.file_name))

        if '$outputO' in self.new_data:
            self.new_data=self.new_data.replace('$outputO',str(self.out_name))

        if '$errorE' in self.new_data:
            self.new_data = self.new_data.replace('$errorE', str(self.err_name))

        if '$projectName' in self.new_data:
            self.new_data = self.new_data.replace('$projectName', str(self.acount))

        if '$queue' in self.new_data:
            self.new_data= self.new_data.replace('$queue', str(self.partition))

        if '$tasksPerNode' in self.new_data:
            self.new_data = self.new_data.replace('$tasksPerNode', str(self.task_node))



        self.new_data = self.new_data + ' ' + self.add_par

        self.screen.setText(str(self.new_data))

    def clear(self):  #ekranda doldrulmuş tüm lineEditler boşluğa eşitlenip temizlendi
        self.screen.setText(str(' '))
        self.textbox1.setText(str(' '))
        self.textbox2.setText(str(' '))
        self.textbox3.setText(str(' '))
        self.textbox4.setText(str(' '))
        self.textbox5.setText(str(' '))
        self.textbox6.setText(str(' '))

    def save(self):  #değişikliklerin yapıldığı new_data değişkeninde bulunan yeni text dosyasının hali başka bir dosya açılarak oraya kaydedilmelidir
        os.chdir(directory + '/new_jobs2/')  # yeni package içine girildi
        new_file = open(self.job_type, 'w')  # içinde girilen type cinsinde yeni bir file oluşturldu
        new_file.write(self.new_data) #yazılma işlemi gerçekleşti
        new_file.close() #dosya işlemleri kapatıldı

if __name__ == '__main__':
    directory = os.getcwd()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

