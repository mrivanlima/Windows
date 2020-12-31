

$FileName = Read-Host -Prompt 'New object path name:'

$path=[Environment]::GetFolderPath("MyDocuments")
$FullPath = "$path\$FileName"

Write-Output $FullPath

aws s3 cp $FullPath s3://mrivanlima/$FileName
