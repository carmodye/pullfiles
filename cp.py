from cloudpathlib import CloudPath

cp = CloudPath("s3://sftpdemo/automate")
cp.download_to("/home/carmodye/code/pullfiles/localfile")

