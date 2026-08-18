from datetime import datetime, timedelta


def date_tool(operation, days=0):
    try:
        today = datetime.now().date()

        if operation == "today":
            return {
                "success": True,
                "date": str(today)
            }

        elif operation == "add_days":
            new_date = today + timedelta(days=days)

            return {
                "success": True,
                "date": str(new_date)
            }

        elif operation == "subtract_days":
            new_date = today - timedelta(days=days)

            return {
                "success": True,
                "date": str(new_date)
            }

        elif operation == "day_name":
            return {
                "success": True,
                "day": today.strftime("%A")
            }

        else:
            return {
                "success": False,
                "error": "Invalid date operation."
            }

    except Exception as e:
        return {
            "success": False,
            "error": f"Date Tool Error: {str(e)}"
        }


if __name__ == "__main__":

    print("Date Tool")
    print("=" * 40)

    print("Today's Date:")
    print(date_tool("today"))

    print("\nDate After 7 Days:")
    print(date_tool("add_days", 7))

    print("\nDate Before 7 Days:")
    print(date_tool("subtract_days", 7))

    print("\nToday's Day:")
    print(date_tool("day_name"))