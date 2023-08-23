import os
import json
from awsed.client import DefaultAwsedClient
from awsed.types import *

os.environ['AWSED_ENDPOINT'] = 'https://awsed-dev.ucsd.edu/api'
os.environ['AWSED_API_KEY'] = 'ZKQTo0ySUDhV3Hid'

client = DefaultAwsedClient()

form = ListEnrollmentsForm(
    courseSlugs=['cse110', 'cse120'],
    username='jdoe',
    courseSlug=['cse110', 'cse120']
)

client.list_enrollments_for_environment(form, 'jdoe')
