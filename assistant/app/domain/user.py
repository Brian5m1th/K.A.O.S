from pydantic import BaseModel


class UserContext(BaseModel):
    user_id: str
    username: str
    role: str = "user"
