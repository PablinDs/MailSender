import os.path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Escopo de leitura da planilha Google
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def enviar_email(destinatario, nome, departamento):
    remetente = "seu_email@gmail.com"  # Remetente (remova o e-mail real)
    senha = "sua_senha"  # Senha do e-mail (remova a senha real)
    assunto = "Teste de Comunicação 📨"
    conteudo = f"""
Olá {nome}! Você faz parte do setor {departamento}, correto?

Este é um e-mail teste enviado automaticamente.

Conforme informado mais cedo, peço para que dê um retorno confirmando se a mensagem chegou e se suas informações estão corretas.

Agradeço desde já, abraços.
"""

    # Monta a mensagem
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(conteudo, "plain"))

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, mensagem.as_string())
        servidor.quit()
        print(f"E-mail enviado com sucesso para {destinatario}")
        log = f"✔️ {nome} ({destinatario}) - Setor: {departamento} - ENVIADO\n"
    except Exception as e:
        print(f"Erro ao enviar e-mail para {destinatario}: {e}")
        log = f"❌ {nome} ({destinatario}) - Setor: {departamento} - ERRO: {e}\n"

    # Registra no log
    with open("log_emails.txt", "a", encoding="utf-8") as f:
        f.write(log)

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Conecta ao Google Sheets
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId="ID_da_sua_planilha",  # ID da planilha
            range="TESTE!A1:D51"
        ).execute()

        values = result.get("values", [])

        if not values:
            print("Nenhum dado encontrado na planilha.")
            return

        for linha in values[1:]:  # Ignora o cabeçalho
            if len(linha) >= 4:
                nome = linha[0]
                departamento = linha[2]
                email = linha[3]
                enviar_email(email, nome, departamento)

    except HttpError as error:
        print(f"Ocorreu um erro ao acessar a planilha: {error}")

if __name__ == "__main__":
    main()
