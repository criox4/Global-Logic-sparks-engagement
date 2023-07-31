#!/bin/bash

create_subdirectories() {
    local week_folder="Week $1"
    local num_questions="$2"

    if [ ! -d "$week_folder" ]; then
        mkdir "$week_folder"
    fi

    cd "$week_folder"

    for (( i = 1; i <= num_questions; i++ )); do
        local question_folder="Question $i"
        mkdir "$question_folder"

        # Create question.txt file inside the question folder
        touch "$question_folder/question.txt"
    done

    echo "Week $1 Folder with $num_questions Subdirectories has been created."
}

read -p "What Week is it: " week_number

if [[ ! "$week_number" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a valid number for the week."
    exit 1
fi

read -p "No of questions in Week $week_number: " num_questions

if [[ ! "$num_questions" =~ ^[0-9]+$ ]]; then
    echo "Error: Please enter a valid number for the number of questions."
    exit 1
fi

create_subdirectories "$week_number" "$num_questions"
