import autogen
import os
import dotenv

dotenv.load_dotenv()

config_list = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.getenv("OPENAI_API_KEY")
    }
]

def cleanup(paper):
    completion = autogen.Completion.create(
        config_list=config_list,
        context={"paper": f"{paper}"},
        prompt="{paper}\nTASK:\nCleanup and format the file. Keep title and body. Get rid of the names, links, references, leftovers and the word 'Abstract'.",
        allow_format_str_template=True,
        seed=1,
    )
    abstract = completion["choices"][0]["message"]["content"]
    print(abstract)
    
    return completion


if __name__ == "__main__":
    with open('file4.txt', 'r') as file:
        test_message = file.read()
        
    cleanup(test_message)