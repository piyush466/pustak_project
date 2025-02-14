import pytest

class TestNewDemo:

    @pytest.mark.order(2)  # Execute second
    def test_01_piyush(self):
        print("Executing test_01_piyush")
        assert 1 + 2 == 3

    @pytest.mark.order(1)  # Execute first
    def test_02_akash(self):
        print("Executing test_02_akash")
        assert True

    @pytest.mark.order(3)  # Execute third
    def test_03_john(self):
        print("Executing test_03_john")
        assert True

    @pytest.mark.order(4)  # Execute fourth
    def test_04_doe(self):
        print("Executing test_04_doe")
        assert True
