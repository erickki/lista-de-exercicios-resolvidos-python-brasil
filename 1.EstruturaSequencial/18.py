#18.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
#   (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def calcular_tempo_download(tamanho_arquivo_mb, velocidade_link_mbps):
    velocidade_link_mbps_em_mbs = velocidade_link_mbps * 0.125
    tempo_download_segundos = tamanho_arquivo_mb / velocidade_link_mbps_em_mbs
    tempo_download_minutos = tempo_download_segundos / 60
    return tempo_download_minutos

tamanho_arquivo = float(input("Informe o tamanho do arquivo para download (em MB): "))
velocidade_link = float(input("Informe a velocidade do link de Internet (em Mbps): "))

tempo = calcular_tempo_download(tamanho_arquivo, velocidade_link)

print(f"O tempo aproximado de download é: {tempo:.2f} minutos.")
