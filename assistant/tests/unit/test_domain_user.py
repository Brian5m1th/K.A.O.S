from app.domain.user import UserContext


class TestUserContext:
    def test_create_with_default_role(self):
        ctx = UserContext(user_id="user1", username="test_user")
        assert ctx.user_id == "user1"
        assert ctx.username == "test_user"
        assert ctx.role == "user"

    def test_create_with_custom_role(self):
        ctx = UserContext(user_id="admin1", username="admin", role="admin")
        assert ctx.role == "admin"

    def test_to_dict(self):
        ctx = UserContext(user_id="u1", username="name")
        data = ctx.model_dump()
        assert data == {"user_id": "u1", "username": "name", "role": "user"}
