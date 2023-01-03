============================
How to update MX-tools
============================

Pre-requisites:

1. Create token for pypi for project and place in github secret vault
2. Setup feedstock so that mxtools conda package is built on pypi release 

Steps to update an push to mxtools

1. Add to tag after the code has been pushed
2. Create release in github. Add info related to release
3. Wait for conda forge package release or manually create one 
4. Create LSDC conda environment. In github.com/nsls2-conda-envs/lsdc-server, update the yaml build files to point to the new version of mxtools
5. Wait for merging of yaml file changes, after which github will kick off artifact build.
6. Use conda env built here for the LSDC server conda env 