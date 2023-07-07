FILE_PATH = "books/frankenstein.txt"

def main():
    with open(FILE_PATH) as f:
        file_contents = f.read()
        words = file_contents.split()

        count = {}
        for word in words:
            for c in word:
                count[c.lower()] = count.get(c.lower(), 0) + 1

        sorted_count = [(k, v) for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True) if k.isalpha()]

        print(f"--- Begin report of {FILE_PATH} ---")
        print(f"{len(words)} words found in the document")
        print()
        for char, num in sorted_count:
            print(f"The '{char}' character was found {num} times")
        print("--- End report ---")
        

if __name__ == "__main__":
    main()