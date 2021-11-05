from fpdf import FPDF
from datetime import datetime
from dao_project.ModelUsuario import DAOUsuario, Usuario, Endereco, DAOEndereco

class PDF(FPDF):

    #region Header e Footer
    def header(self):
        #self.image("C:\Users\leozi\Desktop\Repositorios Python\WebPythonDescubraSuaDoenca\Desenvolvimento Web\static\Desagrupar.png")
        self.set_font('arial','B', 15)
        self.cell(0, 5, 'Leonardo Meister.', 0, 1, 'C', 0)
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
    #endregion
    
    #region PDF GERAL
    def pdfGeral(self):
        pdf = PDF('P', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Leonardo Meister.")
        pdf.set_title('Dados do Perfil.')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(0, 5, 'Dados do Perfil.', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(280, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 8)
        pdf.cell(10, 5, 'ID', 0, 0, 'L')
        pdf.cell(55, 5, 'Nome', 0, 0, 'L')
        pdf.cell(30, 5, 'Telefone', 0, 0, 'L')
        pdf.cell(50, 5, 'E-Mail', 0, 0, 'L')
        pdf.cell(25, 5, 'Login', 0, 0, 'L')
        pdf.cell(20, 5, 'Grupo', 0, 0, 'L')
        pdf.cell(90, 5, 'Endereço', 0, 1, 'L')
        # busca e mostra todos os clientes
        pdf.set_font('arial', '', 8)

        #cliente = Clientes()
        #res = cliente.selectALL()
        #if res:
          #  for row in res:
           #     pdf.cell(10, 5, str(row[0]), 0, 0, 'L')
            #    pdf.cell(55, 5, str(row[1]), 0, 0, 'L')
            #    pdf.cell(30, 5, str(row[9]), 0, 0, 'L')
            #    pdf.cell(50, 5, str(row[10]), 0, 0, 'L')
            #    pdf.cell(25, 5, str(row[11]), 0, 0, 'L')
            #    pdf.cell(20, 5, str(row[12]), 0, 0, 'L')
            #    pdf.multi_cell(90, 5, "Rua: " + str(row[2]) + ", No: " + str(row[3]) + "\n" + str(row[6]) + "\n" + str(
            #        row[7]) + " - " + str(row[8]) + "\n" + str(row[5]) + "\nOBS: " + str(row[4]), '', 'L', 0) # LTRB

        # baixa o relatório criado
        pdf.output('DadosGerais.pdf')
    #endregion

    #region PDF ENDERECO
    def pdfEndereco(self):
        pdf = PDF('P', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Leonardo Meister")
        pdf.set_title('Endereços')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(0, 5, 'Endereços', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(280, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 8)
        pdf.cell(15, 5, 'ID', 0, 0, 'L')
        pdf.cell(45, 5, 'Cidade', 0, 0, 'L')
        pdf.cell(20, 5, 'Estado', 0, 0, 'L')
        pdf.cell(50, 5, 'Rua', 0, 0, 'L')
        pdf.cell(35, 5, 'Numero', 0, 1, 'L')
        
        # busca e mostra todos os clientes
        pdf.set_font('arial', '', 8)

        banco = DAOEndereco()
        res = banco.SelectAll()
        if res:
            for row in res:
                print(row)
                pdf.cell(15, 5, str(row[0]), 0, 0, 'L')
                pdf.cell(45, 5, str(row[1]), 0, 0, 'L')
                pdf.cell(20, 5, str(row[2]), 0, 0, 'L')
                pdf.cell(50, 5, str(row[3]), 0, 0, 'L')
                pdf.cell(35, 5, str(row[4]), 0, 1, 'L')

        # baixa o relatório criado
        pdf.output('PdfDadosEndereco.pdf')
    #endregion

    #region PDF PERFIL
    def  pdfPerfil(self):
        pdf = PDF('L', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Abc Bolinhas")
        pdf.set_title('Perfis')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(280, 5, 'Perfis', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(280, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 8)
        pdf.cell(10, 5, 'ID', 0, 0, 'L')
        pdf.cell(40, 5, 'Nome', 0, 0, 'L')
        pdf.cell(30, 5, 'CPF', 0, 0, 'L')
        pdf.cell(30, 5, 'Telefone', 0, 0, 'L')
        pdf.cell(45, 5, 'E-Mail', 0, 0, 'L')
        pdf.cell(25, 5, 'Tipo Sangue', 0, 0, 'L')
        pdf.cell(35, 5, 'Alergia', 0, 0, 'L')
        pdf.cell(10, 5, 'Endereco', 0, 1, 'L')
        # busca e mostra todos os clientes
        pdf.set_font('arial', '', 8)

        banco = DAOUsuario()
        res = banco.SelectAll()
        if res:
            for row in res:
                print(row)
                pdf.cell(10, 5, str(row[0]), 0, 0, 'L')
                pdf.cell(40, 5, str(row[1]), 0, 0, 'L')
                pdf.cell(30, 5, str(row[2]), 0, 0, 'L')
                pdf.cell(30, 5, str(row[3]), 0, 0, 'L')
                pdf.cell(45, 5, str(row[4]), 0, 0, 'L')
                pdf.cell(25, 5, str(row[7]), 0, 0, 'L')
                pdf.cell(35, 5, str(row[8]), 0, 0, 'L')
                pdf.cell(10, 5, str(row[9]), 0, 1, 'L')       
        # baixa o relatório criado
        pdf.output('PdfDadosPerfil.pdf')
    #endregion