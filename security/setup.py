from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from psycopg2 import sql
import secrets, subprocess, datetime, psycopg2, jwt

secret_key = 'chave_auth'

def gerar_token(usuario_id):
    payload = {
        'user_id': usuario_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  
    }
    return jwt.encode(payload, secret_key, algorithm='HS256')

def verificar_token(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expirado")
    except jwt.InvalidTokenError:
        raise ValueError("Token inválido")

conn = psycopg2.connect("dbname=test user=postgres password=secret")
cursor = conn.cursor()

email = 'usuario@example.com'  # Substitua com o valor do email desejado

cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
result = cursor.fetchall()

print(result)

cursor.close()
conn.close()

key = Fernet.generate_key()
cipher = Fernet(key)
encrypted = cipher.encrypt(b"Sensitive data")
decrypted = cipher.decrypt(encrypted)
import bcrypt

senha = b"minha_senha_super_secreta"
salt = bcrypt.gensalt()  
hashed = bcrypt.hashpw(senha, salt)  
print(hashed)


senha_fornecida = b"minha_senha_super_secreta"
if bcrypt.checkpw(senha_fornecida, hashed):
    print("Senha correta")
else:
    print("Senha incorreta")
def analisar_vulnerabilidades(caminho_projeto):

  comando = f"bandit -r {caminho_projeto}"
  resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

  print(resultado.stdout)
  print(resultado.stderr)

  return resultado.returncode

if __name__ == "__main__":
  caminho = "../index.html"  
  codigo_saida = analisar_vulnerabilidades(caminho)

  if codigo_saida == 0:
    print("A análise foi concluída sem encontrar vulnerabilidades.")
  else:
    print("Foram encontradas vulnerabilidades. Verifique a saída do Bandit.")


class SecurityUtils:
    """Classe utilitária para funções de segurança com geração de chaves seguras."""
    
    @staticmethod
    def generate_master_key():
        """Gera uma chave mestra segura de 64 bytes, metade para AES e metade para HMAC."""
        return secrets.token_bytes(64)  
    
    @staticmethod
    def generate_iv():
        """Gera um IV (vetor de inicialização) seguro para AES-GCM."""
        return secrets.token_bytes(12)  

class CassinoDataProtector:
    def __init__(self):
        self.master_key = SecurityUtils.generate_master_key()
        self.encryption_key = self.master_key[:32]  
        self.hmac_key = self.master_key[32:]        
        print(f"Chave de criptografia gerada (não compartilhe): {self.master_key.hex()}")

    def encrypt_data(self, data):
        """Criptografa dados usando AES-GCM e gera HMAC para autenticação."""
        iv = SecurityUtils.generate_iv()
        
        encryptor = Cipher(
            algorithms.AES(self.encryption_key),
            modes.GCM(iv),
            backend=default_backend()
        ).encryptor()
        
        ciphertext = encryptor.update(data.encode('utf-8')) + encryptor.finalize()
        aes_tag = encryptor.tag
        
        h = hmac.HMAC(self.hmac_key, hashes.SHA256(), backend=default_backend())
        h.update(iv + aes_tag + ciphertext)
        hmac_tag = h.finalize() 

        return iv, ciphertext, aes_tag, hmac_tag

    def decrypt_data(self, iv, ciphertext, aes_tag, hmac_tag):
        """Descriptografa os dados usando AES-GCM e valida com HMAC."""
        h = hmac.HMAC(self.hmac_key, hashes.SHA256(), backend=default_backend())
        h.update(iv + aes_tag + ciphertext)
        
        try:
            h.verify(hmac_tag)
            print("HMAC verificado com sucesso.")
        except Exception as e:
            raise ValueError("Erro de autenticação: os dados foram alterados ou corrompidos.")
        
        decryptor = Cipher(
            algorithms.AES(self.encryption_key),
            modes.GCM(iv, aes_tag),
            backend=default_backend()
        ).decryptor()
        
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        return decrypted_data.decode('utf-8')

if __name__ == "__main__":
    protector = CassinoDataProtector()
    
    user_id = "user12345"
    password = "SenhaSegura!@#123"
    transaction_value = "1500.00"

    sensitive_data = f"{user_id}|{password}|{transaction_value}"
    
    iv, ciphertext, aes_tag, hmac_tag = protector.encrypt_data(sensitive_data)
    print(f"Dados criptografados: {ciphertext.hex()}")
    print(f"Tag HMAC: {hmac_tag.hex()}")
    
    decrypted_data = protector.decrypt_data(iv, ciphertext, aes_tag, hmac_tag)
    print(f"Dados descriptografados: {decrypted_data}")


