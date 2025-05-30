import google.generativeai as genai
genai.configure(api_key="AIzaSyBBXujpMN8-HzAPrZptQGiJZ2O5yCsDyW4")
print(list(genai.list_models()))
