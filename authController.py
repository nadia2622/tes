class AuthController:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def login(self, username, password):
        if self.auth_service.authenticate(username, password):
            return "Login successful"
        else:
            return "Invalid credentials"

    def logout(self):
        return "Logout successful"
    
    def forgot_password(self, email):
        if self.auth_service.send_reset_link(email):
            return "Password reset link sent"
        else:
            return "Email not found"