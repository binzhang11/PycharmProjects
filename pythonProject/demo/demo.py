import pytest


class TestStorm:
    def test_a(self):
        print('aaa')
        assert  'a'=='a'

    def test_b(self):
        print('bbbb')
        assert 'b'=='b'

if __name__ == '__main__':
    pytest.main()