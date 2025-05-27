from py.functions import load_settings, save_settings, encrypt, decrypt
import json

def is_encrypted(value):
	return isinstance(value, str) and value.startswith("ENC(") and value.endswith(")")
	

def encrypt_json_values(data):
	if isinstance(data, dict):
		return {key: encrypt_json_values(value) for key, value in data.items()}
	elif isinstance(data, list):
		return [encrypt_json_values(item) for item in data]
	elif isinstance(data, str):
		return data if is_encrypted(data) else encrypt(data)
	elif isinstance(data, (int, float, bool)):
		return encrypt(str(data))
	else:
		return data

def main(input_file, output_file):
	with open(input_file, 'r', encoding='utf-8') as f:
		data = json.load(f)

	encrypted_data = encrypt_json_values(data)

	with open(output_file, 'w', encoding='utf-8') as f:
		json.dump(encrypted_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
	main("./json/settings.json", "./json/settings.json")
