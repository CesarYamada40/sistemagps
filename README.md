# GPS Location Tracker

Aplicativo web para rastreamento de localização GPS com funcionalidades CRUD completas.

## Funcionalidades

- ✅ Busca de endereços com conversão para coordenadas GPS
- 🗺️ Visualização em mapa interativo
- 📝 Adição de descrições às localizações
- 📍 Marcadores no mapa
- 🗑️ Exclusão de localizações
- 📱 Interface responsiva

## Tecnologias Utilizadas

### Backend
- Flask (Python)
- SQLite
- Flask-CORS

### Frontend
- HTML5
- JavaScript
- Leaflet (mapas)
- OpenStreetMap

## Como Executar

### Backend

1. Instalar dependências:
```bash
cd backend
pip install -r requirements.txt
```

2. Iniciar servidor:
```bash
python app.py
```
O backend estará rodando em `http://127.0.0.1:5000`

### Frontend

Abra o arquivo `frontend/index.html` no navegador ou use um servidor web simples:

```bash
cd frontend
python -m http.server 8000
```
O frontend estará disponível em `http://127.0.0.1:8000`

## API Endpoints

- `GET /api/locations` - Lista todas as localizações
- `POST /api/locations` - Adiciona nova localização
- `DELETE /api/locations/{id}` - Remove uma localização
- `PUT /api/locations/{id}` - Atualiza uma localização

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT.
