import os


def read_file(file_path):
    try:
        if not os.path.exists(file_path):
            return {
                "success": False,
                "error": f"File not found: {file_path}"
            }

        if not os.path.isfile(file_path):
            return {
                "success": False,
                "error": "The provided path is not a file."
            }

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        if not content.strip():
            return {
                "success": False,
                "error": "File is empty."
            }

        return {
            "success": True,
            "file": file_path,
            "content": content
        }

    except UnicodeDecodeError:
        return {
            "success": False,
            "error": "File encoding is not supported."
        }

    except PermissionError:
        return {
            "success": False,
            "error": "Permission denied while reading the file."
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"File Reader Error: {str(e)}"
        }


if __name__ == "__main__":

    file_path = input("Enter file path: ")

    result = read_file(file_path)

    if result["success"]:
        print("\nFile Content")
        print("=" * 50)
        print(result["content"])
    else:
        print("\nError:", result["error"])