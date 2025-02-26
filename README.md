# 🌌 Stellar Observatory - API de Monitoreo Espacial

## Descripción

**Stellar Observatory** es una API Flask diseñada para simular un observatorio espacial. Permite monitorear el estado de telescopios, sistemas de energía y comunicación en tiempo real.

## Características

- Monitoreo de estado general del observatorio
- Información en tiempo real sobre telescopios y sus objetivos
- Estado de sistemas de soporte como energía y comunicación
- API REST con múltiples endpoints para consulta

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/stellar-observatory.git
   cd stellar-observatory
   ```
2. Crear y activar un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar el servidor Flask:
```bash
python app.py
```

El servidor se ejecutará en `http://127.0.0.1:5000/`

## Endpoints Disponibles

| Método | Endpoint         | Descripción |
|--------|-----------------|-------------|
| GET    | `/`             | Página de bienvenida |
| GET    | `/health`       | Verifica si el observatorio está operativo |
| GET    | `/status`       | Obtiene el estado general del observatorio |
| GET    | `/telescopes`   | Consulta el estado de los telescopios |
| GET    | `/monitor`      | Muestra un informe detallado en tiempo real |

## Ejemplo de Respuesta

### `/status`
```json
{
    "observatory": "Stellar Laboratory",
    "status": "operational",
    "systems": {
        "power": {"status": "normal", "output": "98%"},
        "communication": {"status": "normal", "signal_strength": "excellent"}
    }
}
```

## Tecnologías Utilizadas

- Python 3
- Flask

## Licencia

Este proyecto está bajo la licencia MIT.

