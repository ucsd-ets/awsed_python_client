from aws_ed_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://awsed.ucsd.edu", token="PKWE...")

print(client.get_headers())

from aws_ed_api_client.models import UserResult
from aws_ed_api_client.api.users import describe_environment
from aws_ed_api_client.api.courses import describe_course

from aws_ed_api_client.types import Response

my_data = describe_environment.sync_detailed(client=client, username="rmankini")
print(my_data)

my_data = describe_course.sync(client=client, course="TEST_NBGRADER")
print(my_data)
