# GPS Location Tracker

Aplicativo web para rastreamento de localização GPS com funcionalidades CRUD completas.

## Estrutura do Projeto

```
ProjetoLocalizacaoGPS/
├── backend/               # API Django
│   ├── gps_tracker/      # Configurações do projeto
│   ├── locations/        # App de localizações
│   └── manage.py
├── frontend/             # Aplicação React
│   ├── public/
│   └── src/
└── README.md
```

## Como Executar

### Backend (Django)

1. Criar e ativar ambiente virtual:
```bash
cd backend
python -m venv env
env\Scripts\activate  # Windows
```

2. Instalar dependências:
```bash
pip install -r requirements.txt
```

3. Executar migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Criar superusuário:
```bash
python manage.py createsuperuser
```

5. Iniciar servidor:
```bash
python manage.py runserver
```

### Frontend (React)

1. Instalar dependências:
```bash
cd frontend
npm install
```

2. Iniciar aplicação:
```bash
npm start
```

## Funcionalidades

- ✅ CRUD completo de localizações
- 🗺️ Visualização em mapa interativo
- 📱 Interface responsiva
- 🔒 Autenticação de usuários
- 📍 Rastreamento GPS em tempo real

## API Endpoints

- `GET /api/locations/` - Listar localizações
- `POST /api/locations/` - Criar localização
- `GET /api/locations/{id}/` - Detalhes da localização
- `PUT /api/locations/{id}/` - Atualizar localização
- `DELETE /api/locations/{id}/` - Deletar localização

## Tecnologias

- **Backend**: Django, Django REST Framework
- **Frontend**: React, Leaflet
- **Banco de Dados**: PostgreSQL
- **Autenticação**: JWT

## Licença

MIT
