# AWSed Python Client

`awsed_python_client` is a python client for the `awsed.ucsd.edu` API. Refer to [API.md](API.md) for a list of commands.

# Usage

## Installation

To install awsed `awsed_python_client` run:

```
pip install git+https://github.com/ucsd-ets/awsed_python_client@VERSION
```

or add it to `requirements.txt`:

```
git+https://github.com/ucsd-ets/awsed_python_client@VERSION
```

## Getting Started

Please follow the installation procedure and initialize the client as such:

```python3
from awsed.client import DefaultClient
awsed_client = DefaultClient(endpoint='awsed_endpoint.com', awsed_api_key='42')
```

# Development

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
