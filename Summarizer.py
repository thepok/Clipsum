from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

import tkinter as tk

import pyperclip


openai = OpenAI(max_tokens=-1)

prompt = PromptTemplate(
    input_variables=["text"],
    template="""{text}
    
    Bullet points:""")

chain = LLMChain(llm=openai, prompt=prompt)


# Create a new window
root = tk.Tk()

# Set the window title
root.title("Message")

# Set the window's size and position
root.geometry("{}x{}+{}+{}".format(
    round(root.winfo_screenwidth() * 0.8),  # Set the width to 80% of the screen width
    round(root.winfo_screenheight() * 0.8), # Set the height to 80% of the screen height
    round(root.winfo_screenwidth() * 0.1),  # Set the x-position to 10% of the screen width
    round(root.winfo_screenheight() * 0.1)  # Set the y-position to 10% of the screen height
))

# Create a canvas with a scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the label
frame = tk.Frame(canvas)

# Create a label with the text
label = tk.Label(frame, text=chain.predict(text=pyperclip.paste()), wraplength=round(root.winfo_screenwidth() * 0.8))

# Place the label in the frame
label.pack()

# Place the frame in the canvas
canvas.create_window((0, 0), window=frame, anchor="nw")

# Update the scrollregion of the canvas
canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# Place the canvas and scrollbar in the window
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Start the event loop
root.mainloop()
