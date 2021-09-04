import os

corrections = 0
corrected_text = []
for file in os.listdir(os.getcwd() + '\ex45'):
    with open(os.path.join(os.getcwd() + '\ex45\corrected.txt'), 'w') as f:
        f.close()
        if file != 'corrected.txt':
            path = os.getcwd() + f'\ex45\{file}'
            with open(path, 'r') as f:
                content = f.read()
                for word in content.split():
                    if 'utilize' in word:
                        corrected = content.replace(word, 'use')
                        corrections += 1
                        print(corrected)
                        with open(os.path.join(os.getcwd() + '\ex45\corrected.txt'), 'a') as f:
                            f.write(corrected)
print(f'Number of corrections: {corrections}.')