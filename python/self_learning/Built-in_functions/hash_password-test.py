import unittest
import hashlib

def password_strength(password):
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    blacklisted_hashes = [
        "098f6bcd4621d373cade4e832627b4f6", # "test"
        "d8578edf8458ce06fbc5bb76a58c5ca4", # "123456"
        "7c4a8d09ca3762af61e59520943dc26494f8941b", # "password"
    ]
    return password_hash not in blacklisted_hashes

class TestPasswordStrength(unittest.TestCase):
    def test_strong_password(self):
        password = "my_strong_password"
        result = password_strength(password)
        self.assertTrue(result)

    def test_weak_password(self):
        password = "password"
        result = password_strength(password)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
