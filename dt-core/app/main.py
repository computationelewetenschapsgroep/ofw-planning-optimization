import uvicorn
from app.api.api import app
from app.conf.configuration import settings


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = settings.PORT)