import pygame
import time
import psutil
import cpuinfo
import platform
import socket

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
linux = False
info = cpuinfo.get_cpu_info()
# colors
green_bars = (50, 205, 50)
bg_color = (30, 30, 30)
botao_color = (0, 50, 0)
red = (255, 0, 0)
black = (0, 0, 0)
light_gray = (200, 200, 200)
blue = (0, 0, 255)

# dados

# cpu
cpu = psutil.cpu_percent(percpu=False)
info = cpuinfo.get_cpu_info()

nucleos = psutil.cpu_percent(percpu=True)
processadores_logicos = info['count']
qtd_nucleos = psutil.cpu_count(logical=False)
processador = info['brand_raw']
arquitetura = info['bits']
arquitetura_arch = info['arch']
freq = psutil.cpu_freq(percpu=False)
freq_atual = freq[0]
freq_total = freq[2]

# memoria
memory = psutil.virtual_memory()
memory_percent = memory[2]
memory_used = memory[3]
memory_available = memory[1]
memory_total = memory[0]
system = platform.system()
if system == "Linux":
    memory_cache = memory[9]
    linux = True

# disco
disk_usage = psutil.disk_usage('.')
disk_percent = disk_usage.percent

disk_used = disk_usage.used
disk_free = disk_usage.free
disk_total = disk_usage.total

# IP
hostname = socket.gethostname()
ipv4 = socket.gethostbyname(hostname)
ip = socket.gethostbyaddr(hostname)
ipv6 = ip[2][0]

ip_data = psutil.net_io_counters(pernic=False, nowrap=True)
ip_sent = ip_data[0]
ip_receive = ip_data[1]

# elements_bg
left_bar = pygame.Rect(50, 0, 10, altura_tela - 100)
bottom_bar = pygame.Rect(50, altura_tela - 100, largura_tela - 50, 10)

# textos
fonte_id = pygame.font.Font(None, 15)
fonte = pygame.font.Font(None, 24)
fonte_titulo = pygame.font.Font(None, 50)
font_cpu_page = pygame.font.Font(None, 20)

# cpu
cpu_text = fonte.render("CPU", 1, green_bars)
cpu_text_title = fonte_titulo.render("CPU", 1, green_bars)
cpu_nucleo_text = fonte.render("Uso de CPU por nucleo: ", 1, green_bars)
cpu_percent_text = fonte_titulo.render(f"{cpu}%", 1, green_bars)

cpu_processador_text = font_cpu_page.render(f"Processador: {processador}", 1, green_bars)
cpu_qtd_nucleos_text = font_cpu_page.render(f"Nucleos: {qtd_nucleos} ", 1, green_bars)
cpu_proc_logicos_text = font_cpu_page.render(f"Processadores logicos: {processadores_logicos} ", 1, green_bars)
cpu_arq_text = font_cpu_page.render(f"Arquitetura: {arquitetura_arch}, {arquitetura} (bits)", 1, green_bars)
cpu_freqTotal_text = font_cpu_page.render(f"Velocidade base: {(freq_total / 1000):.3f} Ghz", 1, green_bars)
cpu_freqAtual_text = fonte.render(f"Velocidade: {(freq_atual / 1000):.3f} Ghz", 1, green_bars)

# memory
memory_text = fonte.render("Memory", 1, green_bars)
memory_text_title = fonte_titulo.render("MEMORY", 1, green_bars)

memory_percent_text = fonte_titulo.render(f"{memory_percent}%", 1, green_bars)
memory_available_text = fonte_titulo.render(f"Free: {memory_available / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)
memory_used_text = fonte_titulo.render(f"Used: {memory_used / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)
memory_total_text = fonte_titulo.render(f"Total: {memory_total / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)
if linux == True:
    memory_cache_text = fonte.render(f"Cache: {memory_cache}", 1, green_bars)

# disk
disk_text = fonte.render("Disk usage", 1, green_bars)
disk_text_title = fonte_titulo.render("DISK", 1, green_bars)

disk_percent_text = fonte_titulo.render(f"{disk_percent}%", 1, green_bars)
disk_free_text = fonte_titulo.render(f"Free: {disk_free / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)
disk_used_text = fonte_titulo.render(f"Used: {disk_used / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)
disk_total_text = fonte_titulo.render(f"Total: {disk_total / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)

# ip
ip_text = fonte_id.render(ipv4, 1, green_bars)
ip_text_title = fonte_titulo.render("ETHERNET", 1, green_bars)

ip_sent_text = fonte_titulo.render(f"Enviar: {ip_sent / (1024):.1f} Kb", 1, green_bars)
ip_receive_text = fonte_titulo.render(f"Receber: {ip_receive / (1024):.1f} Kb", 1, green_bars)
ipv4_text = fonte.render(f"Endereço Ipv4: {ipv4}", 1, green_bars)
ipv6_text = fonte.render(f"Endereço Ipv6: {ipv6}", 1, green_bars)

# barras_dados
bar_page_bg = pygame.Rect(450, 50, 50, 500)
bar_page_border = pygame.Rect(440, 40, 70, 520)

bar_nucleos_bg = pygame.Rect(75, 75, 300, 400)
bar_nucleos_bg_border = pygame.Rect(65, 65, 320, 420)

cpu_bar = pygame.Rect(140, altura_tela - 100, 50, 0)
cpu_bar_page = pygame.Rect(450, 50, 50, 0)

memory_bar = pygame.Rect(240, altura_tela - 100, 50, 0)
memory_bar_page = pygame.Rect(450, 50, 50, 0)

disk_bar = pygame.Rect(340, altura_tela - 100, 50, 0)
disk_bar_page = pygame.Rect(450, 50, 50, 0)

ip_sent_bar = pygame.Rect(100, 50, 0, 50)
ip_receive_bar = pygame.Rect(100, 50, 0, 50)
bar_ip_border = pygame.Rect(0, 100, 600, 350)
bar_ip_limite = pygame.Rect(largura_tela - 100, 100, 100, 350)

# botao
cpu_botao = pygame.Rect(132, altura_tela - 58, 70, 30)
memory_botao = pygame.Rect(235, altura_tela - 58, 90, 30)
disk_botao = pygame.Rect(350, altura_tela - 58, 110, 30)
ip_botao = pygame.Rect(5, altura_tela - 25, 80, 20)


def cpu_information():
    global nucleos, cpu_freqAtual_text, cpu_percent_text, cpu_bar, cpu_bar_page

    nucleos = psutil.cpu_percent(percpu=True)
    cpu = psutil.cpu_percent(percpu=False)
    cpu_percent_text = fonte_titulo.render(f"{cpu}%", 1, green_bars)
    freq = psutil.cpu_freq(percpu=False)
    freq_atual = freq[0]
    cpu_freqAtual_text = fonte.render(f"Velocidade: {(freq_atual):.3f} GHz", 1, green_bars)

    cpu_bar = pygame.Rect(140, altura_tela - 100 - (cpu * 5), 50, cpu * 5)
    cpu_bar_page = pygame.Rect(450, altura_tela - 50 - (cpu * 5), 50, cpu * 5)


def memory_information():
    global memory_percent_text, memory_available_text, memory_used_text, memory_cache_text, memory_bar, memory_bar_page

    memory = psutil.virtual_memory()
    memory_percent = memory[2]
    memory_used = memory[3]
    memory_available = memory[1]
    memory_percent_text = fonte_titulo.render(f"{memory_percent}%", 1, green_bars)
    memory_available_text = fonte_titulo.render(f"Free: {memory_available / (1024 * 1024 * 1024):.2f} GB", 1,
                                                green_bars)
    memory_used_text = fonte_titulo.render(f"Used: {memory_used / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)
    if linux == True:
        memory_cache = memory[9]
        memory_cache_text = fonte.render(f"Cache: {memory_cache / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)

    memory_bar = pygame.Rect(255, altura_tela - 100 - (memory_percent * 5), 50, memory_percent * 5)
    memory_bar_page = pygame.Rect(450, altura_tela - 50 - (memory_percent * 5), 50, memory_percent * 5)


def disk_information():
    global disk_percent_text, disk_free_text, disk_used_text, disk_bar, disk_bar_page

    disk_usage = psutil.disk_usage('.')
    disk_percent = disk_usage.percent

    disk_used = disk_usage.used
    disk_free = disk_usage.free
    disk_percent_text = fonte_titulo.render(f"{disk_percent}%", 1, green_bars)
    disk_free_text = fonte_titulo.render(f"Free: {disk_free / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)
    disk_used_text = fonte_titulo.render(f"Used: {disk_used / (1024 * 1024 * 1024):.2f} GB", 1, green_bars)

    disk_bar = pygame.Rect(375, altura_tela - 100 - (disk_percent * 5), 50, disk_percent * 5)
    disk_bar_page = pygame.Rect(450, altura_tela - 50 - (disk_percent * 5), 50, disk_percent * 5)


def ip_information():
    global ip_sent, ip_sent, ip_sent_text, ip_receive_text, ip_receive, ip_sent_bar, ip_receive_bar

    ip_sent_var = ip_sent
    ip_receive_var = ip_receive

    time.sleep(1)

    ip_data = psutil.net_io_counters(pernic=False, nowrap=True)
    ip_sent = ip_data[0]
    ip_receive = ip_data[1]

    ip_sent_text = fonte_titulo.render(f"Enviar: {((ip_sent - ip_sent_var) / 1024):.1f} Kbps", 1, green_bars)
    ip_receive_text = fonte_titulo.render(f"Receber: {((ip_receive - ip_receive_var) / 1024):.1f} Kbps", 1, green_bars)

    ip_sent_bar = pygame.Rect(100, 200, ((ip_sent - ip_sent_var) / 1024), 40)
    ip_receive_bar = pygame.Rect(100, 300, ((ip_receive - ip_receive_var) / 1024), 40)


def desenha_nucleos():
    x_nucleo = 75
    nucleos_counter = 1
    for nucleo in nucleos:
        if nucleos_counter > 10:
            y_nucleo = 475 - (nucleo * (1.5))
        else:
            y_nucleo = 275 - (nucleo * (1.5))
        nucleos_counter += 1
        nucleo = pygame.Rect(x_nucleo, y_nucleo, 30, (nucleo * (1.5)))
        pygame.draw.rect(screen, red, nucleo)
        x_nucleo += 30
        if x_nucleo >= 375:
            x_nucleo = 75


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
        cpu_information()
        disk_information()
        memory_information()

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
        cpu_information()

        screen.fill(bg_color)

        pygame.draw.rect(screen, black, bar_nucleos_bg_border)
        pygame.draw.rect(screen, green_bars, bar_nucleos_bg)
        desenha_nucleos()
        pygame.draw.line(screen, black, (65, 275), (380, 275), 5)  # divisao pela metade do fundo dos nucleos

        for x in range(105, 125 + (30 * 8) + 1, 30):  # linhas verticais para dividir os nucleos
            pygame.draw.line(screen, black, (x, 65), (x, 475), 3)

        pygame.draw.rect(screen, black, bar_page_border)
        pygame.draw.rect(screen, green_bars, bar_page_bg)
        pygame.draw.rect(screen, red, cpu_bar_page)

        screen.blit(cpu_nucleo_text, (75, 50))
        screen.blit(cpu_percent_text, (445, 10))

        screen.blit(cpu_processador_text, (20, 500))
        screen.blit(cpu_arq_text, (20, 520))
        screen.blit(cpu_proc_logicos_text, (20, 540))
        screen.blit(cpu_qtd_nucleos_text, (20, 560))
        screen.blit(cpu_freqTotal_text, (20, 580))
        screen.blit(cpu_freqAtual_text, (220, 550))

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
        memory_information()

        screen.fill(bg_color)

        pygame.draw.rect(screen, black, bar_page_border)
        pygame.draw.rect(screen, green_bars, bar_page_bg)
        pygame.draw.rect(screen, red, memory_bar_page)

        screen.blit(memory_text_title, (5, 7))
        desenha_seta()

        screen.blit(memory_percent_text, (445, 10))
        screen.blit(memory_available_text, (100, 200))
        screen.blit(memory_used_text, (100, 250))
        screen.blit(memory_total_text, (100, 350))
        if linux == True:
            screen.blit(memory_cache_text, (20, 500))

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
        disk_information()

        screen.fill(bg_color)

        pygame.draw.rect(screen, black, bar_page_border)
        pygame.draw.rect(screen, green_bars, bar_page_bg)
        pygame.draw.rect(screen, red, disk_bar_page)

        screen.blit(disk_text_title, (5, 7))
        desenha_seta()

        screen.blit(disk_percent_text, (445, 10))
        screen.blit(disk_free_text, (100, 200))
        screen.blit(disk_used_text, (100, 250))
        screen.blit(disk_total_text, (100, 350))

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
        ip_information()

        screen.fill(bg_color)
        screen.blit(ip_text_title, (5, 7))

        pygame.draw.rect(screen, black, bar_ip_border)

        screen.blit(ip_sent_text, (100, 150))
        pygame.draw.rect(screen, green_bars, ip_sent_bar)

        screen.blit(ip_receive_text, (100, 250))
        pygame.draw.rect(screen, green_bars, ip_receive_bar)

        screen.blit(ipv4_text, (100, 350))
        screen.blit(ipv6_text, (100, 370))

        pygame.draw.rect(screen, black, bar_ip_limite)
        desenha_seta()

        pygame.display.update()
        clock.tick(60)

pygame.display.quit()
pygame.quit()