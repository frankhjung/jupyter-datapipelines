# Kaggle Training - Data Pipelines

## Day 1 - Versioning Data

  * introduction to dataset versioning tools
  * exercise to adjust versioning a dataset on [Kaggle](https://www.kaggle.com/)

## Day 2 - Validation & Creating Datasets from URLs

  * loading data from a URL
  * validating data

## Day 3 - Automated Data Pipelines


## Dependencies

  * Use either of these two Docker images
    * [clutteredcode/python3-alpine-pandas](https://hub.docker.com/r/clutteredcode/python3-alpine-pandas)
    * [python:3.7.2-stretch](https://hub.docker.com/_/python)
  * [Python 3](https://python.org)
  * [pandas](https://pandas.pydata.org)
  * [numpy](https://www.numpy.org)
  * [GNU R](https://www.r-project.org/)

## Repositories

This project is mirrored at 3 different Git repositories. The reason for this
was to explore features that each have to offer. In particular what pipeline
support each provide.

### GitLab

[GitLab](https://gitlab.com) pipelines are configured using
[.gitlab-ci.yml](.gitlab-ci.yml). Each branch has it's own configuration:

* [master:.gitlab-ci.yml](https://gitlab.com/theMarloGroup/jupyter-notebooks/datapipelines/blob/master/.gitlab-ci.yml)
* [gnur:.gitlab-ci.yml](https://gitlab.com/theMarloGroup/jupyter-notebooks/datapipelines/blob/gnur/.gitlab-ci.yml)

### Bitbucket

[Bitbucket](https://bitbucket.org) pipelines are configured using
[bitbucket-pipelines.yml](https://bitbucket.org/frankhjung/jupyter-datapipelines/src/master/bitbucket-pipelines.yml).

The same configuration is used for each branch.

### GitHub

[GitHub](https://github.com) uses [Azure pipelines](https://github.com/marketplace/azure-pipelines).

The pipeline configuration is
[azure-pipelines.yml](https://github.com/frankhjung/jupyter-datapipelines/blob/master/azure-pipelines.yml).

This is the link to see pipeline build history, https://dev.azure.com/FrankJung/

See also [python pipeline
documentation](https://docs.microsoft.com/azure/devops/pipelines/languages/python).

