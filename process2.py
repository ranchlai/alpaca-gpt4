from datasets import load_dataset
import os
import json
from prompting import Prompting

dataset = load_dataset("teknium/GPT4-LLM-Cleaned")
prompting = Prompting()

os.makedirs("data/GPT4-LLM-Cleaned", exist_ok=True)

for key in dataset.keys():
    subdataset = dataset[key]
    data = []
    for i in range(len(dataset[key])):
        input = subdataset[i]["input"]
        output = subdataset[i]["output"]
        instruction = subdataset[i]["instruction"]

        #  remove all \n\n with \n
        input = (
            input.replace("\n\n", "\n")
            .replace("\nHuman", "\n\nHuman")
            .replace("\nAssistance", "\n\nAssistance")
        )
        output = (
            output.replace("\n\n", "\n")
            .replace("\nHuman", "\n\nHuman")
            .replace("\nAssistance", "\n\nAssistance")
        )
        instruction = (
            instruction.replace("\n\n", "\n")
            .replace("\nHuman", "\n\nHuman")
            .replace("\nAssistance", "\n\nAssistance")
        )

        text = prompting.format_prompt(
            input=input, output=output, instruction=instruction
        )
        data.append(
            {"text": text, "input": input, "output": output, "instruction": instruction}
        )

    with open("data//GPT4-LLM-Cleaned/{}.json".format(key), "w") as f:
        json.dump(data, f, indent=4)

    print("Finished writing {} lines to data/GPT4-LLM-Cleaned/{}.json".format(len(data), key))
