import csv
from datetime import datetime

results = [
    {
        "Provider": "OpenAI",
        "Model": "GPT-5 mini",
        "Status": "Not Available",
        "Response Time (sec)": "N/A",
        "Input Tokens": "N/A",
        "Output Tokens": "N/A",
        "Total Tokens": "N/A",
        "Accuracy": "N/A",
        "Reason": "API quota unavailable ($0)"
    },
    {
        "Provider": "Claude",
        "Model": "Claude Sonnet",
        "Status": "Not Available",
        "Response Time (sec)": "N/A",
        "Input Tokens": "N/A",
        "Output Tokens": "N/A",
        "Total Tokens": "N/A",
        "Accuracy": "N/A",
        "Reason": "Insufficient API credits"
    },
    {
        "Provider": "Gemini",
        "Model": "gemini-3.6-flash",
        "Status": "Success",
        "Response Time (sec)": 11.73,
        "Input Tokens": 63,
        "Output Tokens": 255,
        "Total Tokens": 1792,
        "Accuracy": "5/5",
        "Reason": "Live test completed"
    },
    {
        "Provider": "Groq",
        "Model": "openai/gpt-oss-20b",
        "Status": "Success",
        "Response Time (sec)": 1.27,
        "Input Tokens": 124,
        "Output Tokens": 300,
        "Total Tokens": 424,
        "Accuracy": "5/5",
        "Reason": "Live test completed"
    }
]

filename = "results/provider_comparison_results.csv"

fieldnames = [
    "Provider",
    "Model",
    "Status",
    "Response Time (sec)",
    "Input Tokens",
    "Output Tokens",
    "Total Tokens",
    "Accuracy",
    "Reason"
]

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("=" * 60)
print("DAY 25 - FINAL PROVIDER COMPARISON")
print("=" * 60)

for result in results:
    print(
        f"{result['Provider']:10} | "
        f"{result['Status']:12} | "
        f"Speed: {result['Response Time (sec)']} sec | "
        f"Accuracy: {result['Accuracy']}"
    )

print("\nCSV report created successfully.")
print(f"File: {filename}")
print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")