<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png" 
     width="200px"
     height="auto"/>
</p>

# <h1 align="center" id="heading">QuestionMyDoc</h1>

### Objectives 🔍

- [ ] Set up and Test Chain
- [ ] Push Chain to a Hugging Face :hugging_face: Space

### General Diagram of Today's Task

This is a simplified version of the full LangChain application diagram!

![image](https://github.com/FourthBrain/Building-With-LLMs/assets/19699016/1ea9c31a-a7e6-48ed-87b4-cafee3b26587)

### Notebook 📓

We'll be working out of this notebook for this assignment: [🗣️QuestionMyDoc📄 with LangChain](https://colab.research.google.com/drive/1CAE_gdSQlcDsXGc6YbL1GAnnlZPZuE3b?usp=sharing)

### Hugging Face Deployment

First you'll want to set up a new Hugging Face Space! (Documentation [here](https://huggingface.co/spaces/launch))

1. You can do this by navigating to [Hugging Face's Space](https://huggingface.co/spaces)
2. You can select the `Create new Space` button to start making a new space.
3. Name your space something appropriate to your application.
4. Select the appropriate license for your space. 
5. We'll be using Gradio in this example, so for now you'll choose Gradio as your Space SDK - but any will do.
6. You can leave the Space Hardware as the default option.
7. We'll be creating public spaces today, so we'll leave that as default as well.

Second, you'll either follow the on-screen instructions and clone the space (or add it as a remote in this repository) and add contents of the app folder - or you can upload each file individually, or you can edit the files provided in the web based HF repository. 

The end result should be a repository with the contents of the `app` folder host on your Hugging Face space.

In this example, we'll show how this can be done through the web interface. 

1. Navigate to the `Files` tab in the top right of the screen. 
2. Clik the `+ Add file` button in the top right and select the `Upload files` option from the dropdown. 
3. Navigate to your `app` folder in your file explorer/Finder.
4. Select all the files in the `app` folder. Ensure you select the files themselves, not the `app` folder.
5. Click `Open`!

Now that we have our files uploaded, we'll need to do one more step - which is connect our OpenAI API key to the Space. We can do this using Hugging Face Space's secrets feature!

1. Navigate to your Space's `Settings` tab in the top right of the webpage. 
2. Scroll down to the `Repository secrets` section of the settings. 
2. Select `New secret`
4. Name the secret `OPENAI_API_KEY` and paste the OpenAI API key into the `Secret value` textbox.
5. Click `Add new secret`.

With that, you're done - and your space should be functional and let you query your document!

Please ensure you remove your secret once you've shown that the Space is working to avoid any additional API costs!

You could add a parameter to your Gradio app that prompts the user to input their own API key - as is shown in the `NO API KEY` example.

### Results 💯:

At the end of this assignment, you should have a document search application on Hugging Face Spaces.

### Example:

[Here](https://huggingface.co/spaces/FourthBrainGenAI/TalkToMyDoc-Hitch-Hikers-Guide) is an example of a completed assignment.
