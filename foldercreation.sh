#!/bin/bash

# Function to create subdirectories for each question
create_subdirectories() {
    local week_folder="Week $1"
    local num_questions="$2"

    if [ ! -d "$week_folder" ]; then
        mkdir "$week_folder"
    fi

    cd "$week_folder"

    for (( i = 1; i <= num_questions; i++ )); do
        mkdir "Question $i"
    done

    echo "Week $1 Folder with $num_questions Subdirectories has been created."
}

# Main script starts here
read -p "What Week is it: " week_number

# Validate if week_number is a number
if [[ ! "$week_number" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a valid number for the week."
    exit 1
fi

read -p "No of questions in Week $week_number: " num_questions

# Validate if num_questions is a number
if [[ ! "$num_questions" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a valid number for the number of questions."
    exit 1
fi

create_subdirectories "$week_number" "$num_questions"

