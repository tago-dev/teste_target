import json
import os

def carregar_dados():
    try:
        if not os.path.exists("database/dados.json"):
            print("Erro: Arquivo 'database/dados.json' não encontrado.")
            return None
            
        with open("database/dados.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
            
    except FileNotFoundError:
        print("Erro: Diretório 'database' não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro: O arquivo não contém um JSON válido.")
        return None
    except PermissionError:
        print("Erro: Sem permissão para acessar o arquivo.")
        return None
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        return None

def calcular_menor_valor(dados):
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    return min(valores) if valores else None

def calcular_maior_valor(dados):
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    return max(valores) if valores else None

def calcular_media_mensal(dados):
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    return sum(valores) / len(valores) if valores else None

def dias_acima_da_media(dados, media):
    return len([dia for dia in dados if dia['valor'] > media])

def formatar_valor(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

data = carregar_dados()

if data:
    menor_valor = calcular_menor_valor(data)
    maior_valor = calcular_maior_valor(data)
    media_mensal = calcular_media_mensal(data)
    dias_acima_media = dias_acima_da_media(data, media_mensal)

    print(f"Menor valor de faturamento: {formatar_valor(menor_valor)}")
    print(f"Maior valor de faturamento: {formatar_valor(maior_valor)}")
    print(f"Média mensal de faturamento: {formatar_valor(media_mensal)}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")