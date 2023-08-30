function create-subdirectories {
    param (
        [int]$weekNumber,
        [int]$numQuestions
    )

    $weekFolder = "Week $weekNumber"

    if (-not (Test-Path -Path $weekFolder -PathType Container)) {
        New-Item -Path $weekFolder -ItemType Directory
    }

    Set-Location -Path $weekFolder

    for ($i = 1; $i -le $numQuestions; $i++) {
        $questionFolder = "Question $i"
        New-Item -Path $questionFolder -ItemType Directory

        # Create question.txt file inside the question folder
        New-Item -Path "$questionFolder\question.txt" -ItemType File

        # Create solution.py file inside the question folder
        New-Item -Path "$questionFolder\solution.py" -ItemType File
    }

    Write-Host "Week $weekNumber Folder with $numQuestions Subdirectories has been created."
}

$weekNumber = Read-Host "What Week is it"
if (-not ($weekNumber -match '^\d+$')) {
    Write-Host "Error: Please enter a valid number for the week."
    exit 1
}

$numQuestions = Read-Host "No of questions in Week $weekNumber"
if (-not ($numQuestions -match '^\d+$')) {
    Write-Host "Error: Please enter a valid number for the number of questions."
    exit 1
}

create-subdirectories -weekNumber $weekNumber -numQuestions $numQuestions
