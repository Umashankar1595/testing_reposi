import pytest
@pytest.fixture(scope='module')
def resource_1_setup(request):
    print('\nSetup for resource 1 called')
    def resource_1_setup(request):
        print('\nSetup for resource 1 called')
        def resource_1_teardown():
            print('\nTeardown for resource 1 called')
        request.addfinalizer(resource_1_teardown())
def test_1_using_resource_1(resource_1_setup):
    print('Test 1 uses resource 1')
def test_2_not_using_resource_1():
    print('\nTest 2 does not need resource 1')