import pygame
import time
import psutil

altura_tela = 600
largura_tela = 600
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((largura_tela, altura_tela))
main_running = True
cpu_running = False
memory_running = False
disk_running = False
ip_running = False

# colors
green_bars = (50, 205, 50)
bg_color = (30, 30, 30)
botao_color = (0, 50, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# dados

# cpu
cpu = psutil.cpu_percent()

# memoria
memory = psutil.virtual_memory()
memory_percent = memory[2]

# disco
disk_usage = psutil.disk_usage('.')
disk_percent = disk_usage.percent

# IP
psutil.net_connections()
dic_interfaces = psutil.net_if_addrs()
adress_data = dic_interfaces["Wi-fi"] # Alterar
adress_ip = adress_data[1][1]

# elements_bg
left_bar = pygame.Rect(50, 0, 10, altura_tela - 100)
bottom_bar = pygame.Rect(50, altura_tela - 100, largura_tela - 50, 10)

# textos
fonte_id = pygame.font.Font(None, 15)
fonte = pygame.font.Font(None, 24)
fonte_titulo = pygame.font.Font(None, 50)

seta_page = fonte_titulo.render("<=  =>", 1, green_bars)

cpu_text = fonte.render("CPU", 1, green_bars)
cpu_text_title = fonte_titulo.render("CPU", 1, green_bars)

memory_text = fonte.render("Memory", 1, green_bars)
memory_text_title = fonte_titulo.render("MEMORY", 1, green_bars)

disk_text = fonte.render("Disk usage", 1, green_bars)
disk_text_title = fonte_titulo.render("DISK", 1, green_bars)

ip_text = fonte_id.render(adress_ip, 1, green_bars)
ip_text_title = fonte_titulo.render("ETHERNET", 1, green_bars)

# barras_dados
bar_page_bg = pygame.Rect(450, 50, 50, 500)
bar_page_border = pygame.Rect(440, 40, 70, 520)

cpu_bar = pygame.Rect(140, altura_tela - 100, 50, 0)
cpu_bar_page = pygame.Rect(450, 50, 50, 0)

memory_bar = pygame.Rect(240, altura_tela - 100, 50, 0)
memory_bar_page = pygame.Rect(450, 50, 50, 0)

disk_bar = pygame.Rect(340, altura_tela - 100, 50, 0)
disk_bar_page = pygame.Rect(450, 50, 50, 0)

# botao
cpu_botao = pygame.Rect(132, altura_tela - 58, 70, 30)
memory_botao = pygame.Rect(235, altura_tela - 58, 90, 30)
disk_botao = pygame.Rect(350, altura_tela - 58, 110, 30)
ip_botao = pygame.Rect(5, altura_tela - 25, 80, 20)


# barras_automaticas
def dados_att():
    global cpu_bar, memory_bar, disk_bar, cpu_bar_page, disk_bar_page, memory_bar_page
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    memory_percent = memory[2]
    disk_usage = psutil.disk_usage('.')
    disk_percent = disk_usage.percent

    cpu_bar = pygame.Rect(140, altura_tela - 100 - (cpu * 5), 50, cpu * 5)
    cpu_bar_page = pygame.Rect(450, altura_tela - 50 - (cpu * 5), 50, cpu * 5)

    memory_bar = pygame.Rect(255, altura_tela - 100 - (memory_percent * 5), 50, memory_percent * 5)
    memory_bar_page = pygame.Rect(450, altura_tela - 50 - (memory_percent * 5), 50, memory_percent * 5)

    disk_bar = pygame.Rect(375, altura_tela - 100 - (disk_percent * 5), 50, disk_percent * 5)
    disk_bar_page = pygame.Rect(450, altura_tela - 50 - (disk_percent * 5), 50, disk_percent * 5)


def desenha_seta():
    pygame.draw.line(screen, green_bars, (560, altura_tela - 30), (575, altura_tela - 40), 3)
    pygame.draw.line(screen, green_bars, (560, altura_tela - 50), (575, altura_tela - 40), 3)
    pygame.draw.line(screen, green_bars, (550, altura_tela - 30), (535, altura_tela - 40), 3)
    pygame.draw.line(screen, green_bars, (550, altura_tela - 50), (535, altura_tela - 40), 3)


while main_running:
    # cursor_att
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

        # imagem do cursor encima dos botoes
        if cpu_botao.collidepoint(pos) or ip_botao.collidepoint(pos) or memory_botao.collidepoint(
                pos) or disk_botao.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        # clique nos botoes para levar as respectivas paginas
        if event.type == pygame.MOUSEBUTTONDOWN and cpu_botao.collidepoint(pos):
            cpu_running = True
        if event.type == pygame.MOUSEBUTTONDOWN and memory_botao.collidepoint(pos):
            memory_running = True
        if event.type == pygame.MOUSEBUTTONDOWN and disk_botao.collidepoint(pos):
            disk_running = True
        if event.type == pygame.MOUSEBUTTONDOWN and ip_botao.collidepoint(pos):
            ip_running = True

        # mudar as paginas com as setas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cpu_running = True
            if event.key == pygame.K_LEFT:
                ip_running = True

    if not cpu_running and not ip_running and not memory_running and not disk_running:

        # pegar_att_dados
        time.sleep(0.5)
        dados_att()

        # bg att
        porcentagem = 100  # inserir a porcentagem do lado esquerdo da tela
        screen.fill(bg_color)

        for i in range(5, largura_tela - 100, 50):  # inserir a porcentagem do lado esquerdo da tela
            valor = fonte.render(f'{porcentagem}%', 1, green_bars)
            screen.blit(valor, (5, i))
            porcentagem -= 10

        for i in range(0, largura_tela - 100, 50):  # inserir as barras finas para medir a porcentagem
            bg_bars = pygame.Rect(50, i, largura_tela, 1)
            pygame.draw.rect(screen, green_bars, bg_bars)

        pygame.draw.rect(screen, green_bars, left_bar)  # barra_vertical_esquerda
        pygame.draw.rect(screen, green_bars, bottom_bar)  # barra_horizontal_baixo

        # inserir_att_dados
        pygame.draw.rect(screen, botao_color, cpu_botao)
        pygame.draw.rect(screen, green_bars, cpu_bar)
        screen.blit(cpu_text, (150, altura_tela - 50))

        pygame.draw.rect(screen, botao_color, memory_botao)
        pygame.draw.rect(screen, green_bars, memory_bar)
        screen.blit(memory_text, (250, altura_tela - 50))

        pygame.draw.rect(screen, botao_color, disk_botao)
        pygame.draw.rect(screen, green_bars, disk_bar)
        screen.blit(disk_text, (360, altura_tela - 50))

        pygame.draw.rect(screen, botao_color, ip_botao)
        screen.blit(ip_text, (10, altura_tela - 20))

        desenha_seta()

        pygame.display.update()
        clock.tick(60)

    while cpu_running:
        # cursor_att
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cpu_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    cpu_running = False
                    memory_running = True
                if event.key == pygame.K_LEFT:
                    cpu_running = False

        # dados
        time.sleep(0.5)
        dados_att()

        screen.fill(bg_color)

        pygame.draw.rect(screen, black, bar_page_border)
        pygame.draw.rect(screen, green_bars, bar_page_bg)
        pygame.draw.rect(screen, red, cpu_bar_page)

        screen.blit(cpu_text_title, (5, 7))
        desenha_seta()

        pygame.display.update()
        clock.tick(60)

    while memory_running:
        # cursor_att
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    memory_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    memory_running = False
                    disk_running = True
                if event.key == pygame.K_LEFT:
                    memory_running = False
                    cpu_running = True

        # dados
        time.sleep(0.5)
        dados_att()

        screen.fill(bg_color)

        pygame.draw.rect(screen, black, bar_page_border)
        pygame.draw.rect(screen, green_bars, bar_page_bg)
        pygame.draw.rect(screen, red, memory_bar_page)

        screen.blit(memory_text_title, (5, 7))
        desenha_seta()

        pygame.display.update()
        clock.tick(60)

    while disk_running:
        # cursor_att
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    disk_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    disk_running = False
                    ip_running = True
                if event.key == pygame.K_LEFT:
                    disk_running = False
                    memory_running = True

        # dados
        time.sleep(0.5)
        dados_att()

        screen.fill(bg_color)

        pygame.draw.rect(screen, black, bar_page_border)
        pygame.draw.rect(screen, green_bars, bar_page_bg)
        pygame.draw.rect(screen, red, disk_bar_page)

        screen.blit(disk_text_title, (5, 7))
        desenha_seta()

        pygame.display.update()
        clock.tick(60)

    while ip_running:
        # cursor_att
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ip_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ip_running = False
                if event.key == pygame.K_LEFT:
                    ip_running = False
                    disk_running = True
        # dados
        time.sleep(0.5)
        dados_att()

        screen.fill(bg_color)

        screen.blit(ip_text_title, (5, 7))
        desenha_seta()

        pygame.display.update()
        clock.tick(60)

pygame.display.quit()
pygame.quit()