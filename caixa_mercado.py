from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QMessageBox
import sys 

class CaixaMercado(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. Setandos valores de posição X e Y,
        # além de largura e altura
        self.setGeometry(500,30,600,800)

        # Texto para a barra de título
        self.setWindowTitle("Caixa")

        #Layout vertical da tela inteira
        self.layout_v_total = QVBoxLayout()

        #Label titulo
        self.label_titulo = QLabel("Finalizar Venda")
        self.label_titulo.setStyleSheet("QLabel{background-color:grey; color:white; font-size: 20px}")
        # adicionar a label de titulo ao layout
        self.layout_v_total.addWidget(self.label_titulo)







        #Label dados
        self.label_dados = QLabel()

        # Criar e adicionar um layout horizontal para 
        # os dados da compra
        self.layout_h_dados = QHBoxLayout()

        #================================================================================
        # criar label da esquerda ######################################
        self.label_esquerda = QLabel()
        # Criar um layout vertical
        self.layout_v_esquerda = QVBoxLayout()
        # label para guardar o texto Total de venda
        # e a caixa total de venda, ou seja, irá
        # a guardar uma nova label e uma lineEdit
       
    #    ===================Total Venda==============================
       
        self.label_total_venda = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_total_venda = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_venda = QLabel("Total de Venda")
        # Criar a LineEdit que recebe o total de venda
        self.edit_venda = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_total_venda.addWidget(self.label_venda)
        self.layout_h_total_venda.addWidget(self.edit_venda)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_total_venda.setLayout(self.layout_h_total_venda)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_total_venda)

# ================== Fim do total venda ======================================


# =================== Inicio do Desconto ====================================

        self.label_desconto = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_desconto = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_desc = QLabel("Desconto")
        # Criar a LineEdit que recebe o total de desc
        self.edit_desc = QLineEdit("R$ 0,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_desconto.setLayout(self.layout_h_desconto)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_desconto)

# =================== Fim do Desconto =========================================



# =================== Inicio do acrescimo ====================================

        self.label_acrescimo = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_acrescimo = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_acrescimoo = QLabel("acrescimo")
        # Criar a LineEdit que recebe o total de desc
        self.edit_acrescimoo = QLineEdit("R$ 0,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_acrescimo.addWidget(self.label_acrescimoo)
        self.layout_h_acrescimo.addWidget(self.edit_acrescimoo)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_acrescimo.setLayout(self.layout_h_acrescimo)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_acrescimo)

# =================== Fim do acrescimo =========================================


# =================== Inicio do total liquido ====================================

        self.label_total_liquido = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_liquido = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_liquido = QLabel("total liquido")
        # Criar a LineEdit que recebe o total de desc
        self.edit_liquido = QLineEdit("R$ 0,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_liquido.addWidget(self.label_liquido)
        self.layout_h_liquido.addWidget(self.edit_liquido)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_total_liquido.setLayout(self.layout_h_liquido)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_total_liquido)

# =================== Fim do total liquido =========================================



# =================== Inicio do troco ====================================

        self.label_troco = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_troco = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_trocoo = QLabel("troco")
        # Criar a LineEdit que recebe o total de desc
        self.edit_trocoo = QLineEdit("R$ 0,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_troco.addWidget(self.label_trocoo)
        self.layout_h_troco.addWidget(self.edit_trocoo)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_troco.setLayout(self.layout_h_troco)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_troco)

# =================== Fim do troco =========================================







        # Adicionar o layout vertical da esquerda
        # na coluna da esquerda
        self.label_esquerda.setLayout(self.layout_v_esquerda)

        self.label_esquerda.setStyleSheet("QLabel{background-color:gray}")
        # adicionar a label da esquerda no layout 
        # horizontal
        self.layout_h_dados.addWidget(self.label_esquerda)
        #=============================================================



         # criar label da direita ###############################################################
        self.label_direita = QLabel()
        self.label_direita.setStyleSheet("QLabel{background-color:yellow}")
        # adicionar a label da direita no layout 
        # horizontal
        self.layout_h_dados.addWidget(self.label_direita)


#    =================== cliente ==============================
       
        self.label_cliente = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_cliente = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_clientee = QLabel("cliente")
        # Criar a LineEdit que recebe o total de venda
        self.edit_clientee = QLineEdit("1 - consumidor final")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_cliente.addWidget(self.label_clientee)
        self.layout_h_cliente.addWidget(self.edit_clientee)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_cliente.setLayout(self.layout_h_cliente)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_h_dados.addWidget(self.label_cliente)

# ================== Fim do cliente ======================================



#    =================== vendedor ==============================
       
        self.label_vendedor = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_vendedor = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_vendedorr = QLabel("vendedor")
        # Criar a LineEdit que recebe o total de venda
        self.edit_vendedorr = QLineEdit(" 999 - syndata")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_vendedor.addWidget(self.label_vendedorr)
        self.layout_h_vendedor.addWidget(self.edit_vendedorr)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_vendedor.setLayout(self.layout_h_vendedor)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_h_dados.addWidget(self.label_vendedor)

# ================== Fim do cliente ======================================






        self.label_dados.setLayout(self.layout_h_dados)
        self.label_dados.setStyleSheet("QLabel{background-color:red}")
        self.layout_v_total.addWidget(self.label_dados)
        
        









        #Label rodape
        self.label_rodape = QLabel()
        self.label_rodape.setStyleSheet("QLabel{background-color:green}")
        self.layout_v_total.addWidget(self.label_rodape)

        # adicionar o layout vertical a tela
        self.setLayout(self.layout_v_total)

app = QApplication(sys.argv)
tela = CaixaMercado()
tela.show()
app.exec()