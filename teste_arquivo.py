from src.dados.arquivo_excel import ExcelDados


ed = ExcelDados(
    nome_arquivo='planilha_produtos.xlsx'
)


for dado in ed.ler_valores():
    codpro, descricao,  link_fornecedor, descricao_titulo, imagens_baixadas, conteudo_da_embalagem_um, conteudo_da_embalagem_dois, detalhes_tecnicos_um, detalhes_tecnicos_dois,  certificados, certificados_html, categoria_produto, *resto = dado
    print(codpro.value, descricao.value, link_fornecedor.value,
          descricao_titulo.value, imagens_baixadas.value, conteudo_da_embalagem_um.value, conteudo_da_embalagem_dois.value, detalhes_tecnicos_um.value, detalhes_tecnicos_dois.value, certificados.value, certificados_html.value, categoria_produto.value)

    # print(codpro.value, descricao.value, link_fornecedor.value, descricao_titulo.value, imagens_baixadas.value, conteudo_da_embalagem_um.value,
    #       conteudo_da_embalagem_dois.value, detalhes_tecnicos_um.value, detalhes_tecnicos_dois.value, certificados.value, certificados_html.value, categoria_produto.value)
