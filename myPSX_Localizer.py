import Metashape

class MyPSX_Localizer:

    menu_item_1=""
    menu_item_2=""
    menu_item_3=""
    menu_item_4=""
    menu_item_5=""
    menu_item_6=""
    about_msg=""
    emptyChunk_msg=""
    noComponents_msg=""
    finishedComp_msg=""
    finishedVideoImp_msg=""
    pathToVideo=""
    frameStepLbl=""
    startImportLbl=""
    stepS=["","","",""]
    startCompProc=""
    comProcLbl_1=""
    comProcLbl_2=""
    comProcLbl_3=""
    comProcLbl_Qual=""
    compProcUseNet=""
    compProcQaulItem=["","","","",""]
    compMarksOk=""

    def __init__(self):

        print("Current language: "+Metashape.app.settings.language)

        if (Metashape.app.settings.language=="ru"):
            self.menu_item_1=u"Пакетный импорт видео"
            self.menu_item_2=u"Показать ключи компонентов"
            self.menu_item_3=u"Пакетный обработчик компонентов"
            self.menu_item_4=u"- Об этом плагине -"
            self.menu_item_5=u"Полигональные Модели из всех Облаков Точек"
            self.menu_item_6=u"Полигональные Модели из всех Связывающих Точек"
            self.about_msg=("Этот плагин для Metasahpe 2.1.3 и pySide 2 разработан\n"+
                            "Карнаушенко Александром Дмитриевичем (scadl) в Ноябре 2024\n"+
                            "scad.luncher@gmail.com");
            self.emptyChunk_msg=("Не найдено ни одного комопонета в этом блоке!\n"+
                                 "Пожалуйста, попробуйте выравнять ваши снимки снова.")
            self.noComponents_msg=("Ни один из существующих компонентов не обаботан...\n"+
                                   "Запускаю маркировку компонетов номерами ключей\n"+
                                   "Убедитесь, что вы выставили правильный диапазон КЛЮЧЕЙ!")
            self.finishedComp_msg=("Обработка завершена!\n"+
                                  "Построено: {goodV}\n"+
                                  "Битые (пропущеные): {badV}")
            self.finishedVideoImp_msg="Все видео успешно импортированы"
            self.pathToVideo="Путь к папке с видео для импорта"
            self.frameStepLbl="Шаг импорта кадров"
            self.startImportLbl="Выполнить импорт"
            self.stepS=["Автоматически: Малый","Автоматически: Средний","Автоматически: Большой","Свой шаг:"]
            self.startCompProc="Запустить обработку:\n Cоздать Плотные Облака Точек"
            self.startCompProc2="Запустить обработку:\n Cоздать Текстурированые Модели"
            self.comProcLbl_1="Обработать комп. с КЛЮЧАМИ: "
            self.comProcLbl_2=" по "
            self.comProcLbl_Qual="Качество обработки: "
            self.compProcUseNet="Использовать сетвую обработку"
            self.compProcQaulItem=["Ульра","Высокое","Среднее","Низкое","Черновое"]
            self.compMarksOk="Ключи успешно добавлены к именам компонентов"
            
        else:
            self.menu_item_1=u"Batch Video Import"
            self.menu_item_2=u"Show Component keys"
            self.menu_item_3=u"Batch Component Processor"
            self.menu_item_4=u"- About this plugin -"
            self.menu_item_5=u"Meshes from all PointClouds"
            self.menu_item_6=u"Meshes from all Components"
            self.about_msg=("This plugin built for Metasahpe 2.1.3 and pySide 2 by\n"+
                            "Karnaushenko Alexander Dmitrievich (scadl) at November 2024\n"+
                            "scad.luncher@gmail.com");
            self.emptyChunk_msg=("No components in this chunk found!\n"+
                                 "Try to align you photos again.")
            self.noComponents_msg=("No components proceseed...\n"+
                                   "I\'ll run component key check for you\n"+
                                   "Make sure you set right KEYS in processing diapazone!")
            self.finishedComp_msg=("Processing done!\n"+
                                  "Succesfuly built: {goodV}\n"+
                                  "Broken elements: {badV}")
            self.finishedVideoImp_msg="All videos succesfully imported!"
            self.pathToVideo="Path to videos for import"
            self.frameStepLbl="Frame Step"
            self.startImportLbl="Start Import"
            self.stepS=["Automatic Small","Automatic Medium","Automatic Large","Custom Step"]
            self.startCompProc="Start building\n Dense Point Clouds"
            self.startCompProc2="Start building\n Textured Meshes"
            self.comProcLbl_1="Process comp. with keys: "
            self.comProcLbl_2=" to "
            self.comProcLbl_Qual="Processing quality: "
            self.compProcUseNet="Use network processing"
            self.compProcQaulItem=["Ultra high","High","Medium","Low","Lowest"]
            self.compMarksOk="Keys succesfully added to all compnent names"

