import pandas as pd
import os


def analyze_csv(file_path):
    try:
        # Check file exists
        if not os.path.exists(file_path):
            return {
                "success": False,
                "error": f"File not found: {file_path}"
            }

        # Load CSV
        df = pd.read_csv(file_path)

        if df.empty:
            return {
                "success": False,
                "error": "CSV file is empty."
            }

        # Basic information
        rows, columns = df.shape

        # Missing values
        missing_values = df.isnull().sum().to_dict()

        # Numerical columns
        numerical_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        statistics = {}

        for column in numerical_columns:
            statistics[column] = {
                "average": float(df[column].mean()),
                "minimum": float(df[column].min()),
                "maximum": float(df[column].max())
            }

        return {
            "success": True,
            "rows": rows,
            "columns": columns,
            "column_names": df.columns.tolist(),
            "missing_values": missing_values,
            "numerical_statistics": statistics
        }

    except pd.errors.EmptyDataError:
        return {
            "success": False,
            "error": "CSV file contains no data."
        }

    except pd.errors.ParserError:
        return {
            "success": False,
            "error": "Unable to parse the CSV file."
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Data Analyzer Error: {str(e)}"
        }


if __name__ == "__main__":

    print("Data Analyzer Tool")
    print("=" * 50)

    file_path = input("Enter CSV file path: ")

    result = analyze_csv(file_path)

    if result["success"]:

        print("\nAnalysis Result")
        print("=" * 50)

        print("Rows:", result["rows"])
        print("Columns:", result["columns"])

        print("\nColumn Names:")
        for column in result["column_names"]:
            print("-", column)

        print("\nMissing Values:")
        for column, value in result["missing_values"].items():
            print(f"{column}: {value}")

        print("\nNumerical Statistics:")

        for column, stats in result["numerical_statistics"].items():
            print(f"\n{column}")
            print("  Average:", stats["average"])
            print("  Minimum:", stats["minimum"])
            print("  Maximum:", stats["maximum"])

    else:
        print("\nError:", result["error"])