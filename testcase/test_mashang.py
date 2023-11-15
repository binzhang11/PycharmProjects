import pytest


class TestMashang:
    @pytest.mark.smoke
    def test_baili(self):
        print("测试百里老师")

    def test_yiran(self):
        print("测试依然老师")

    @pytest.mark.smoke
    def test_xingyao(self):
        print("测试星耀老师")
