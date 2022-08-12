# **Teste Backend Q2Bank**

## ***Siga as etapas abaixo em ordem, para executar a API.***

### Antes de qualquer coisa, será necessario ter as seguintes ferramentas.

* Um editor de texto, recomento utilizar o VisualStudio Code (VsCode).
* Python 3.7 ou acima.
* Se preferir pode utilizar um banco de dados externo, mas por padrão o propio Django ja cria um ambiente de teste em sqlite. Como nesse projeto eu utilizei o PostgreSQL 14, ele vai esta configurado. Irei explicar como alterar essas configurações mais a baixo.

## **Agora vamos iniciar a configuração do projeto.**

> ps. Para o passo a passo abaixo, utilizarei a configuração no windows utilizando o Vscode.

**1. Criação de um ambiente virtual: Utilizarei o terminal do Bash dentro do VsCode. Mas o processo será o mesmo em outros terminais, mudando apenas os comandos.**

* execute o comando `python3 -m venv "nome_da_env"`
* após a criação do ambiente virtual (env), inicie o mesmo, com o comando `source "nome_da_env"/Scripts/activate`

**2.  Agora iremos realizar a instalação das Bibliotecas, com a env ativa, execute os comandos abaixo.**

* `pip install -r requirements.txt` para realizar a instalação das bibliotes.
* Caso ocorra um erro durante a instalação, procure por um responsavel do projeto.

**3. Configuração do Banco de Dados.**

* abra o arquivo `settings.py`, localizado na pasta `setup`
* Encontre o topico `DATABASES`, você encontrará o seguinte codigo:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'DB_NAME'),
        'USER': os.environ.get('DB_USER', 'DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS', 'DB_PASS'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```
* Altere passando as credenciais do seu banco, passando usuario, senha, host...
* Para utilizar o sqlite padrão do django, altere o codigo acima, para:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

``` 

* Para configuração de demais bancos de dados abra o link: [`https://docs.djangoproject.com/pt-br/2.2/howto/legacy-databases/`](https://)

**4. Apos configurar o banco de dados, será necessário a criação das tabelas. para isso é so executar os comandos abaixo**

* Novamente no terminal da aplicação, execute o comando `python manage.py makemigrations`, ele ira mapear as migrações pendentes.
* Apos isso, execute o comando `python manage.py migrate`, para realizar as migrações para o banco de dados.
* Caso ocorra algum erro, o possivel problema pode ser a conexão com o banco, verifique se todos os parametros estão corretos. Caso o erro percista, procure por um responsavel pelo projeto.

**5. Agore que ja instalou as bibliotecas, configurou o banco, e criou as tabelas, so falta criar um usuario admin**

* Ainda no terminal, execute o comando `python manage.py createsuperuser`
> Será exibido uma lista de perguntas, é so preencher tudo, e seu usuario admin estará criado. Lembre-se de sua senha, pois para executar as apis em ambiente externo (postman por exemplo), será necessário passar as credenciais de usuario.
```
py manage.py createsuperuser
Usuário: admin
Endereço de email: admin@admin.com
Password: 
Password (again):
←[31;1mA senha é muito parecida com usuário
Esta senha é muito curta. Ela precisa conter pelo menos 8 caracteres.
Esta senha é muito comum.
←[0mBypass password validation and create user anyway? [y/N]: y
Superuser created successfully.****
```


**6. Antes de subir o servidor, será necessário alterar algumas coisas no codigo.**

* Na pasta `Banco`, abra o arquivo `validators.py`
* Dentro do arquivo, encontre a função `Valida_valorTransferencia`

```
def Valida_valorTransferencia(id, valorTransferencia):
    saldo = requests.get(f"http://127.0.0.1:8000/SaldoBancario/{id}/Saldo/", auth=HTTPBasicAuth('seu_user_admin', 'sua_senha_admin'))
    data = saldo.json()
    if data[0]['saldo_total'] >= valorTransferencia:
        resposta = True
    else:
        resposta = False
    return resposta
```
* Agora altere os dados de autenticação da api, para o seu usuario admin:
```
...
  ,auth=HTTPBasicAuth('seu_user_admin', 'sua_senha_admin'))
...
```
* Salve o arquivo, e abra o `transacao.py`, e repita o processo acima, para todas as rotas, que pedem autenticação.


**7. Agore que ja instalou as bibliotecas, configurou o banco, criou as tabelas e definiu um usuario admin, so falta subir o servidor em localhost**

* No terminal da aplicação, execute: `python manage.py runserver`

**8. Para mais informações sobre a api, abra a documentação.**
* Com o servidor rodando, abra a url: [http://127.0.0.1:8000/documentacao/v1/](https://), ou [[http://127.0.0.1:8000/documentacao/v2/]](https://)
* Observação: O caminho `127.0.0.1:8000` é o localhost padrão do Django. caso você altere esse caminho, é so trocar ele pelo o seu.


### ***Caso Ocorra algum erro durante a instalação, que não esteja descrita acima. Reveja o passo a passo, se o erro percistir, procure por um responsavel pelo projeto.***
