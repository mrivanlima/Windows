

$BucketName = Read-Host -Prompt 'New bucket name:'

#List buckets
$Buckets = aws s3api list-buckets --query "Buckets[].Name" | ConvertFrom-Json


#Create Bucket
if($Buckets.count -eq 0)
{
    aws s3api create-bucket --bucket $BucketName --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2 --acl private
    Write-Output "Bucket $BucketName created!"
    $Buckets += $BucketName
}
else
{
   Write-Output "Bucket $BucketName already exists!"
}
<#
if($Buckets.count -ne 0)
{
   foreach($Bucket in $Buckets)
   {
      aws s3api delete-bucket --bucket $Bucket --region us-west-2
      Write-Output "Bucket $Bucket has been deleted!"

   }
}
#>
