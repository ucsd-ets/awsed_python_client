from abc import ABC, abstractmethod
from typing import Optional, Any, Dict


class AbstractAwsedClient(ABC):
    """This is a default implementation of the AwsedClient interface. It uses the requests library to make HTTP requests to the AWSEd API.

    Raises:
        HTTPError: If the request fails with a 4xx or 5xx status code, an HTTPError is raised. Inherits from RequestException.
        Timeout: If the request times out, a Timeout is raised. Inherits from RequestException.
        DaciteError: If the response JSON cannot be parsed into the expected dataclass, a DaciteError is raised.
    """

    def __init__(self, endpoint: str, awsed_api_key: str, global_timeout: int = 10):
        self.endpoint = endpoint
        self.awsed_api_key = awsed_api_key
        self.global_timeout = global_timeout

    @abstractmethod
    def describe_user(self, username: str) -> Any:
        """
        Retrieves detailed information about a specified user.

        Args:
        username: A string representing the username of the user to be described.

        Returns:
        Detailed information about the specified user.
        """
        pass

    @abstractmethod
    def list_user_launch_profiles(self, username: str) -> Any:
        """
        Retrieves a list of launch profiles associated with a specified user.

        Args:
        username: A string representing the username of the user.

        Returns:
        A list of launch profiles associated with the user.
        """
        pass

    @abstractmethod
    def list_enrollments(self, form: Any, username: Optional[str] = None) -> Any:
        """
        Retrieves a list of enrollments based on provided criteria.

        Args:
        form: An object representing the criteria for enrollment listing.
        username: Optional; a string representing the username of the user to filter enrollments by.

        Returns:
        A list of enrollments that match the provided criteria.
        """
        pass

    @abstractmethod
    def import_enrollments(self, csv_content: str, dry_run: bool = False) -> str:
        """Imports enrollment data from provided CSV content.

        Args:
            csv_content: A string containing the CSV content of enrollments.
            dry_run: A boolean to check if it's a test run without actually importing.

        Returns:
            A string indicating success or failure of the operation.
        """
        pass

    @abstractmethod
    def list_pools_under_root(self, pool_root_name: str) -> Any:
        """Lists all pools under the given root.

        Args:
            pool_root_name: A string representing the root name of the pool.

        Returns:
            An object representing the pools under the root.
        """
        pass

    @abstractmethod
    def post_course_environment(self, course_name: str, course_environment: Any) -> Any:
        """Creates a new course environment.

        Args:
            course_name: A string representing the name of the course.
            course_environment: An object representing the environment details to associate with the course.

        Returns:
            An object confirming the creation of the course environment.
        """
        pass

    @abstractmethod
    def get_course_environment(self, course: str, environment: str) -> Any:
        """Retrieves details of a specific course environment.

        Args:
            course: A string representing the name of the course.
            environment: A string representing the environment of interest.

        Returns:
            An object representing the details of the specified course environment.
        """
        pass

    @abstractmethod
    def patch_course_environment(
        self, course: str, environment: str, modification: Any
    ) -> Any:
        """Updates details of a specific course environment.

        Args:
            course: A string representing the name of the course.
            environment: A string representing the environment of interest.
            modification: An object containing the modifications to be applied to the environment.

        Returns:
            An object confirming the modifications to the course environment.
        """
        pass

    @abstractmethod
    def list_course_environments(self, request: Any) -> Any:
        """
        Lists the environments associated with a specific course.

        Args:
            request: The request object containing details to filter the environments.

        Returns:
            A list or an object containing the details of the course environments.
        """
        pass

    @abstractmethod
    def generate_aws_credentials(self, course: str, role: str) -> str:
        """
        Generates AWS credentials for a given course and role.

        Args:
            course: The name or identifier of the course.
            role: The AWS role associated with the course.

        Returns:
            A string containing the AWS credentials.
        """
        pass

    @abstractmethod
    def list_file_systems(self) -> Any:
        """
        Lists the file systems.

        Returns:
            A list or an object containing the details of the file systems.
        """
        pass

    @abstractmethod
    def describe_file_system(self, file_system: str) -> Any:
        """
        Provides a detailed description of the specified file system.

        Args:
          file_system (str): The name or identifier of the file system.

        Returns:
          Any: An object or data structure containing details of the file system.
        """

        pass

    @abstractmethod
    def list_courses(self, username: str = None, tag: str = None) -> Any:
        """
        Lists the courses based on the given filters.

        Args:
            username: (Optional) The username to filter the courses.
            tag: (Optional) A tag associated with the courses to be listed.

        Returns:
            A list or an object containing the details of the courses.
        """
        pass

    @abstractmethod
    def create_course(self, course: Any) -> Any:
        """
        Creates a new course entry.

        Args:
            course: An object or data structure containing the details of the course to be created.

        Returns:
            An object or a response indicating the status of course creation.
        """
        pass

    @abstractmethod
    def list_course_launch_profiles(self, course: str) -> Any:
        """
        Lists the launch profiles associated with a specific course.

        Args:
            course: The name or identifier of the course.

        Returns:
            A list or an object containing the details of the course launch profiles.
        """

    pass

    @abstractmethod
    def create_course_launch_profile(self, course: str, launch_profile: Any) -> str:
        """
        Creates a launch profile for the specified course.

        Args:
          course (str): The name or identifier of the course.
          launch_profile (Any): The data or object describing the launch profile.

        Returns:
          str: A confirmation or identifier related to the newly created launch profile.
        """
        pass

    @abstractmethod
    def describe_course(self, course: str) -> Any:
        """
        Provides a detailed description of the specified course.

        Args:
          course (str): The name or identifier of the course.

        Returns:
          Any: An object or data structure containing details of the course.
        """

        pass

    @abstractmethod
    def update_course(self, course: str, course_data: Any) -> str:
        """
        Updates the information or content of the specified course.

        Args:
          course (str): The name or identifier of the course.
          course_data (Any): The new data or content to update the course with.

        Returns:
          str: A confirmation or identifier indicating the update status."""

        pass

    @abstractmethod
    def list_course_teams(self, course: str) -> Any:
        """
        Lists all teams associated with the specified course.

        Args:
          course (str): The name or identifier of the course.

        Returns:
          Any: A list or data structure containing teams related to the course."""

        pass

    @abstractmethod
    def list_enrollments_slug(self, slug: str) -> Any:
        """
        Lists all enrollments associated with the specified slug.

        Args:
          slug (str): The unique slug or identifier for a set of enrollments.

        Returns:
          Any: A list or data structure containing enrollments related to the slug."""

        pass

    @abstractmethod
    def list_enrollments_roster(self, slug: str) -> Any:
        """
        List the enrollments roster for a given slug.

        Args:
            slug (str): The slug for which to list the enrollments roster.

        Returns:
            Any: An object representing the enrollments roster.
        """
        pass

    @abstractmethod
    def upload_enrollments(self, csv_content: str, dry_run: bool = False) -> str:
        """
        Upload enrollments from a CSV file.

        Args:
            csv_content (str): The content of the CSV file to upload.
            dry_run (bool, optional): Whether to perform a dry run. Defaults to False.

        Returns:
            str: A message indicating the success or failure of the upload.
        """
        pass

    @abstractmethod
    def list_teams(self, username: str) -> Any:
        """
        List the teams for a given username.

        Args:
            username (str): The username for which to list the teams.

        Returns:
            Any: An object representing the teams.
        """
        pass
