# SPDX-FileCopyrightText: © 2023 Project's authors 
# SPDX-License-Identifier: MIT

import argparse
import json

parser=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--predictions_path", metavar="STRING", help="The JSON file that contains the predictions", type=str, default="pred.val_ours.json")
args=parser.parse_args()

with open("ScanQA_v1.0_val.json","r") as dataset_json:
    dataset = json.load(dataset_json)

with open(args.predictions_path,"r") as predictions_json:
    predictions = json.load(predictions_json)

correct_question_ids = []
for question in dataset:
    # Find the prediction for the given question_id
    for prediction in predictions:
        if prediction["question_id"] == question["question_id"]:
            break

    if prediction["answer_top10"][9] in question["answers"]:
        correct_question_ids.append(question["question_id"])

print("\n".join(correct_question_ids))

