# arquivo = open('helloworld.txt', 'w')
# for linha in range(1, 101):
#     arquivo.write("%d\n" % linha)
# arquivo.close()

# arquivo = open('helloworld.txt', 'r')
# ponto = "."
# for linha in arquivo.readlines():
#     print(ponto + linha.rstrip())
#     ponto += "."
# arquivo.close()

arquivo = open('sites.html', 'w')

titulo = input("Digite o título de sua página")
texto = input("Digite o texto do cabeçalho")
link = input("Digite o link (Ex: Google.com, Facebook.com)")
aliasLink = input("Digite o nome do link (Ex: Google, Facebook)")
link2 = input("Digite o link (Ex: Google.com, Facebook.com)")
aliasLink2 = input("Digite o nome do link (Ex: Google, Facebook)")
arquivo.write(''' <HTML> \n
                  <head> \n 
                  <title> \n {} \n </title> \n
                  </head> \n 
                  <h1> \n {} \n</h1> \n 
                  <a href="{}"> {} \n </a> \n 
                  <a href="{}"> {} \n </a> 
                  </HTML> '''.format(titulo, texto, link, aliasLink, link2, aliasLink2))