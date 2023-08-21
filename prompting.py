"""The prompting module that takes any plant text or input/insturction/output dict  and format 
into a prompt that can be used for training or testing.
"""

import random


class Prompting:
    def __init__(
        self, input_key="input", output_key="output", instruction_key="instruction"
    ):
        self.input_key = input_key
        self.output_key = output_key
        self.instruction_key = instruction_key

        self.prompt_dict = {
            "prompt_no_input": "\n\nHuman: {instruction}\n\nAssistant: {output}",
            "prompt_input": "\n\nHuman: {instruction} {input}\n\nAssistant: {output}",
        }

        self.prompt_dict_reverse = {
            "prompt_no_input": "\n\nHuman: {instruction}\n\nAssistant: {output}",
            "prompt_input": "\n\nHuman: {input} {instruction}\n\nAssistant: {output}",
        }

    def format_prompt(self, input, output, instruction, random_context_order=False):
        """Format the input, output, instruction into a prompt.
        Args:x
            input (str): the input text
            output (str): the output text
            instruction (str): the instruction text
        Returns:
            str: the formatted prompt
        """
        prompt_dict = (
            random.choice([self.prompt_dict, self.prompt_dict_reverse])
            if random_context_order
            else self.prompt_dict
        )
        if input.strip() == "":
            text = prompt_dict["prompt_no_input"].format(
                instruction=instruction, output=output
            )
        else:
            text = prompt_dict["prompt_input"].format(
                instruction=instruction, input=input, output=output
            )
        return text

    def format_prompt_from_dict(self, data, random_context_order=False):
        """Format the input, output, instruction into a prompt.
        Args:
            input (str): the input text
            output (str): the output text
            instruction (str): the instruction text
        Returns:
            str: the formatted prompt
        """

        prompt_dict = (
            random.choice([self.prompt_dict, self.prompt_dict_reverse])
            if random_context_order
            else self.prompt_dict
        )

        if data[self.input_key].strip() == "":
            text = prompt_dict["prompt_no_input"].format(
                instruction=data[self.instruction_key], output=data[self.output_key]
            )
        else:
            text = prompt_dict["prompt_input"].format(
                instruction=data[self.instruction_key],
                input=data[self.input_key],
                output=data[self.output_key],
            )
        return text

    def format_prompt_from_plain_text(self, plain_text):
        """Format the input, output, instruction into a prompt.
        Args:
            plain_text (str): the input text
        Returns:
            str: the formatted prompt
        """
        text = self.prompt_dict["prompt_input"].format(
            instruction="", input=plain_text, output=""
        )
        return text
