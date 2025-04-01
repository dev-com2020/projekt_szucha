# zmokuj metody send_email w serwisie

import unittest
from unittest.mock import Mock

class UserService:
    def send_email(self,user_id):
        pass

class UserController:
    def __init__(self,service):
        self.service = service
    
    def notify_user(self, user_id):
        self.service.send_email(user_id)

class TestUserContoller(unittest.TestCase):
    def test_notify_user_calls_email(self):
        mock_service = Mock()
        controller = UserController(mock_service)
        controller.notify_user(123)
        mock_service.send_email.assert_called_once_with(123)