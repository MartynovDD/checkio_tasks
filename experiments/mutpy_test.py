from unittest import TestCase, main
from electronic_station.task_007_acceptable_password_vi import is_acceptable_password


class AcceptablePasswordMutationTest(TestCase):
    def test_acceptable(self):
        self.assertTrue(is_acceptable_password("abC1dhs"))


if __name__ == "__main__":
    main()
