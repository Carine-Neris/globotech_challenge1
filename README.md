# Aplicativo Web para cadastro de funcionários

Esté é um aplicativo para cadastro de funcionários.

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

### Sem Docker
No terminal: 
```
git clone https://github.com/Carine-Neris/globotech_challenge1.git
python -m venv .venv
.venv/Script/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Com Docker

Com docker
-----------

No terminal

``` bash
git clone https://github.com/Carine-Neris/globotech_challenge1.git
cd pasta-do-projeto
docker-compose build
docker-compose up
```

Criar superusuário para o primeiro acesso ao sistema

```bash
docker-compose exec web python manage.py createsuperuser
```