from cloudpathlib import CloudPath

# dispatches to S3Path based on prefix
#root_dir = CloudPath("s3://drivendata-public-assets/")
root_dir = CloudPath("s3://sftpdemo/automate")

root_dir
#> S3Path('s3://drivendata-public-assets/')

# there's only one file, but globbing works in nested folder
for f in root_dir.glob('**/*.txt'):
    text_data = f.read_text()
    print(f)
    print(text_data)
#> s3://drivendata-public-assets/odsc-west-2019/DATA_DICTIONARY.txt
#> Eviction Lab Data Dictionary
#>
#> Additional information in our FAQ evictionlab.org/help-faq/
#> Full methodology evictionlab.org/methods/
#>
#> ... (additional text output truncated)

# use / to join paths (and, in this case, create a new file)
new_file_copy = root_dir / "nested_dir/copy_file.txt"
new_file_copy
#> S3Path('s3://drivendata-public-assets/nested_dir/copy_file.txt')

# show things work and the file does not exist yet
new_file_copy.exists()
#> False

# writing text data to the new file in the cloud
new_file_copy.write_text(text_data)
#> 6933

# file now listed
list(root_dir.glob('**/*.txt'))
#> [S3Path('s3://drivendata-public-assets/nested_dir/copy_file.txt'),
#>  S3Path('s3://drivendata-public-assets/odsc-west-2019/DATA_DICTIONARY.txt')]

# but, we can remove it
new_file_copy.unlink()

# no longer there
list(root_dir.glob('**/*.txt'))
#> [S3Path('s3://drivendata-public-assets/odsc-west-2019/DATA_DICTIONARY.txt')]
