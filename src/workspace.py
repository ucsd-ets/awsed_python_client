import os
from awsed.client import DefaultAwsedClient
from awsed.types import *

os.environ['AWSED_ENDPOINT'] = 'https://awsed-dev.ucsd.edu/api'
os.environ['AWSED_API_KEY'] = 'ZKQTo0ySUDhV3Hid'

client = DefaultAwsedClient()

var = client.list_pools_under_root('root')
print(var)

var = client.post_course_environment('course', AssociateCourseEnvironmentRequestBody("a", "b", "c"))
print(var)


