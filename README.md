# Introduction 
This page to collect all the information for the DTDJ MCU Build process on Windows.
# Architecture

Until a better place is found, architecture sketches are maintained in the [20231106-Sprint-11a](https://calsonickansei.sharepoint.com/:i:/s/CloudTransformationPrograms-ELSDevOpsELS-CoreTeam/EaKfb6ijZMlIqxg5pjGjPoMBlHk-SUFQj4zROeYYGtuxcg?e=9TBdTB).

# Getting Started



## Prerequisites

- [Node.js 14](https://github.com/nodesource/distributions/blob/master/README.md) or later
- [Python 3.10.6](https://www.python.org/) or later with [venv](https://docs.python.org/3/library/venv.html)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
- Your workstation configured with your credentials (using `aws configure sso`)

## Configure env

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

To activate your virtualenv:

```
$ source .venv/bin/activate 
            or 
If you are a Windows platform, you would activate the virtualenv like this:
$ source .venv/Scripts/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt