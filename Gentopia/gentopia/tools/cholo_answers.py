from transformers import GPT2Tokenizer, GPT2LMHeadModel
from gentopia.tools.basetool import BaseTool
from pydantic import BaseModel, Field
from typing import AnyStr, Optional, Type, Any
import torch
import os

# class AskQuestionArgs(BaseModel):
#     question: str = Field(..., description="The question to ask based on the scraped content.")

# class CholoAnswers(BaseTool):
#     """Tool that loads scraped text and answers questions based on it."""

#     name = "cholo_answers"
#     description = "A tool to answer questions based on previously scraped and cleaned content."

#     args_schema: Optional[Type[BaseModel]] = AskQuestionArgs

#     def __init__(self, model_name='gpt2'):
#         super().__init__()
#         # Load the GPT-mini-40 model and tokenizer
#         self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
#         self.model = GPT2LMHeadModel.from_pretrained(model_name)
#         self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#         self.model.to(self.device)

#     def load_cleaned_text(self) -> str:
#         """Load the cleaned text from the saved file."""
#         if os.path.exists("cleaned_text.txt"):
#             with open("cleaned_text.txt", "r", encoding="utf-8") as f:
#                 return f.read()
#         else:
#             raise FileNotFoundError("Cleaned text file not found. Run CholoUnderstands first.")

#     def _run(self, question: AnyStr) -> str:
#         """Generate an answer based on the cleaned text and the provided question."""
#         # Load the cleaned text
#         context_text = self.load_cleaned_text()

#         # Combine the context and the question
#         prompt = f"{context_text}\n\nQuestion: {question}\nAnswer:"
        
#         # Generate an answer using the GPT model
#         inputs = self.tokenizer.encode(prompt, return_tensors='pt').to(self.device)
#         output = self.model.generate(inputs, max_length=150, num_return_sequences=1)
#         answer = self.tokenizer.decode(output[0], skip_special_tokens=True)

#         return answer

#     async def _arun(self, *args, **kwargs) -> Any:
#         raise NotImplementedError


# if __name__ == "__main__":
#     # Example usage for answering a question based on the cleaned text
#     cholo = CholoAnswers()
#     question = input("Enter your question: ")
#     answer = cholo._run(question)
#     print(f"Answer:\n{answer}")


# import os
# import openai  # You need the `openai` package installed: pip install openai
# from gentopia.tools.basetool import BaseTool
# from pydantic import BaseModel, Field
# from typing import Optional, Type

# class AskQuestionArgs(BaseModel):
#     question: str = Field(..., description="The question to ask based on the scraped content.")

# class CholoAnswers(BaseTool):
#     """Tool that uses GPT-40-mini to answer questions based on cleaned text."""

#     name = "cholo_answers"
#     description = "A tool to answer questions based on previously cleaned text using GPT-40-mini."

#     args_schema: Optional[Type[BaseModel]] = AskQuestionArgs

#     def __init__(self, api_key: str):
#         super().__init__()
#         self.api_key = api_key
#         openai.api_key = self.api_key

#     def load_cleaned_text(self) -> str:
#         """Load the cleaned text from the saved file."""
#         if os.path.exists("cleaned_text.txt"):
#             with open("cleaned_text.txt", "r", encoding="utf-8") as f:
#                 return f.read()
#         else:
#             raise FileNotFoundError("Cleaned text file not found. Run CholoUnderstands first.")

#     def _run(self, question: str) -> str:
#         """Generate an answer using GPT-40-mini based on the cleaned text and the provided question."""
#         # Load the cleaned text
#         context_text = self.load_cleaned_text()

#         # Combine the context and the question
#         prompt = f"{context_text}\n\nQuestion: {question}\nAnswer:"

#         # Make an API call to GPT-40-mini using the OpenAI API
#         response = openai.Completion.create(
#             engine="gpt-4",  # Adjust this if you have access to another engine like `gpt-40-mini`
#             prompt=prompt,
#             max_tokens=150,
#             n=1,
#             stop=None,
#             temperature=0.7,
#         )

#         answer = response.choices[0].text.strip()
#         return answer

#     async def _arun(self, *args, **kwargs):
#         raise NotImplementedError


# if __name__ == "__main__":
#     # Example usage for answering a question based on the cleaned text
#     API_KEY = "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"  # Add your OpenAI API key here
#     cholo = CholoAnswers(api_key=API_KEY)
#     question = input("Enter your question: ")
#     answer = cholo._run(question)
#     print(f"Answer:\n{answer}")



# Below is the first working code but has v1/compeletion errors



# import openai
# from gentopia.tools.basetool import BaseTool
# from pydantic import BaseModel, Field, PrivateAttr
# from typing import Optional, Type

# class AskQuestionArgs(BaseModel):
#     question: str = Field(..., description="The question to ask based on the scraped content.")

# class CholoAnswers(BaseTool):
#     """Tool that uses GPT-40-mini to answer questions based on cleaned text."""

#     name = "cholo_answers"
#     description = "A tool to answer questions based on previously cleaned text using GPT-40-mini."

#     args_schema: Optional[Type[BaseModel]] = AskQuestionArgs

#     # Define the api_key as a private attribute
#     _api_key: str = PrivateAttr()

#     def __init__(self, api_key: str):
#         super().__init__()
#         self._api_key = api_key
#         openai.api_key = self._api_key

#     def load_cleaned_text(self) -> str:
#         """Load the cleaned text from the saved file."""
#         if os.path.exists("cleaned_text.txt"):
#             with open("cleaned_text.txt", "r", encoding="utf-8") as f:
#                 return f.read()
#         else:
#             raise FileNotFoundError("Cleaned text file not found. Run CholoUnderstands first.")

#     def _run(self, question: str) -> str:
#         """Generate an answer using GPT-40-mini based on the cleaned text and the provided question."""
#         # Load the cleaned text
#         context_text = self.load_cleaned_text()

#         # Combine the context and the question
#         prompt = f"{context_text}\n\nQuestion: {question}\nAnswer:"

#         # Make an API call to GPT-40-mini using the OpenAI API
#         response = openai.Completion.create(
#             engine="gpt-4",  # Adjust this if you have access to another engine like `gpt-40-mini`
#             prompt=prompt,
#             max_tokens=150,
#             n=1,
#             stop=None,
#             temperature=0.7,
#         )

#         answer = response.choices[0].text.strip()
#         return answer

#     async def _arun(self, *args, **kwargs):
#         raise NotImplementedError


# if __name__ == "__main__":
#     # Example usage for answering a question based on the cleaned text
#     API_KEY = "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"  # Add your OpenAI API key here
#     cholo = CholoAnswers(api_key=API_KEY)
#     question = input("Enter your question: ")
#     answer = cholo._run(question)
#     print(f"Answer:\n{answer}")



#



import openai
from gentopia.tools.basetool import BaseTool
from pydantic import BaseModel, Field, PrivateAttr
from typing import Optional, Type

class AskQuestionArgs(BaseModel):
    question: str = Field(..., description="The question to ask based on the scraped content.")

class CholoAnswers(BaseTool):
    """Tool that uses GPT-40-mini to answer questions based on cleaned text."""

    name = "cholo_answers"
    description = "A tool to answer questions based on previously cleaned text using GPT-40-mini."

    args_schema: Optional[Type[BaseModel]] = AskQuestionArgs

    # Define the api_key as a private attribute
    _api_key: str = PrivateAttr()

    def __init__(self, api_key: str):
        super().__init__()
        self._api_key = api_key
        openai.api_key = self._api_key

    def load_cleaned_text(self) -> str:
        """Load the cleaned text from the saved file."""
        if os.path.exists("cleaned_text.txt"):
            with open("cleaned_text.txt", "r", encoding="utf-8") as f:
                return f.read()
        else:
            raise FileNotFoundError("Cleaned text file not found. Run CholoUnderstands first.")

    def _run(self, question: str) -> str:
        """Generate an answer using GPT-40-mini based on the cleaned text and the provided question."""
        # Load the cleaned text
        context_text = self.load_cleaned_text()

        # Prepare the system message and the user question for a chat model
        messages = [
            {"role": "system", "content": f"The following context is based on a webpage: {context_text}"},
            {"role": "user", "content": question}
        ]

        # Make an API call to GPT-40-mini using the OpenAI Chat API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Adjust this if you have access to another engine like `gpt-40-mini`
            messages=messages,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        answer = response['choices'][0]['message']['content'].strip()
        return answer

    async def _arun(self, *args, **kwargs):
        raise NotImplementedError


if __name__ == "__main__":
    # Example usage for answering a question based on the cleaned text
    API_KEY = "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"  # Add your OpenAI API key here
    cholo = CholoAnswers(api_key=API_KEY)
    question = input("Enter your question: ")
    answer = cholo._run(question)
    print(f"Answer:\n{answer}")
