import pytest


class TestNew_demo:

    @pytest.mark.dependency(name="test_01_piyush")  # Explicitly naming the test
    def test_01_piyush(self):
        print("hello Piyush")
        assert 1 + 2 == 7  # This test will fail

    @pytest.mark.dependency(depends=["test_01_piyush"])  # Match the correct name
    def test_02_akash(self):
        print("hello Akash")
        assert True  # Should run only if test_01_piyush passes
