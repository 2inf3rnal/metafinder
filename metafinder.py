#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests as r
import sys
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

# DIRETORIOS ::::::::::::
ear_php = ["admin.php", "logado.php", "principal.php", "painel.php", "sistema.php", "noticias.php", "index.php", "index2.php", "index1.php", "inicial.php", "inicio.php", "menu.php", "upload.php", "agenda.php", "pagina.php", "admin/", "adm.php", "adm/", "admin_index.php", "paineladministrativo.php", "paineladministrativo", "intranet/", "intranet.php", "intra/", "intra.php", "paineldecontrole.php", "controle.php", "paineldecontrole/", "controle/", "gerenciador/", "gerencia/", "gerenciar/", "gerenciador.php", "gerencia.php", "gerenciar.php", "dashboard/", "dashboard.php", "control/", "control.php", "main.php", "main/", "iniciar.php", "inicia/", "login1.php", "login1/", "album.php", "album/", "noticias/", "manager.php", "manage/", "star.php", "start/", "lista.php", "lista/", "editar.php", "editar/", "inserir.php", "inserir/", "usuario/", "usuario.php", "server/", "server.php", "root.php", "root/"]
procura_login = "login" or "entrar" or "usuario" or "senha" or "painel" or "admin" or "restrito" or "adm"
admin_page = "logado" or "bem vindo" or "sistema" or "intranet" or "painel" or "admin" or "restrito" or "adm"
admin_pages = ["login.php","usuario/","usuarios/","admin/", "adm/", "painel/", "panel/", "administrador/", "administrator/", "administrative/", "administrar/", "intranet/", "paineldecontrole/", "painel_de_controle/", "atualizar/", "suporte/", "controle/", "controlar/", "servidor/", "server/", "root/", "admin_login/", "admin_index/", "sistema/", "sistemas/", "logar_admin/", "login_admin/", "3d/", "configurar/", "config/", "intra/", "area/","admin/login.php", "adm/login.php", "painel/login.php", "panel/login.php", "administrador/login.php", "administrator/login.php", "administrative/login.php", "administrar/login.php", "intranet/login.php", "paineldecontrole/login.php", "painel_de_controle/login.php", "atualizar/login.php", "suporte/login.php", "controle/login.php", "controlar/login.php", "servidor/login.php", "server/login.php", "root/login.php", "admin_login/login.php", "admin_index/login.php", "sistema/login.php", "sistemas/login.php", "logar_admin/login.php", "login_admin/login.php", "3d/login.php", "configurar/login.php", "config/login.php", "intra/login.php", "area/login.php", "wp-login.php", "dashboard/", "dashboard.php"]
# INDEX ::::::::::::
index = """
___  ___     _       ______ _           _           
|  \/  |    | |      |  ___(_)         | |     Recoda não comédia!     
| .  . | ___| |_ __ _| |_   _ _ __   __| | ___ _ __ 
| |\/| |/ _ \ __/ _` |  _| | | '_ \ / _` |/ _ \ '__|
| |  | |  __/ || (_| | |   | | | | | (_| |  __/ |   
\_|  |_/\___|\__\__,_\_|   |_|_| |_|\__,_|\___|_|   
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                      Metafinder v1.0
# Facebook :: www.facebook.com/yunkers01/ ou www.facebook.com/yunkers1/
# IRC :: Servidor = Afternet e canal = #yunkerscrew
# Autor :: Supr3m0 e W4r1o6k
# Github :: www.github.com/2inf3rnal/
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""

# Verifica Parãmetros ::::::::::::
x = sys.argv
script = x[0]

if len(x) == 7:
	if x[1] == "--ferramenta":
		ferramenta = x[2]
	else:
		print(Fore.GREEN + index)
		print(Fore.RED + "[-]" + Fore.WHITE + " Parãmetros inválidos!")
		print(Fore.GREEN + "    Use: python3",script, "--ferramenta <admin, ear> --url <http[s]://site.com/> --ext <php, asp, aspx, html, jsp, cgi>")
		exit()
	if x[3] == "--url":
		url = x[4]
	else:
		print(Fore.GREEN + index)
		print(Fore.RED + "[-]" + Fore.WHITE + " Parãmetros inválidos!")
		print(Fore.GREEN + "    Use: python3",script, "--ferramenta <admin, ear> --url <http[s]://site.com/> --ext <php, asp, aspx, html, jsp, cgi>")
		exit()
	if x[5] == "--ext":
		ext = x[6]
	else:
		print(Fore.GREEN + index)
		print(Fore.RED + "[-]" + Fore.WHITE + " Parãmetros inválidos!")
		print(Fore.GREEN + "    Use: python3",script, "--ferramenta <admin, ear> --url <http[s]://site.com/> --ext <php, asp, aspx, html, jsp, cgi>")
		exit()
else:
	print(Fore.GREEN + index)
	print(Fore.RED + "[-]" + Fore.WHITE + " Parãmetros inválidos!")
	print(Fore.GREEN + "    Use: python3",script, "--ferramenta <admin, ear> --url <http[s]://site.com/> --ext <php, asp, aspx, html, jsp, cgi>")
	exit()

# Verifica requisição ::::::::::::
print(Fore.GREEN + index)
print(Fore.BLUE + "[...]" + Fore.WHITE + " Verificando conexão, aguarde.")
def checa_url(url):
	if url[-1] != "/":
		url = url + "/"
	# H T T P : / /
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url
try:
	url = checa_url(url)
	checa_site = r.get(url)
	s_code = checa_site.status_code
	if s_code == 404:
		print(Fore.RED + "[-]" + Fore.WHITE + " Erro em conectar ao site", url)
		exit()
except Exception as err:
	print(Fore.RED + "[-]" + Fore.WHITE + " Erro em conectar ao site", url)
	exit()

# Checa finder ::::::::::::
if ferramenta == "admin":
	tipo = "Painel de controle (login)"
elif ferramenta == "ear":
	tipo = "Manager para falhas E.A.R"
else:
	print(Fore.RED + "[-]" + Fore.WHITE + " Tipo de finder inválido.")
	exit()
print(Fore.BLUE + "\n[+]" + Fore.WHITE + " Site:",url)
print(Fore.BLUE + "[+]" + Fore.WHITE + " Status:", s_code)
print(Fore.BLUE + "[+]" + Fore.WHITE + " Tipo de busca:", tipo)
print(Fore.BLUE + "[+]" + Fore.WHITE + " EXT:", ext)


# Admin finder ::::::::::::
testa = 0
achadas = 0
if ferramenta == "admin":
	x_ext = ["php", "asp", "aspx", "html", "jsp", "cgi"]
	if ext not in x_ext:
		print(Fore.RED + "[-]" + Fore.WHITE + " Tipo de EXT inválido!")
		exit()
	else:
		for i in admin_pages:
			x_patch = [i.replace('php', ext) for i in admin_pages]
		print(Fore.BLUE + "\n[*]" + Fore.WHITE + " Iniciando scan :)")
		print(Fore.YELLOW + "(Vai aparecer apenas os diretorios que não retornar '404')")
		for pagina in x_patch:
			admin_dir = url + pagina
			checa_admin = r.get(admin_dir)
			testa += 1
			if checa_admin.status_code != 404:
				achadas += 1
				if procura_login in checa_admin.text:
					print(Fore.GREEN + "    [!]" + Fore.WHITE + " Painel administrativo: " + Fore.YELLOW + admin_dir)
				else:
					print(Fore.GREEN + "    [!]" + Fore.WHITE + " Possível painel administrativo:" + Fore.YELLOW + admin_dir)
			else:
				continue
		if achadas == 0:
			print(Fore.RED + "\n:´(" + Fore.WHITE + " Não encontramos nenhuma página de login.")
		else:
			print(Fore.GREEN + "[=]" + Fore.WHITE + " Total de páginas encontradas: ",achadas)
		print(Fore.GREEN + "[=]" + Fore.WHITE + " Total de páginas testadas: ",testa)
		exit()

elif ferramenta == "ear":
	x_ext = ["php", "asp", "aspx", "html", "jsp", "cgi"]
	if ext not in x_ext:
		print(Fore.RED + "[-]" + Fore.WHITE + " Tipo de EXT inválido!")
		exit()
	else:
		for i in ear_php:
			x_ear = [i.replace('php', ext) for i in ear_php]
		print(Fore.BLUE + "\n[*]" + Fore.WHITE + " Iniciando scan :)")
		print(Fore.YELLOW + "(Vai aparecer apenas os diretorios que não retornar '404')")
		for pagina in x_ear:
			admin_dir = url + pagina
			checa_admin = r.get(admin_dir)
			testa += 1
			if checa_admin.status_code != 404:
				achadas += 1
				if admin_page in checa_admin.text:
					print(Fore.GREEN + "    [!]" + Fore.WHITE + " Painel administrativo: " + Fore.YELLOW + admin_dir)
				else:
					print(Fore.GREEN + "    [!]" + Fore.WHITE + " Possível painel administrativo:" + Fore.YELLOW + admin_dir)
			else:
				continue
		if achadas == 0:
			print(Fore.RED + "\n:´(" + Fore.WHITE + " Não encontramos nenhuma página de login.")
		else:
			print(Fore.GREEN + "[=]" + Fore.WHITE + " Total de páginas encontradas: ",achadas)
		print(Fore.GREEN + "[=]" + Fore.WHITE + " Total de páginas testadas: ",testa)
		exit()
exit()
