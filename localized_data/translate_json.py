import json
from googletrans import Translator

def translate_json(input_file, output_file):
    # Load the JSON file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    translator = Translator()
    
    # Translate values
    def translate_values(obj):
        if isinstance(obj, dict):
            return {key: translate_values(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [translate_values(item) for item in obj]
        elif isinstance(obj, str):
            return translator.translate(obj, src='auto', dest='en').text
        else:
            return obj

    translated_data = translate_values(data)
    
    # Save the translated JSON
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(translated_data, file, ensure_ascii=False, indent=4)

# Example usage
input_path = "c:\\Users\\Hp 745 g6\\Documents\\hachimi\\localized_data\\input.json"
output_path = "c:\\Users\\Hp 745 g6\\Documents\\hachimi\\localized_data\\output.json"
translate_json(input_path, output_path)
