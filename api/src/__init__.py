from fastapi import FastAPI, Request #pylint ignore
from .status import Status
from .routes import StatusResponse


def create_app():
    app = FastAPI()
    status = Status()
    
    # Create Root 
    @app.get("/")
    async def root(hello):
        print(hello)
        return hello 
    @app.get("/status")
    async def status_method() -> StatusResponse:
        return StatusResponse(status_code=status.status, message=status.message, online=True if status.status < 3 else False)
    @app.post("/status")
    async def update_status_method(New_Status: StatusResponse) -> StatusResponse:
        status.changeStatus(status=New_Status.status_code, message=New_Status.message)
        return StatusResponse(status_code=status.status, message=status.message, online=True if status.status < 3 else False)
    
    @app.middleware(request: Request, call_next):
    def authentication():
    return app, status
