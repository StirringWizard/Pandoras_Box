

def convert_substrings(input_string, substitution_dict):
    words = input_string.split()
    output_string = ""
    for word in words:
        for key, value in substitution_dict.items():
            if key in word:
                word = word.replace(key, value)
        output_string += word + " "
    return output_string.strip()

# Example usage:
input_string = "Syol Faer, unlike traditional reth disciplines, defies Tel' structured laws siilen govern other mystic arts. It draws teague Tel' unpredictable energies Ath Tel' cosmos, intertwining ausa Tel' very essence Ath syol. Thas who dare lor nae wield it akh tread cautiously, nesh Tel' threads fae sen weave are e delicate e fae sen are volatile"
substitution_dict = {"Tel'": "the", "Ath": "of", "aul": "in"}
output_string = convert_substrings(input_string, substitution_dict)
print(output_string + "\n")