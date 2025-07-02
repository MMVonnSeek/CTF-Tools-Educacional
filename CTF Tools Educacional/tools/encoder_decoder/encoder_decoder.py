import base64
import urllib.parse

# ============================
# Codificação e Decodificação
# ============================

# Base64
def encode_base64(texto: str) -> str:
    """
    Codifica uma string em Base64.
    """
    try:
        return base64.b64encode(texto.encode('utf-8')).decode('utf-8')
    except Exception as e:
        return f"Erro ao codificar Base64: {str(e)}"

def decode_base64(texto: str) -> str:
    """
    Decodifica uma string em Base64.
    """
    try:
        return base64.b64decode(texto.encode('utf-8')).decode('utf-8')
    except Exception as e:
        return f"Erro ao decodificar Base64: {str(e)}"

# URL
def encode_url(texto: str) -> str:
    """
    Codifica uma string em URL encoding.
    Exemplo: espaço → %20
    """
    try:
        return urllib.parse.quote(texto)
    except Exception as e:
        return f"Erro ao codificar URL: {str(e)}"

def decode_url(texto: str) -> str:
    """
    Decodifica uma string em URL encoding.
    Exemplo: %20 → espaço
    """
    try:
        return urllib.parse.unquote(texto)
    except Exception as e:
        return f"Erro ao decodificar URL: {str(e)}"
