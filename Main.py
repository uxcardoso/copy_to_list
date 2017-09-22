import MainWindow
import sys
import os
import shutil
from PyQt5 import QtWidgets


class meuApp(QtWidgets.QMainWindow, MainWindow.Ui_Dialog):

    def __init__(self, parent=None):
        super(meuApp, self).__init__(parent)
        self.setupUi(self)

        self.btn_directory_txt.clicked.connect(self.browser_file)
        self.btn_directory_final.clicked.connect(self.browser_directory)
        self.btn_sair.clicked.connect(lambda: self.close())
        self.btn_copiar.clicked.connect(self.copy_txt)


    def browser_directory(self):
        self.save_dir = QtWidgets.QFileDialog.getExistingDirectory(self, None, 'Escolha o diretório')
        self.directory_replace = self.save_dir.replace('/', '\\')
        self.txt_directory_final.setText(self.directory_replace)



    def browser_file(self):
        self.save_dir = QtWidgets.QFileDialog.getOpenFileName(self, 'Escolha o arquivo txt', None, 'txt files: *.txt')
        self.txt_directory_txt.setText(str(self.save_dir[0]))

    def copy_txt(self):

        try:
            file = open(self.txt_directory_txt.text(), 'r')
            os.mkdir(self.txt_directory_final.text() + '\\copy')
            lista = file

            with open(self.txt_directory_txt.text()) as f:
                referencia = len(f.readlines())
            contador = 100 / referencia
            print(contador)
            for f in file:
                print(f.replace('\n', ''))

                self.file = self.txt_directory_final.text() + '\\' + f.replace('\n', '')
                self.dir = self.txt_directory_final.text() + '\\copy'

                try:
                    shutil.copy(self.file, self.dir)
                    self.progressBar.setValue(contador)
                    contador += 100 / referencia
                    if self.progressBar.value() == 100:
                        sucess = QtWidgets.QMessageBox.about(self, 'Sucesso ', 'Arquivos copiados!')
                except:
                    error = QtWidgets.QMessageBox.warning(self, 'Erro ao copiar ' + self.file)
        except:
            error = QtWidgets.QMessageBox.warning(self, 'ERROR', 'Algo deu errado!')






def main():
    app = QtWidgets.QApplication(sys.argv)
    form = meuApp()
    form.show()

    app.exec_()

if __name__ == '__main__':
    main()