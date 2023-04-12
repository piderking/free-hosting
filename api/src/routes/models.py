from pydantic import BaseModel

class StatusResponse(BaseModel):
    message: str
    status_code: int
    online: bool
    
