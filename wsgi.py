"""
Startup da aplicacao.
"""

from flasgger.base import Swagger
from controller.rest import create_app

app = create_app('config.default')
app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "specs": [
        {
            "version": "1.0.0",
            "title": "Agrines S3AIR",
            "endpoint": 'v1_spec',
            "route": '/',
            "description": "Api CORE do Pagamento Escritural."
        }
    ]
}

Swagger(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
